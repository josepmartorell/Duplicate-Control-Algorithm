#!/usr/bin/python3.7
#! -*- coding: utf-8 -*-

import os
from os.path import join
import hashlib

count = 0
mydict = {}
thefile = ()
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
        if filename.endswith('.txt'):
            if thehash in mydict:
                mydict[thehash] += (thefile,)
            else:
                mydict[thehash] = (thefile,)

# print hashes and values
for key in mydict.keys():
    print('Hash: ', key)
    print('File: ', mydict[key])
    # if duplicated or more
    if len(mydict[key]) > 1:
        length = len(mydict[key])
        # we go through the tuple and print the repeated files but the first one
        for i in range(length):
            if i >= 1:
                print(mydict[key][i])
