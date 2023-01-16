import threading 

def Even(No):
    for i in range(1 , No):
        if(i%2==0):
            print("Even Number :" , i)


def Odd(No):
    for i in range(1 , No):
        if(i%2!=0):
            print("Odd Number :" , i)


def main():
    number = 20
    p1 = threading.Thread(target =Even , args = (number ,))
    p2 = threading.Thread(target =Odd , args = (number ,))
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

    p2.start()
    p2.join()
    print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    p1.start()
    p1.join()


if __name__=="__main__":
    main()