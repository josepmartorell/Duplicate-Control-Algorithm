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
