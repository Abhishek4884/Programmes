import os

def DeleteFile(FileName):
    if (os.path.exists(FileName)):
        size = os.path.getsize(FileName)
        if(size == 0):
            os.remove(FileName)
        else:
            print("You want to sure to delete this file : Y/N" )
            option = input()
            if(option == "Y" or option == "y"):
                os.remove(FileName)
    else:
        print("There is  No exist")
        return

    
def main():
    print("Enter the file name to delete ")
    Name =  input()
    DeleteFile(Name)

if __name__=="__main__":
    main()