import os

def CreateFile(FileName):
    if (os.path.exists(FileName)):
        print("File is already exist")
        return
    else:
        f = open(FileName ,"w")

    
def main():
    print("Enter the filr name to create")
    Name =  input()
    CreateFile(Name)

if __name__=="__main__":
    main()