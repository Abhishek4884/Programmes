import os

def Chk_File(Data):
    if (os.path.exists(Data)):
        print("___File Exist___")
        return
    else:
        print("___File Not Exist_____")
        return


def main():
    print("Enter the File name")
    Name = input()
    Chk_File(Name)

if __name__=="__main__":
    main()