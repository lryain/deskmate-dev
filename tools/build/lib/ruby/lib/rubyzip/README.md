# rubyzip
[![Build Status](https://secure.travis-ci.org/rubyzip/rubyzip.png)](http://travis-ci.org/rubyzip/rubyzip)
[![Code Climate](https://codeclimate.com/github/rubyzip/rubyzip.png)](https://codeclimate.com/github/rubyzip/rubyzip)
[![Coverage Status](https://coveralls.io/repos/rubyzip/rubyzip/badge.png?branch=master)](https://coveralls.io/r/rubyzip/rubyzip?branch=master)

rubyzip is a ruby library for reading and writing zip files.

## Important note

Rubyzip interface changed!!! No need to do `require "zip/zip"` and `Zip` prefix in class names removed.

If you have issues with any third-party gems what required old version of rubyzip you can use next workaround:

```ruby
gem 'rubyzip', '>= 1.0.0' # will load new rubyzip version
gem 'zip-zip' # will load compatibility for old rubyzip API.
```

## Requirements

* Ruby 1.9.2 or greater

## Installation
rubyzip is available on RubyGems, so:

```
gem install rubyzip
```

Or in your Gemfile:

```ruby
gem 'rubyzip'
```

## Usage

### Basic zip archive creation

```ruby
require 'rubygems'
require 'zip'

folder = "Users/me/Desktop/stuff_to_zip"
input_filenames = ['image.jpg', 'description.txt', 'stats.csv']

zipfile_name = "/Users/me/Desktop/archive.zip"

Zip::File.open(zipfile_name, Zip::File::CREATE) do |zipfile|
  input_filenames.each do |filename|
    # Two arguments:
    # - The name of the file as it will appear in the archive
    # - The original file, including the path to find it
    zipfile.add(filename, folder + '/' + filename)
  end
  zipfile.get_output_stream("myFile") { |os| os.write "myFile contains just this" }
end
```

### Zipping a directory recursively

```ruby
require 'rubygems'
require 'zip'

directory = '/Users/me/Desktop/directory_to_zip/'
zipfile_name = '/Users/me/Desktop/recursive_directory.zip'

Zip::File.open(zipfile_name, Zip::File::CREATE) do |zipfile|
	Dir[File.join(directory, '**', '**')].each do |file|
	  zipfile.add(file.sub(directory, ''), file)
	end
end
```

### Save zip archive entries in sorted by name state

To saving zip archives in sorted order like below you need to set `::Zip.sort_entries` to `true`

```
Vegetable/
Vegetable/bean
Vegetable/carrot
Vegetable/celery
fruit/
fruit/apple
fruit/kiwi
fruit/mango
fruit/orange
```

After this entries in zip archive will be saved in ordered state.

### Reading a Zip file

```ruby
Zip::File.open('foo.zip') do |zip_file|
  # Handle entries one by one
  zip_file.each do |entry|
    # Extract to file/directory/symlink
    puts "Extracting #{entry.name}"
    entry.extract(dest_file)

    # Read into memory
    content = entry.get_input_stream.read
  end

  # Find specific entry
  entry = zip_file.glob('*.csv').first
  puts entry.get_input_stream.read
end
```

## Known issues

### Modify docx file with rubyzip

Use `write_buffer` instead `open`. Thanks to @jondruse

```ruby
buffer = Zip::OutputStream.write_buffer do |out|
  @zip_file.entries.each do |e|
    unless [DOCUMENT_FILE_PATH, RELS_FILE_PATH].include?(e.name)
      out.put_next_entry(e.name)
      out.write e.get_input_stream.read
     end
  end

  out.put_next_entry(DOCUMENT_FILE_PATH)
  out.write xml_doc.to_xml(:indent => 0).gsub("\n","")

  out.put_next_entry(RELS_FILE_PATH)
  out.write rels.to_xml(:indent => 0).gsub("\n","")
end

File.open(new_path, "w") {|f| f.write(buffer.string) }
```

## Configuration

By default, rubyzip will not overwrite files if they already exist inside of the extracted path.  To change this behavior, you may specify a configuration option like so:

```ruby
Zip.on_exists_proc = true
```

If you're using rubyzip with rails, consider placing this snippet of code in an initializer file such as `config/initializers/rubyzip.rb`

Additionally, if you want to configure rubyzip to overwrite existing files while creating a .zip file, you can do so with the following:

```ruby
Zip.continue_on_exists_proc = true
```

If you want to store non english names and want to open properly file on Windows(pre 7) you need to set next option:

```ruby
Zip.unicode_names = true
```

You can set the default compression level like so:

```ruby
Zip.default_compression = Zlib::DEFAULT_COMPRESSION
```

It defaults to `Zlib::DEFAULT_COMPRESSION`. Possible values are `Zlib::BEST_COMPRESSION`, `Zlib::DEFAULT_COMPRESSION` and `Zlib::NO_COMPRESSION`

All settings in same time

```ruby
  Zip.setup do |c|
    c.on_exists_proc = true
    c.continue_on_exists_proc = true
    c.unicode_names = true
    c.default_compression = Zlib::BEST_COMPRESSION
  end
```

By default Zip64 support is disabled for writing. To enable it do next:

```ruby
Zip.write_zip64_support = true
```

_NOTE_: If you will enable Zip64 writing then you will need zip extractor with Zip64 support to extract archive.

## Developing

To run tests you need run next commands:

```
bundle install
rake
```

## Website and Project Home

http://github.com/rubyzip/rubyzip

http://rdoc.info/github/rubyzip/rubyzip/master/frames

## Authors

Alexander Simonov ( alex at simonov.me)

Alan Harper ( alan at aussiegeek.net)

Thomas Sondergaard (thomas at sondergaard.cc)

Technorama Ltd. (oss-ruby-zip at technorama.net)

extra-field support contributed by Tatsuki Sugiura (sugi at nemui.org)

## License

rubyzip is distributed under the same license as ruby. See
http://www.ruby-lang.org/en/LICENSE.txt
