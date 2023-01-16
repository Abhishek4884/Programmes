from sys import *
import os
import shutil

def Directory_Copy(Path , Copy_path , Extenstion):
    
    if not os.path.exists(Copy_path):
        try:
            os.mkdir(Copy_path)
        except:
            pass

    exist = os.path.exists(Path)
    if exist:
        for foldername,subfolder,filename in os.walk(Path):
            for fname in filename:
                if fname.lower().endswith(Extenstion):
                    try:    
                        full_name = os.path.join(Path , fname)
                        shutil.copy(full_name , Copy_path)
                        
                    except FileExistsError:
                        print("File {} already exit".format(fname))

        print("Successfully copied............")
    else:
        print("Path not exist")




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

    Directory_Copy(Path = argv[1] , Copy_path= argv[2] , Extenstion = argv[3])

if __name__=="__main__":
    main()