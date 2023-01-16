import os
from sys import *


def Directory_Watcher(Dir_Name):
    print("_________Inside Watcher method_________")
    print("Name of directory : ," , Dir_Name)
    
    for foldername,subfolder,filesname in os.walk(Dir_Name):
        print("Folder name :" + foldername)
        for subf in subfolder:
            print("subfolder name of "+ foldername +" is " + subf)
        for fname in filesname:
            print("File inside folder "+ foldername+" is "+fname)



def main():
    print("Directory Watcher Application")
    if (argv[1]=="-h"):
        print("This Script will travel the directory and display the names of all the entirs")
        exit()

    if (argv[1]=="-u"):
        print("Usage : Application name Directory_Name")
        exit()

    Directory_Watcher(argv[1])

if __name__=="__main__":
    main()