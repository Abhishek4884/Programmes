import os

def WriteFile(FileName):
    if (os.path.exists(FileName)):
        print("Enter the data you want to write")
        Data = input()
        fd = open(FileName , "a")
        fd.write(Data)
    else:
        print("File is Not exist")
        return

    
def main():
    print("Enter the filr name to create")
    Name =  input()
    WriteFile(Name)

if __name__=="__main__":
    main()