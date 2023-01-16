from sys import *
import filecmp

def Chk_File(Path1 , Path2):
    Ans = filecmp.cmp(Path1 , Path2)
    return Ans



def main():

    print("________Welcome to Automation World________")
    if(len(argv) !=3):
        print("Error : Invalid numbers of argument ")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("Script will tell Two files are same or not")
        exit()

    if(argv[1]=="-u" or argv[1] =="-U"):
        print("Appliction name first file name second file name")
        exit()

    
    Result = Chk_File(Path1=argv[1] , Path2=argv[2])

    if(Result ==True):
        print("The files are same : {}".format(Result))
    else:
        print("The files are Not same : {}".format(Result))
if __name__ == "__main__":
    main()