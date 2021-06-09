def swapFileData():
    filename =  input("Enter the file name: ")
    file1 = 'file1.txt'
    file2 = 'file2.txt'

    data_a = ""
    data_b = ""

    with open(file1, 'r') as a:
        data_a = a.read()

    with open(file2, 'r') as a:
        data_b = a.read()

    with open(filename, 'w') as a:
        a.write(data_b)

swapFileData()