from sys import * 

def Copy_File(Data1):
    try:
        fd = open(Data1 , "r")
        Text = fd.readlines()
        fd.close()

        fd1 = open("Demo.txt" , "a")
        for line in Text:
            fd1.write(line)
        fd1.close()
        print("Data copied Succesfully")
    except FileNotFoundError:
        print("File not found ")
        

def main():
    if(len(argv)!=2):
        print("Error : Invalid number of arguments ")
        exit()
    if(argv[1]=="-h" or argv[1]=="-H"):
        print("The Script is used to copy data from existing file to new file")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("usage : Application name fileName.extension")
        exit()

    Copy_File(argv[1])


if __name__ =="__main__":
    main()