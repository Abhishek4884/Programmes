import os
import multiprocessing

def Square(No):
    print("PID of worker process is {} for the input {}" .format(os.getpid() , No))
    return (No*No)

def main():
    print("Prosess ID of application" , os.getpid())
    Data = [1,2,3,4,5,6]
    Result = []
    
    pobj = multiprocessing.Pool()
    Result = pobj.map(Square , Data)


    print("result sfter Square " , Result )

if __name__=="__main__":
    main()