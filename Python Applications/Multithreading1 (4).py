import threading
import os

def Small(Data):
    res = ""
    for i in Data:
        if  i.islower()== True:
            res = res +" "+ i
    print("Thread ID id of Small is :", threading.get_ident())
    print("The name of thread is :" , threading.current_thread())
    return print("Smaller case in the String :" ,res )
    
def Capital(Data):
    res = ""
    for i in Data:
        if  i.isupper()== True:
            res = res +" "+ i
    print("Thread ID id of Capital is :", threading.get_ident())
    print("The name of thread is :" , threading.current_thread())
    return print("Uppercase in the string :" ,res)
            

def Digits(Data):
    res = []
    for i in Data:
        if  i.isdigit()== True:
            res.append(i)
    print("Thread ID id of Digits is :", threading.get_ident())
    print("The name of thread is :" , threading.current_thread())
    return print("Digits in the string :" ,res)  

def main():
    print("Enter the String :")
    Line = input()
    p1 = threading.Thread(target = Small , args=(Line ,))
    p2 = threading.Thread(target = Capital , args=(Line ,))
    p3 = threading.Thread(target = Digits , args=(Line ,))
    print("______________________________")
    p2.start()
    p2.join()
    print("______________________________")
    p1.start()
    p1.join()
    print("______________________________")
    p3.start()
    p3.join()
    print("______________________________")

if __name__=="__main__":
    main()