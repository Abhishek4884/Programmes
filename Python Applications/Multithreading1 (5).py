import threading

def Thread1(No):
    for i in range(1 , No+1):
        print(i)

def Thread2(No):
    for i in range( No,0 ,-1):
        print(i)


def main():
    print("Enter the number :")
    Num = int(input())
    p1 = threading.Thread(target=Thread1 , args=(Num ,))
    p2 = threading.Thread(target=Thread2 , args=(Num ,))
    print("_______________________")
    p1.start()
    p1.join()
    print("_______________________")
    p2.start()
    p2.join()
    print("_______________________")


if __name__=="__main__":
    main()