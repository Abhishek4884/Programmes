import os

def ReadFile(FileName):
    if (os.path.exists(FileName)):

        fd = open(FileName , "r")
        Data = fd.read()
        print(Data)

        fd.close()
    else:
        print("File is Not exist")
        return

    
def main():
    print("Enter the filr name ")
    Name =  input()
    ReadFile(Name)

if __name__=="__main__":
    main()