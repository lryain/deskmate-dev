#!/usr/bin/env python2

# Author: Jordan Rivas
# Date:   3/27/17
#
# Description: This script uses 'SoundbanksInfo.json' metadata generated by Wwise Generate Soundbanks script to identify
#              all assets associated with each soundbank. The soundbank.bnk and all of it's lose files are packaged
#              together into a zip file. All of the files in the zip file dates are replace with a static time to allow
#              RAMS to identify what assets have changed and need to be uploaded to the endpoint.


import argparse
import json
import logging
import ntpath
import os
import posixpath
import sys
import textwrap
import zipfile


#set up default logger
Logger = logging.getLogger('bundle_soundbank_products')
stdout_handler = logging.StreamHandler()
formatter = logging.Formatter('%(name)s - %(message)s')
stdout_handler.setFormatter(formatter)
Logger.addHandler(stdout_handler)
# Bundle info meta data file name
json_bundle_file = 'SoundbankBundleInfo.json'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class SoundbankBundle:

    # Wwise generated metadata JSON Doc Keys
    NAME_KEY = 'ShortName'
    PATH_KEY = 'Path'
    LANGUAGE_KEY = 'Language'
    STREAMED_FILES_KEY = 'ReferencedStreamedFiles'
    ID_KEY = 'Id'

    def __init__(self, json_data):
        self.name = ''
        self.path = ''
        self.language = ''
        self.streamed_files = []
        self.read_json(json_data)

    def get_posix_path(self):
        return self.path.replace(ntpath.sep, posixpath.sep)


    def read_json(self, json_data):
        self.name = json_data[self.NAME_KEY]
        self.path = json_data[self.PATH_KEY].replace(ntpath.sep, os.sep)
        self.language = json_data[self.LANGUAGE_KEY]

        # Get all reserved files
        if self.STREAMED_FILES_KEY in json_data:

            for a_file_obj in json_data[self.STREAMED_FILES_KEY]:
                if self.ID_KEY in a_file_obj:
                    self.streamed_files.append(a_file_obj[self.ID_KEY])
                else:
                    logging.error('Id not found in Streamed File Object')

    def generate_object(self):

        BUNDLE_NAME_KEY = 'bundle_name'
        SOUNDBANK_NAME_KEY = 'soundbank_name'
        PATH_KEY = 'path'
        LANGUAGE_KEY = 'language'

        object_model = {}
        object_model[BUNDLE_NAME_KEY] = self.create_filename()
        object_model[SOUNDBANK_NAME_KEY] = self.name
        object_model[PATH_KEY] = self.get_posix_path()
        object_model[LANGUAGE_KEY] = self.language

        return object_model;


    def create_filename(self, extension=''):
        # Create filename
        filename = self.name
        if self.language != 'SFX':
            filename += '_' + self.language
        if len(extension) > 0:
            filename += '.' + extension
        return filename


    def description(self):
        return 'Name:\'{0}\' - Path:\'{1}\' - Lang:\'{2}\' - StreamedFileCount: {3}'.format(self.name,
                                                                                            self.path,
                                                                                            self.language,
                                                                                            len(self.streamed_files))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class AssetInfo:

    def __init__(self, name, org_path, sub_path = ''):
        self.name = name
        self.org_path = org_path
        self.sub_path = sub_path


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
WWISE_SOUNDBANK_INFO_KEY = 'SoundBanksInfo'
WWISE_SOUNDBANK_KEY = 'SoundBanks'
WWISE_STREAMED_FILES_KEY = 'StreamedFiles'


def read_soundbank_info_json(filePath):

    bundles = []

    with open(filePath) as json_file:
        jsonData = json.load(json_file)

        for a_soundbank in jsonData[WWISE_SOUNDBANK_INFO_KEY][WWISE_SOUNDBANK_KEY]:
            a_bundle = SoundbankBundle(a_soundbank)
            bundles.append(a_bundle)
            Logger.debug('{0}'.format(a_bundle.description()))

    return  bundles

def prune_missing_soundbank_bundles(soundbank_bundles, source_path):
    # Create paths
    valid_bundles = []
    for a_bundle in soundbank_bundles:
        bank_file_path = os.path.join(source_path, a_bundle.path)
        if os.path.exists(bank_file_path):
            valid_bundles.append(a_bundle)
            Logger.debug('\'{0}\' soundbank exists'.format(a_bundle.name))
        else:
            Logger.warning('\'{0}\' soundbank does NOT exists at path: \'{1}\''.format(a_bundle.name, bank_file_path))

    return valid_bundles


# Find all files for a soundbank bundle and add them to in_out_asset_list
# Return False if the bank's .bnk file is not found
# Return False if the soundbank_bundle lose file is not found and allow_missing_files is False
def find_soundbank_files(soundbank_bundle, source_path, in_out_asset_list, allow_missing_files = False):
    # Find all assets for bundle

    # Create paths
    sub_path, bundle_file_name = os.path.split(soundbank_bundle.path)
    bank_file_path = os.path.join(source_path, sub_path)

    # Check soundbank exists
    if not os.path.exists(os.path.join(bank_file_path, bundle_file_name)):
        Logger.warning('Soundbank: \'{0}\' file does NOT exist'.format(bundle_file_name))
        return False

    lang_dest_path = ''
    is_lang_path = False
    if len(sub_path) > 0:
        is_lang_path = True
        lang_dest_path = sub_path

    Logger.debug('\'{0}\' Soundbank subpath: \'{1}\''.format(soundbank_bundle.name, lang_dest_path))

    # Add sound bank file
    in_out_asset_list.append(AssetInfo(bundle_file_name, bank_file_path, lang_dest_path))

    # Find .wem files
    for a_wem_file in soundbank_bundle.streamed_files:
        file_name = a_wem_file + '.wem'
        org_file_path = ''
        dest_file_path = ''

        found_file = False
        if is_lang_path:
            # Check if files exist in lang dir
            possible_path = os.path.join(source_path, sub_path)
            if os.path.exists(os.path.join(possible_path, file_name)):
                org_file_path = possible_path
                dest_file_path = sub_path
                found_file = True

        if not found_file:
            # Check Root Directory
            if os.path.exists(os.path.join(source_path, file_name)):
                org_file_path = source_path
                found_file = True

        # Check if file was found
        if found_file:
            in_out_asset_list.append(AssetInfo(file_name, org_file_path, dest_file_path))

        else:
            Logger.error('Soundbank Bundle \'{0}_{1}\' File NOT found \'{2}\''.format(soundbank_bundle.name,
                                                                                      soundbank_bundle.language,
                                                                                      file_name))
            if not allow_missing_files:
                return False;

    return True


def bundle_soundbank_files(soundbank_bundles, source_path, destination_path, allow_missing_files=False):

    for a_bundle in soundbank_bundles:

        # Find all assets for bundle
        bundle_assets = []

        success = find_soundbank_files(a_bundle, source_path, bundle_assets, allow_missing_files)
        if not success and not allow_missing_files:
            Logger.error('\'{0}\' asset NOT found'.format(a_bundle.name))
            return False

        # Check if there are assets
        if len(bundle_assets) > 0:
            # Write zip file
            zip_sound_bundle(a_bundle, bundle_assets, destination_path)
        else:
            # Will only hit case if allow_missing_files is True and no assets are found soundbank_bundle
            Logger.warning('No assets found for {0}'.format(a_bundle.name))

    return True


def get_bytes_from_file(filename):
    return open(filename, "rb").read()


def zip_sound_bundle(soundbank_bundle, bundle_assets, dest_path):
    # Create Zip filename
    zip_path = os.path.join(dest_path, soundbank_bundle.create_filename('zip'))

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_STORED) as outfile:
        for a_file in bundle_assets:
            org_file_path = os.path.join(a_file.org_path, a_file.name)
            bytes_from_file = get_bytes_from_file(org_file_path)
            filename = os.path.join('', a_file.sub_path, a_file.name)
            zi = zipfile.ZipInfo()
            zi.filename = filename.replace(ntpath.sep, posixpath.sep)
            zi.date_time = (2032, 11, 11, 13, 50, 2)  # Spell out Anki in date/time fields ;)
            # Add an extra field for the extended date time stamp.  Allows us to set a more
            # recent and reasonable date/time if we want to extract these files from the .zip.
            # Still be cute and spell out "Wwise_SB" in the file. ;)
            zi.extra = ''.join(chr(x) for x in [0x55, 0x54,     # UT
                                                0x09, 0x00,     # (TAB) (NULL)
                                                0x03,           # (ETX)
                                                0x57, 0x77, 0x69, 0x73, 0x65, 0x5f, 0x53, 0x42]) # Wwise_SB

            zi.compress_type = zipfile.ZIP_STORED
            outfile.writestr(zi, bytes_from_file, zipfile.ZIP_STORED)


def create_soundbank_bundle_info_file(soundbank_bundles, dest_file_path):
    json_data = []

    for aBundle in soundbank_bundles:
        json_data.append(aBundle.generate_object())

    with open(dest_file_path, 'w') as json_file:
        json.dump(json_data, json_file, sort_keys=True, ensure_ascii=False)


def generate_log(soundbank_bundles, source_meta_filepath, output_dir):

    asset_map = {}
    json_data = {}
    # Log file keys
    LOG_NAME_KEY = 'name'
    LOG_ID_KEY = 'id'
    LOG_SOUNDBANK_KEY = 'soundbank'
    LOG_SOUNDBANK_LOCALE_KEY = "soundbankLocale"
    # Wwise meta data key
    WWISE_ID_KEY = 'Id'
    WWISE_SHORT_NAME_KEY = 'ShortName'

    # Copy Wwise generated metadata
    with open(source_meta_filepath) as json_file:
        json_data = json.load(json_file)

    # Find what soundbanks references streaming assets
    soundbanks_meta = json_data[WWISE_SOUNDBANK_INFO_KEY][WWISE_STREAMED_FILES_KEY]
    for a_file in soundbanks_meta:
        asset_id = a_file['Id']

        for a_bundle in soundbank_bundles:
            # Search if asset_id is in bundle
            if asset_id in a_bundle.streamed_files:

                if not asset_id in asset_map:
                    # Add object to log
                    obj = {}
                    split_res = a_file[WWISE_SHORT_NAME_KEY].split('\\')
                    obj[LOG_NAME_KEY] = split_res[-1]
                    obj[LOG_ID_KEY] = a_file[WWISE_ID_KEY]
                    obj[LOG_SOUNDBANK_KEY] = [a_bundle.name]
                    obj[LOG_SOUNDBANK_LOCALE_KEY] = [a_bundle.create_filename()]
                    asset_map[asset_id] = obj
                else:
                    # Add more bank data log object
                    obj = asset_map[asset_id]
                    obj[LOG_SOUNDBANK_LOCALE_KEY].append(a_bundle.create_filename())
                    if not a_bundle.name in obj[LOG_SOUNDBANK_KEY]:
                        obj[LOG_SOUNDBANK_KEY].append(a_bundle.name)


    # Sort list by greatest number of soundbanks then by name of asset
    sorted_vals = sorted(asset_map.values(),
                         key=lambda  elem: "%02d %s" % ((len(elem[LOG_SOUNDBANK_KEY])-100), elem[LOG_NAME_KEY]) )

    # Write log file
    file_path_2 = os.path.join(output_dir, 'FileLog.json')
    with open(file_path_2, 'w') as json_file:
        json.dump(sorted_vals, json_file, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': '))


def parse_args(argv=[], print_usage=False):
    version = '1.0'
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='zip sound files on a per soundbank basis',
        epilog=textwrap.dedent('''
          options description:
            [path/to/sounds] [path/for/output]
      '''),
        version=version
    )

    parser.add_argument('--debug', '-d', '--verbose', dest='debug', action='store_true',
                        help='Print debug output')
    parser.add_argument('--allow-missing', dest='allow_missing', action='store_true',
                        help='Do not quit for a missing file')
    parser.add_argument('--meta-only', dest='meta_only', action='store_true',
                        help='Only generate the {0} metadata file'.format(json_bundle_file))
    parser.add_argument('--create-log', dest='create_log', action='store_true',
                        help='Generate a log file to show what soundbanks an audio assets is in')
    parser.add_argument('sound_dir', action='store',
                        help='Path to sound directory for a platform')
    parser.add_argument('output_dir', action='store',
                        help='Directory to store output in')

    if print_usage:
        parser.print_help()
        sys.exit(2)

    args = parser.parse_args(argv)

    if (args.debug):
        Logger.setLevel(logging.DEBUG)
        Logger.debug(args)
    else:
        Logger.setLevel(logging.INFO)

    return args


def run(args):
    sound_dir = args.sound_dir
    output_dir = args.output_dir
    json_file = 'SoundbanksInfo.json'

    # Check argument paths
    # Input Dir
    if not os.path.exists(sound_dir):
        Logger.error('sound_dir \'{0}\' does NOT exist'.format(sound_dir))
        return 2

    # Wwise generated metadata file
    wwise_meta_file_path = os.path.join(sound_dir, json_file)
    if not os.path.exists(wwise_meta_file_path):
        Logger.error('\'{0}\' does NOT exist in \'{1}\''.format(json_file, sound_dir))
        return 2

    # Output Dir
    if not os.path.exists(output_dir):
        Logger.error('output_dir \'{0}\' does NOT exist'.format(output_dir))
        return 2

    # Read generated metadata to create bundle objects
    bundles = read_soundbank_info_json(wwise_meta_file_path)
    # Remove bundles that can't be found
    bundles = prune_missing_soundbank_bundles(bundles, sound_dir)
    # Create Soundbank Bundle Info file for app
    bundle_info_file_path = os.path.join(output_dir, json_bundle_file)
    create_soundbank_bundle_info_file(bundles, bundle_info_file_path)

    if not args.meta_only:
        # Create zip files for bundle files
        success = bundle_soundbank_files(bundles, sound_dir, output_dir, args.allow_missing)
        if not success:
            return 2

    if args.create_log:
        # Create log file
        generate_log(bundles, wwise_meta_file_path, output_dir)

    # Success!
    return 0


def main(args):
    parsed_args = parse_args(args)
    return run(parsed_args)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))