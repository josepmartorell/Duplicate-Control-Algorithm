# Duplicate-Control-Algorithm

The duplicate control algorithm detects identical files within the same 
selected extension and directory to quantify duplicate files and eliminate 
them if necessary.

# Table of Contents

- Usage
- Features
- License


# How to Install

First you must access from your terminal to the directory where you want to save the project. Install this project on your local computer by typing the following in the command prompt of the linux command interpreter:
git clone https://github.com/josepmartorell/Duplicate-Control-Algorithm.git

# Usage

To run the script you should first access the src folder and type this line in the interpreter's order indicator to run the script:
username@hostname:~/PycharmProjects/project_foulder$ python3 file_duplicate_detector.py

# Features

- The script ask for the type or extension (recommended txt or odt for this example)
- Ask for the quantity of files (recommended set 4 files)
- Automatically generates the files
- Automatically create a form in the third file to test the duplicator function
- Displays both an iteration and a list of the created files
- Show hashes with attachments (notice that the third file has a different hash)

# License

MIT License

Copyright (c) 2019 Josep Martorell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.