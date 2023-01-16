import os
import psutil
from sys import *
import time


def ProcessDisplay(log_dir):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-"*80
    log_path = os.path.join(log_dir ,'AbhishekLog{}.log'.format(time.time()))
    f = open(log_path , 'w')
    f.write(separator + "\n")

    f.write("Abhishek Process logger :" + time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid' , 'name', 'username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n"% element)
    
    print("File generated Sucessfully_________")







def main():
    print("Application name  ; " + argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments ")
        exit()

    if((argv[1]== "-h") or (argv[1]== "-H")):
        print("This script is used to record log process")
        exit()

    if((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage = Appliction Name Absolute path_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
       
    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception as E:
        print(E)


if __name__ =="__main__":
    main()