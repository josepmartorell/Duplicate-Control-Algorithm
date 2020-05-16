from os import strerror

head = 'file'
ext = str(input(
    '\nenter the report file extension to be created (txt, odt): '))
f = int(input(
    'enter the quantity of test files to be created:\n '))
test = 'file3' + '.' + ext
form = ['ID:',
        'Company:',
        'Address:',
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
        'Account:']

try:
    def generator(quantity):
        my_list = []
        i = 1
        while i <= quantity:
            my_list.append(head + str(i) + '.' + ext)
            i += 1
        return my_list

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