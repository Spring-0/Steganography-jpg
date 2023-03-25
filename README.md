# Steganography-jpg

This is a Python script that provides three functions to perform steganography on JPG files. It allows users to append, delete, and extract text or executables in a JPG file.

## Requirements
To run this script, you need to have Python and the following packages installed:

* `click`

You can intall them using the following command:
`pip install click`

## Usage
To use this script, run the following command:
`python script.py COMMAND [OPTIONS] [ARGS]`

The available commands are:
* `append`: Append data to a file.
* `delete`: Delete all written data from a file.
* `extract`: Extract written data from a file.

## Examples

### Append data to a file
`python main.py append -c "Hello, World!" targetfile.jpg`

### Delete data from a file
`python main.py delete targetfile.jpg`

### Extract data from a file
`python main.py extract targetfile.jpg`
