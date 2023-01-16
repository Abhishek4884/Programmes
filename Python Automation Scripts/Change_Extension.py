import os
import time
from sys import *

def Directory_Rename(Path , Extension1 ,Extension2):
    listprocess = []
    
    exist = os.path.exists(Path)
    if exist:

        
        separator = "-"*80
        f = open("AbhishekLog.txt", 'w')
        f.write(separator + "\n")
        f.write("Find out all the smae extensions :" + time.ctime() + "\n")
        f.write(separator + "\n")

        for foldername,subfolder,filename in os.walk(Path):
            for fname in filename:
                if fname.lower().endswith(Extension1):
                    try:
                        listprocess.append(fname)
                        fname = os.path.join(foldername , fname)

                        new_Ext = fname.replace(Extension1 , Extension2)
                        os.rename(fname,new_Ext)


                    except FileExistsError:
                        print("File {} already exit".format(new_Ext))
        
        for element in listprocess:
            f.write("%s\n"%element)

       

    else:
        print("Such path is bot exist_______")
    print("Sucess")

def main():
    if(len(argv)!=4):
        print("Error : Invalid arguments")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print("The script will channge file extension")
        exit()

    
    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Application name Directory_Name Extention_1 Extention_2")
        exit()

    Directory_Rename(Path = argv[1] , Extension1 = argv[2] , Extension2 = argv[3])


if __name__=="__main__":
    main()