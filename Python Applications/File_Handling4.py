from sys import *

def Chk_Str(Path , Stringx):
    fd = open(Path , 'r')
    Text = fd.read()
    Result = Text.split()
    
    icnt = 0
    for i in Result:
        if(i == Stringx):
            
            icnt += 1
    return icnt

def main():
    if(len(argv) != 3):
        print("Error : Invalid number of arguments ")
        exit()

    if((argv[1]== "-h") or (argv[1]== "-H")):
        print("This script is used to record log process")
        exit()

    if((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage = Appliction Name Absolute path_of_Directory  string to check")
        exit()
    
    print(Chk_Str(Path = argv[1] , Stringx = argv[2]))


if __name__=="__main__":
    main()
