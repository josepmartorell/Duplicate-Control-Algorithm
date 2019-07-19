#!/usr/bin/python3.7
#! -*- coding: utf-8 -*-

import os
import hashlib

class main:

    def __init__(self, extension):

        self.extension = extension
        self.count = 0
        self.mydict = {}
        self.thefile = ()


    def detect(self):

        # walk throught de directories serching for extension's files

        for (dirname, dirs, files) in os.walk('.'):
            for filename in files:
                thefile = os.path.join(dirname, filename)
                hasher = hashlib.md5()
                with open(thefile, 'rb') as afile:
                    buf = afile.read()
                    hasher.update(buf)
                thehash = hasher.hexdigest()

                # in case of txt extension fill the tuple of de dict or else a simple value

                if filename.endswith(self.extension):
                    if thehash in self.mydict:
                        self.mydict[thehash] += (thefile,)
                    else:
                        self.mydict[thehash] = (thefile,)

        # print hashes and values
        for key in self.mydict.keys():
            print('Hash: ', key)
            print('File: ', self.mydict[key])


ext = '.txt'
obj = main(ext)
obj.detect()
