#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import hashlib
import file_report_generator


class Main:

    def __init__(self, extension):

        self.extension = extension
        self.count = 0
        self.my_dict = {}
        self.the_file = ()

    def detect(self):

        # walk through de directories searching for extension's files

        for (dirname, dirs, files) in os.walk('.'):
            for filename in files:
                the_file = os.path.join(dirname, filename)
                h = hashlib.md5()
                with open(the_file, 'rb') as afile:
                    buf = afile.read()
                    h.update(buf)
                thehash = h.hexdigest()

                # in case of txt extension fill the tuple of de dict or else a simple value

                if filename.endswith(self.extension):
                    if thehash in self.my_dict:
                        self.my_dict[thehash] += (the_file,)
                    else:
                        self.my_dict[thehash] = (the_file,)

        # print hashes and values
        for key in self.my_dict.keys():
            print('Hash: ', key)
            snap = ' '.join(self.my_dict[key]).strip('./')
            print('File: ', snap)


if __name__ == '__main__':
    obj = Main(file_report_generator.ext)
    obj.detect()
