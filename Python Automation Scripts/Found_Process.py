from sys import *
import os
import time
import psutil

def Process_Display(log_dir , processname):
    if not os.path.isdir(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    listprocess = []
    Samelist = []
    seprator = "-"*50
    log_path = os.path.join(log_dir , "AbhishekLog%s.log"%time.time())
    fd = open(log_path , 'w')
    fd.write(seprator + '\n')
    fd.write("Abhishek Automation : process logger at %s"%time.ctime() + "\n")
    fd.write(seprator + '\n')
    log_path2 = os.path.join(log_dir , "Abhishek_Process%s.log"%time.time())
    f = open(log_path2 , 'w')
    f.write(seprator + '\n')
    f.write("Abhishek Automation : process logger at %s"%time.ctime() + "\n")
    f.write(seprator + '\n')


    for proc in psutil.process_iter():
        try:            
            info = proc.as_dict(attrs = ['pid' ,'name' ,'username'])            
            listprocess.append(info)
            if processname.lower() in info['name'].lower():
                Samelist.append(info)
        
        
        except (psutil.NoSuchProcess ,psutil.ZombieProcess , psutil.AccessDenied) as E:
            print(E)

    for element in listprocess:
        fd.write("\n%s"%element)

    for element in Samelist:
        f.write("\n%s"%element)
        if (len(Samelist) == 0):
            f.write("No Such process Found............")  

def main():
    if(len(argv) !=3):
        print("Error : Invalid arguments")
        exit()
    
    if(argv[1] =="-h" or argv[1]=="-H"):
        print("The Script is used to print all the current running process in laptop and also create new log file and you can save any perticular process ")
        exit()


    if(argv[1] =="-u" or argv[1]=="-U"):
        print("Usage = Application name  ")
        exit()
        
    try:
        Process_Display(log_dir = argv[1] , processname= argv[2])
    except Exception as E:
        print(E)


if __name__=="__main__":
    main()