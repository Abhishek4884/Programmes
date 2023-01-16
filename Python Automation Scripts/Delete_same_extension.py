from sys import *
import os
import time

def Find_Ext(Path , Extension):
    listprocess = []
    exist = os.path.exists(Path)
    if exist:
    
        separator = "-"*80
        f = open("AbhishekLog.log" , 'w')
        f.write(separator + "\n")
        f.write("Find out all the smae extensions :" + time.ctime() + "\n")
        f.write(separator + "\n")

        for foldername,subfolder,filename in os.walk(Path):
            listprocess.append(foldername)
            for fname in filename:
                if fname.lower().endswith(Extension):
                    full_name = os.path.join(foldername,fname)
                    listprocess.append(full_name)
                    os.remove(full_name)

                

        for element in listprocess:
            f.write("%s\n"% element)

    else:
        print("Such path is not exist")



def main():

    if(len(argv)!=3):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-u" or argv[1] == "-U"):
        print("The Application is used for find out all same extensions")
        exit()


    if(argv[1] == "-h" or argv[1] == "-H"):
        print("Application name Directory extension")
        exit()

    Find_Ext(Path = argv[1] , Extension = argv[2])

if __name__ =="__main__":
    main()