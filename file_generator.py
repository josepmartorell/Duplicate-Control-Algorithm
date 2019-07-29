from os import strerror

head = 'file'
ext = str(input(
    'enter the extension file to be created (txt, odt): '))
f = int(input(
    'enter the quantity of files to be created: '))
test = 'file3' + '.' + ext
form = ['ID:',
        'Company:',
        'Geolocation:',
        'Category:',
        'Staff:',
        'Business:',
        'Seniority:',
        'References:',
        'Channels:',
        'Appointment:',
        'Interview:',
        'Tracer:',
        'Closing:',
        'IBAN:']


try:
    def generator(quantity):
        my_list = []
        i = 1
        while i <= quantity:
            my_list.append(head + str(i) + '.' + ext)
            i += 1
        return my_list

    # print the sequence
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
    

try:
    foo = open(test ,'wt')

    for i in range(14):
        foo.write(form[i] + "\n\n")
    foo.close()

except IOError as e:

    print("I/O error oc curred: ", strerror(e.errno))