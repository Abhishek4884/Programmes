import os
import time
from sys import *

def Folder_Watcher(log_dir , Dir_Name):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-"*80
    log_path = os.path.join(log_dir ,"AbhishekLog.log")
    f = open(log_path , 'w')
    f.write(separator + "\n")
    f.write("Total Folders And files in this Directory :" + time.ctime() + "\n")
    f.write(separator + "\n")

    for foldername,subfolder,filesname in os.walk(Dir_Name):
        listprocess.append("Main Folder Name :"+foldername )
        for subf in subfolder:
            listprocess.append("The sub folder in that main folder :"+subf)
        for fname in filesname:
            listprocess.append("Files in that folder :"+fname)

    for element in listprocess:
        f.write("%s\n"% element)




def main():
    print("Application name  ; " + argv[0])

    if(len(argv) != 3):
        print("Error : Invalid number of arguments ")
        exit()

    if((argv[1]== "-h") or (argv[1]== "-H")):
        print("This script is used to record log process")
        exit()

    if((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage = Appliction Name Name of Directory  Absolute path_of_Directory")
        exit()

    try:
        Folder_Watcher(log_dir= argv[1] , Dir_Name=argv[2])
    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception:
        print("Error : Invalid input")
    finally:
        print("Sucessful")

if __name__=="__main__":
    main()