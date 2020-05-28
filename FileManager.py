import os
import hashlib
import utils
from os import strerror


class Main:

    def __init__(self, extension):

        self.extension = extension
        self.count = 0
        self.my_dict = {}
        self.the_file = ()
        self.hash = ''
        if self.extension != "":
            self.hash = ' sha256'
        else:
            self.hash = ' md5'

    def detect(self):
        try:
            # walk through de directories searching for extension's files
            for (dirname, dirs, files) in os.walk('../../Downloads/'):
                print('hashing files in', ''.join(dirname).strip('./'), 'dir ...\n')
                utils.progress()
                print("\t")
                for filename in files:
                    the_file = os.path.join(dirname, filename)
                    if self.extension == '':
                        h = hashlib.md5()
                    else:
                        h = hashlib.sha256()
                    with open(the_file, 'rb') as afile:
                        buf = afile.read()
                        h.update(buf)
                    thehash = h.hexdigest()

                    # in case of duplication fill the tuple of de dict or else a simple value

                    if filename.endswith(self.extension):
                        if thehash in self.my_dict:
                            self.my_dict[thehash] += (the_file,)
                        else:
                            self.my_dict[thehash] = (the_file,)

            check = utils.is_empty(self.my_dict)

            if check is not True:
                # print hashes and values
                for key in self.my_dict.keys():
                    snap = ' '.join(self.my_dict[key]).lstrip('./Downloads')
                    print('File: ', snap)
                    print('Hash: ', key, self.hash)
            else:
                print('there are no files with the ' + utils.ext + ' extension')

        except IOError as e:
            print("I/O error occurred: ", strerror(e.errno))


if __name__ == '__main__':
    obj = Main(utils.ext)
    obj.detect()
    utils.unzip()
    utils.remove()
