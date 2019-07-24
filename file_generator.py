from os import strerror

head = 'file'
ext = '.txt'
f = int(input("enter the quantity of files to be created: "))

try:
    def generator(quantity):
        mylist = []
        i = 1
        while i <= quantity:
            mylist.append(head + str(i) + ext)
            i += 1
        return mylist


    # print the secuence
    for j in generator(f):
        print(j)

    # print the list itself
    print(generator(f))

    # create a list to be accessed
    mylist2 = list(generator(f))

    # generate the files
    for i in range(f):
        fo = open(mylist2[i], 'wt')
    fo.close()

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))