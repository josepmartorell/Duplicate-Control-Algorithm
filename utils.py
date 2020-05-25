import time
import sys
import zipfile
from past.builtins import xrange
import os
import glob

ext = str(input('\nSwitch manager run mode:'
                '\n\tTARGET EXTENSION FILE ......... type specific extension (zip, xlsx, odt, txt..) + enter'
                "\n\tTARGET ALL FILES .............. just press enter\n"))


def is_empty(data_structure):
    if data_structure:
        print("not empty!")
        return False
    else:
        print("empty!")
        return True


def progress():
    toolbar_width = 40

    # setup toolbar
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width + 1))  # return to start of line, after '['

    for i in xrange(toolbar_width):
        time.sleep(0.1)  # do real work here
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("\n")


def unzip(path):
    zip = str(input('\nSwitch manager run execution:'
                    '\n\tUNPACK ZIP FILES .............. type (zip) + enter'
                    "\n\tSKIP........................... just press enter\n"))
    if zip == 'zip':
        print('unpacking zip files ...\n')
        progress()
        files = os.listdir(path)
        for file in files:
            if file.endswith('.zip'):
                file_path = path + '/' + file
                zip_file = zipfile.ZipFile(file_path)
                for names in zip_file.namelist():
                    zip_file.extract(names, path)
                zip_file.close()
        print('\ndone!')
    else:
        print('\nzip packages not found ...')


def remove():
    rem = str(input('\nSwitch manager run execution:'
                    '\n\tREMOVE ALL FILES .............. type (rem) + enter'
                    "\n\tSKIP........................... just press enter\n"))
    if rem == 'rem':
        files = glob.glob('../../Downloads/*')
        for f in files:
            os.remove(f)
