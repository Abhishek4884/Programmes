import threading

def Even_List(Data):
    Even = 0
    for i in Data:
        if(i%2==0):
            Even = Even + i
    print("The Addition of all Even Numbers are :" , Even)


def Odd_List(Data):
    Odd = 0
    for i in Data:
        if(i%2!=0):
            Odd = Odd + i
    print("The Addition of all Odd Numbers are :" , Odd)

def main():
    print("Enter the value you want to store :")
    Size = int(input())
    Arr = list()
    print("Enter the values : ")

    for i in range(0 , Size):
        Value = int(input())
        Arr.append(Value)
    print(Arr)
    P1 = threading.Thread(target = Even_List , args = (Arr , ))
    P1.start()
    P1.join()

    P2 = threading.Thread(target = Odd_List , args = (Arr , ))
    P2.start()
    P2.join()


if  __name__=="__main__":
    main()
