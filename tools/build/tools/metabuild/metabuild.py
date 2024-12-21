#!/usr/bin/env python3

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import re
import os
import sys
import types

import subprocess
check_output = lambda x : subprocess.check_output(x).decode('cp437').strip()

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, os.path.join(THIS_DIR, '..'))

import ankibuild.util


# glob.py from BUCK project
# https://github.com/facebook/buck/blob/master/src/com/facebook/buck/json/buck_parser/glob_internal.py
# Glob implementation in python.

from pathlib import Path

def is_special(pat):
    """Whether the given pattern string contains match constructs."""
    return "*" in pat or "?" in pat or "[" in pat

def path_contains_dotdot(relative_path):
    for p in relative_path.parts:
        if p == '..':
            return True
    return False

def path_component_contains_dot(relative_path):
    for p in relative_path.parts:
        if p.startswith('.'):
            return True
    return False


def glob_internal(includes, excludes, project_root_relative_excludes, include_dotfiles, include_dotdotfiles,
                  search_base_path, project_root):
    search_base = Path(search_base_path)
    if not include_dotdotfiles and path_contains_dotdot(search_base):
        raise ValueError('Search path may not contain ..')
    def includes_iterator():
        for pattern in includes:
            for path in search_base.glob(pattern):
                if not include_dotdotfiles and path_contains_dotdot(path):
                    raise ValueError('Include path may not contain ..')
                # TODO(beng): Handle hidden files on Windows.
                if path.is_file() and \
                        (include_dotfiles or not path_component_contains_dot(
                            path.relative_to(search_base))):
                    yield path

    non_special_excludes = set()
    match_excludes = set()
    for pattern in excludes:
        if is_special(pattern):
            match_excludes.add(pattern)
        else:
            non_special_excludes.add(pattern)

    def exclusion(path):
        relative_to_search_base = path.relative_to(search_base)
        if relative_to_search_base.as_posix() in non_special_excludes:
            return True
        for pattern in match_excludes:
            result = relative_to_search_base.match(pattern)
            if result:
                return True
        relative_to_project_root = path.relative_to(project_root)
        for pattern in project_root_relative_excludes:
            result = relative_to_project_root.match(pattern)
            if result:
                return True
        return False

    return sorted(set([str(p.relative_to(search_base))
                       for p in includes_iterator() if not exclusion(p)]))

#
# end glob_internal.py
#

#
# buck_parser/buck.py
#

def merge_maps(*header_maps):
    result = {}
    for header_map in header_maps:
        for key in header_map:
            if key in result and result[key] != header_map[key]:
                assert False, 'Conflicting header files in header search paths. ' + \
                              '"%s" maps to both "%s" and "%s".' \
                              % (key, result[key], header_map[key])

            result[key] = header_map[key]

    return result

def single_subdir_glob(dirpath, glob_pattern, excludes=None, prefix=None, build_env=None,
                       search_base=None, allow_safe_import=None):
    if excludes is None:
        excludes = []
    results = {}
    files = glob_internal([os.path.join(dirpath, glob_pattern)],
                 excludes=excludes,
                 project_root_relative_excludes=excludes,
                 include_dotfiles=False,
                 include_dotdotfiles=False,
                 search_base_path=search_base,
                 project_root=search_base)
    #print("pattern {}".format(os.path.join(dirpath, glob_pattern)))
    #print("search_base {}".format(search_base))
    #print("ssg files: {}".format(files))
    for f in files:
        if dirpath:
            key = f[len(dirpath) + 1:]
        else:
            key = f
        if prefix:
            # `f` is a string, but we need to create correct platform-specific Path.
            # This method is called by tests for both posix style paths and
            # windows style paths.
            # When running tests, search_base is always set
            # and happens to have the correct platform-specific Path type.
            cls = PurePath if not search_base else type(search_base)
            key = str(cls(prefix) + '/' + cls(key))
        results[key] = f

    return results


def subdir_glob(glob_specs, excludes=None, prefix=None, build_env=None, search_base=None,
                allow_safe_import=None):
    """
    Given a list of tuples, the form of (relative-sub-directory, glob-pattern),
    return a dict of sub-directory relative paths to full paths.  Useful for
    defining header maps for C/C++ libraries which should be relative the given
    sub-directory.

    If prefix is not None, prepends it it to each key in the dictionary.
    """
    if excludes is None:
        excludes = []

    results = []

    for dirpath, glob_pattern in glob_specs:
        results.append(
            single_subdir_glob(dirpath, glob_pattern, excludes, prefix, build_env, search_base,
                               allow_safe_import=allow_safe_import))

    return merge_maps(*results)
#
# end buck_parser/buck.py
#


class FindSrc(object):
    """Encapsulate state and processes associated with find source files."""

    ANKI_BUILD_PLATFORMS = ('android', 'ios', 'mac', 'linux', 'vicos', 'windows')
    ANKI_CXX_SRC_EXTS = ( '.c', '.cpp', '.cc' )
    ANKI_GO_SRC_EXTS = ( '.go', )
    ANKI_CXX_INCLUDE_EXTS = ( '.h', '.hpp', '.inl', '.def' )
    ANKI_PLATFORM_SRC_GLOBS = {
        'ios': [ '*.m', '*.mm' ],
        'mac': [ '*.m', '*.mm', '*_osx*' ]
    }

    def __init__(self, options = None):
        self.options = options

    def platform_src_globs(self, platform):
        if platform in self.ANKI_PLATFORM_SRC_GLOBS:
            return self.ANKI_PLATFORM_SRC_GLOBS[platform]
        else:
            return []

    def find(self):
        return self.find_src(self.options.search_base,
                             self.options.project_root,
                             self.options.includes,
                             self.options.excludes,
                             self.options.platforms)

    def find_src(self, search_base_path, project_root, includes, excludes, platforms):

        if not includes:
            includes = ["**/*"]

        include_globs = includes
        exclude_globs = excludes

        # exclude files for platforms that are not specified
        for p in self.ANKI_BUILD_PLATFORMS:
            if not p in platforms:
                exclude_globs.append("**/*_{}*".format(p))
                exclude_globs.extend(self.platform_src_globs(p))

        result = glob_internal(include_globs,
                               exclude_globs,
                               project_root_relative_excludes=exclude_globs,
                               include_dotfiles=False,
                               include_dotdotfiles=False,
                               search_base_path=search_base_path,
                               project_root=project_root)

        return result

# public functions

def asset_project(name, project_root, srcs, platform_srcs=[]):
    """Returns a map of key names to source files lists"""

    # asset project produce both input and output files
    asset_srcs = []
    asset_dsts = []
    if isinstance(srcs, dict):
        for (dst,src) in srcs.items():
            asset_srcs.append(src)
            asset_dsts.append(dst)
    else:
        asset_srcs = srcs
        asset_dsts = srcs

    file_map = {
            name + ".srcs.lst" : asset_srcs,
            name + ".dsts.lst" : asset_dsts
    }

    for entry in platform_srcs:
        regex = re.compile(entry[0])
        lst = entry[1]
        for p in FindSrc.ANKI_BUILD_PLATFORMS:
            if regex.match(p):
                p_srcs = []
                p_dsts = []
                if isinstance(lst, dict):
                    for (dst,src) in lst.items():
                        p_srcs.append(src)
                        p_dsts.append(dst)
                else:
                    p_srcs = lst
                    p_dsts = lst
                srcs_key = "{}_{}.srcs.lst".format(name, p)
                dsts_key = "{}_{}.dsts.lst".format(name, p)
                file_map[srcs_key] = p_srcs
                file_map[dsts_key] = p_dsts
                break

    return file_map

def cxx_project(name,
                project_root,
                srcs,
                platform_srcs=[],
                headers=[],
                platform_headers=[],
                data=[]):
    """Returns a map of key names to source file lists"""
    file_map = {
        name + ".srcs.lst" : srcs,
        name + ".headers.lst" : headers,
        name + ".data.lst" : data
    }

    for entry in platform_srcs:
        regex = re.compile(entry[0])
        lst = entry[1]
        for p in FindSrc.ANKI_BUILD_PLATFORMS:
            if regex.match(p):
                key = "{}_{}.srcs.lst".format(name, p)
                file_map[key] = lst
                break

    for entry in platform_headers:
        regex = re.compile(entry[0])
        lst = entry[1]
        for p in FindSrc.ANKI_BUILD_PLATFORMS:
            if regex.match(p):
                key = "{}_{}.headers.lst".format(name, p)
                file_map[key] = lst
                break

    return file_map

# Note: it is useful for the generic glob(), as used by the data member of a project, to allow
#       access outside of the source tree. Source files, by their nature, are in child folders
#       however the data that they access not necessarily so, therefore data will frequently
#       reference ../resources

def glob(search_base, includes, excludes=[]):
    result = glob_internal(includes,
                           excludes,
                           project_root_relative_excludes=excludes,
                           include_dotfiles=True,
                           include_dotdotfiles=True,
                           search_base_path=search_base,
                           project_root=search_base)
    return result


def cxx_glob(search_base, include_paths, include_exts=[""], includes=[], excludes=[], platform=None):
    """Returns a map of src lists based on includes, excludes by platform"""
    include_globs = []
    for p in include_paths:
        globs = ["{}/**/*{}".format(p, ext) for ext in include_exts]
        include_globs.extend(globs)

    include_globs.extend(includes)

    platform_list = platform
    if not platform_list:
        platform_list = []
    elif not isinstance(platform_list, list):
        platform_list = [platform_list]

    finder = FindSrc()
    files = finder.find_src(search_base,
                            search_base,
                            include_globs,
                            excludes,
                            platform_list)

    return files

def cxx_src_glob(search_base, include_paths, includes=[], excludes=[], platform=None):
    return cxx_glob(search_base,
                    include_paths,
                    FindSrc.ANKI_CXX_SRC_EXTS,
                    includes,
                    excludes,
                    [platform] if platform else [])

def cxx_header_glob(search_base, include_paths, includes=[], excludes=[], platform=None):
    return cxx_glob(search_base,
                    include_paths,
                    FindSrc.ANKI_CXX_INCLUDE_EXTS,
                    includes,
                    excludes,
                    [platform] if platform else [])

def all_glob(search_base, include_paths, includes=[], excludes=[], platform=None):
    exts = FindSrc.ANKI_CXX_INCLUDE_EXTS + FindSrc.ANKI_CXX_SRC_EXTS + FindSrc.ANKI_GO_SRC_EXTS
    return cxx_glob(search_base,
                    include_paths,
                    exts,
                    includes,
                    excludes,
                    [platform] if platform else [])

def go_project(name,
               search_base,
               dir):

    deps = go_deps('./' + os.path.join(search_base, dir))

    file_map = {
        name + ".srcs.lst" : deps,
    }

    return file_map

def go_pathfiles(name,
                 search_base,
                 dir):

    file_map = {
        name + ".godir.lst" : [search_base + '/' + dir]
    }

    return file_map

# helper function - use `go list` command to generate array of source files that the given package depends
# on, recursively
# if testonly == True, will only return array of test files in the given package (non-recursive)
def go_deps(pkg, testonly = False):
    import_dir = os.path.join("{{.Root}}", "src", "{{.ImportPath}}")
    file_string = " {{.GoFiles}} {{.CgoFiles}} {{.IgnoredGoFiles}} {{.HFiles}} {{.CFiles}} {{.CXXFiles}}" \
        if not testonly else " {{.TestGoFiles}} {{.XTestGoFiles}}"
    deps_str = "{{.Goroot}} " + import_dir + file_string
    pkg_args = ["go", "list", "-f", deps_str]
    if not testonly:
        pkg_args += ["-deps"]
    pkg_args += [pkg]

    pkg_deps = check_output(pkg_args).split('\n')

    # filter out standard library packages - first item will be true/false for whether
    # dep package is in standard library
    pkg_deps = [x.split(' ', 1) for x in pkg_deps]
    pkg_deps = [x[1] for x in pkg_deps if x[0] != "true"]

    # convert string that looks like [file1 file2 file3] to array of files, and prefix
    # with the given dir
    def get_sources(prefix, s):
        if prefix.startswith('/src/_/'):
            # lack of trailing slash compared to above (included there to be specific w/ matching)
            # is intentional
            prefix = prefix[len('/src/_'):]
        filenames = s.replace('[', '').replace(']', '').split()
        return [os.path.join(prefix, x) for x in filenames]

    # next token is the directory these files live in, followed by filename lists
    pkg_deps = [x.split(' ', 1) for x in pkg_deps]
    pkg_deps = [get_sources(x[0], x[1]) for x in pkg_deps]

    # pkg_deps is now an array of filename arrays - unify them into one
    pkg_deps = sum(pkg_deps, [])
    return pkg_deps

# given a directory, make a file map with dirname.gotestdir.lst, which contains list of all packages
# inside it that contain Go test files, and thus can run unit tests
def go_testdirs(dir, exclude):
    unslashed = dir.replace('/', '_')
    gopaths = os.environ['GOPATH'].split(':')
    gopath_src = os.path.join(gopaths[0], "src")
    search_base = os.path.join(gopath_src, dir)

    all_subdirs = check_output("find {} -mindepth 1 -type d".format(search_base).split(' ')).split('\n')
    # only include subdirs with go files
    def has_go_files(dir):
        contents = os.listdir(dir)
        return len([x for x in contents if x.endswith('.go')]) > 0
    all_subdirs = [x for x in all_subdirs if has_go_files(x)]
    # map full path subdirs to relative package paths
    all_packages = [os.path.relpath(x, gopath_src) for x in all_subdirs]
    def has_test_files(pkg):
        return check_output(["go", "list", "-f", "{{.TestGoFiles}} {{.XTestGoFiles}}", pkg]) != "[] []"
    test_packages = [x for x in all_packages if has_test_files(x) and x not in exclude]

    file_map = {
        unslashed + ".gotestdir.lst": test_packages
    }
    return file_map

# for each testable package in the above list: package.gotest.lst contains a list of all the source
# files that package (and its tests) depend on to build
def go_testdeps(dir, exclude):
    unslashed = dir.replace('/', '_')

    base_map = go_testdirs(dir, exclude)
    test_packages = list(base_map.items())[0][1]

    file_map = {}

    for pkg in test_packages:
        pkg_test = go_deps(pkg, True)
        pkg_deps = go_deps(pkg)
        deps = pkg_deps + pkg_test
        unslashed = pkg.replace('/', '_')
        file_map[unslashed + ".gotest.lst"] = deps

    return file_map

class BuildContext(object):
    def __init__(self):
        self.globals = {}
        self.includes = set()
        self.dirname = None


class BuildProcessor(object):

    def __init__(self):
        self.projects = {}
        self.build_env = BuildContext()

    def _asset_project(self, name, srcs, platform_srcs=[]):
        path = os.path.dirname(__file__)
        filemap = asset_project(name, path, srcs, platform_srcs)
        self.projects[name] = filemap

    def _cxx_project(self, name,
                srcs,
                platform_srcs=[],
                headers=[],
                platform_headers=[],
                data=[]):
        path = os.path.dirname(__file__)
        filemap = cxx_project(name, path, srcs, platform_srcs, headers, platform_headers, data)
        self.projects[name] = filemap

    def _go_project(self, name,
                dir):
        filemap = go_project(name, self.build_env.dirname, dir)
        self.projects[name] = filemap

    def _go_pathfiles(self, name,
                dir):
        filemap = go_pathfiles(name, self.build_env.dirname, dir)
        self.projects[name] = filemap

    def _go_testdirs(self, dir, exclude=[]):
        filemap = go_testdirs(dir, exclude)
        self.projects[dir] = filemap

    def _go_testdeps(self, dir, exclude=[]):
        filemap = go_testdeps(dir, exclude)
        self.projects[dir] = filemap

    def _cxx_src_glob(self, include_paths, includes=[], excludes=[], platform=None):
        return cxx_src_glob(self.build_env.dirname, include_paths, includes, excludes, platform)

    def _cxx_header_glob(self, include_paths, includes=[], excludes=[], platform=None):
        return cxx_header_glob(self.build_env.dirname, include_paths, includes, excludes, platform)

    def _glob(self, includes, excludes=[]):
        return glob(self.build_env.dirname, includes, excludes=[])

    def _subdir_glob(self, glob_specs, excludes=None, prefix=None, build_env=None, search_base=None,
                allow_safe_import=None):
        r = subdir_glob(glob_specs, excludes, prefix, build_env, self.build_env.dirname, allow_safe_import)
        return r

    def _include_defs(self, name):
        pass

    def _nofunc_stub(self, *args, **kwargs):
        return []

    def process_go_file(self, path):
        go_globals = {
            'include_defs': self._nofunc_stub,
            'cxx_src_glob': self._nofunc_stub,
            'cxx_header_glob': self._nofunc_stub,
            'cxx_project': self._nofunc_stub,
            'go_project': self._go_pathfiles,
            'go_testdir': self._go_testdirs,
            'asset_project': self._nofunc_stub,
            'glob': self._nofunc_stub,
            'subdir_glob': self._nofunc_stub,
        }
        return self._process_file_internal(path, go_globals)

    def process_build_file(self, path):
        normal_globals = {
            'include_defs': self._include_defs,
            'cxx_src_glob': self._cxx_src_glob,
            'cxx_header_glob': self._cxx_header_glob,
            'cxx_project': self._cxx_project,
            'go_project': self._go_project,
            'go_testdir': self._go_testdeps,
            'asset_project': self._asset_project,
            'glob': self._glob,
            'subdir_glob': self._subdir_glob,
        }
        return self._process_file_internal(path, normal_globals)

    def _process_file_internal(self, path, default_globals):
        with open(path, 'r') as f:
            contents = f.read()

        self.build_env.dirname = os.path.dirname(path)
        module = types.ModuleType(path)
        module.__file__ = path
        module.__dict__.update(default_globals)

        future_features = absolute_import.compiler_flag
        code = compile(contents, path, 'exec', future_features, 1)
        exec(code, module.__dict__)

        return module

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='metabuild.py source list generator')

    parser.add_argument('--output', '-o',
                        action='store',
                        required=True,
                        help="Output directory where source list files will be written")

    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        default=False,
                        help="Print verbose output")

    parser.add_argument('filelist',
                        action='store',
                        nargs='+',
                        help="List of BUILD.in files to process")

    parser.add_argument('--go-output', '-g',
                        action='store_true',
                        default=False,
                        help="Output Go files exclusively (otherwise no Go output)")

    options = parser.parse_args()

    processor = BuildProcessor()
    for build_file in options.filelist:
        if not options.go_output:
            mod = processor.process_build_file(build_file)
        else:
            mod = processor.process_go_file(build_file)

    output_dir = options.output
    ankibuild.util.File.mkdir_p(output_dir)
    for (name, project) in processor.projects.items():
        #print(project)
        if options.verbose:
            print("processing project: {}".format(name))

        for (lst_filename, files) in project.items():
            if options.verbose:
                print("  {} ({} files)".format(lst_filename, len(files)))

            lst_path = os.path.join(output_dir, lst_filename)
            if options.output != '-':
                with open(lst_path, 'w') as f:
                    f.write("\n".join(files))
                    f.flush()
            else:
                sys.stdout.write("\n".join(files))
                sys.stdout.write("\n")
                sys.stdout.flush()
