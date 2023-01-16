import os

def Open_File(Data):
    if (os.path.exists(Data)):
        fd = open(Data , "r")
        DataX = fd.read()
        print(DataX)
        fd.close()
    else:
        print("File does not exist")
        return

def main():
    print("Enter the file name :")
    Name = input()
    Open_File(Name)


if __name__=="__main__":
    main()