from sys import *
from os import *

def Script_Task(no):
    if (no % 2) == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    print("Automation script started with name :" , argv[0])    

    if(len(argv) != 2):
        print("Error :")
        print("Use -h for help and use _u for usage of the script")
        exit()
    
    if ((argv[1] =="-h") or (argv[1] =="-H")):
        print("Help : This script is perform---------------")

    elif ((argv[1] =="-u") or (argv[1] =="-U")):
        print("usage : provide ______ number of argument as ")

        print("First Argument as : __________")
        print("Second Argument as : __________")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__=="__main__":
    main()