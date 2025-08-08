# Python Readme fixer

A tool which helps you fix malformatted markdown files.
What are these malformatted markdown files?
- Headers from level 1 to 4 where you forgot to place a space between the # symbol and the title. I know, this sounds stupid but I needed to use this not once..

## Usage

If you have a whole directory of markdown files:
Run: `fix_headers_in_recursive_directory(./path/to/files)`

If you have only one:
Run: `fix_headers_in_file(./path/to/file.md)`