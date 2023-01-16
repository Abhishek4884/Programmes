import threading

def Even_Factor(No):
    Even = 0
    Result = []
    for i in range(1 , No+1):
        if (No % i == 0) & (i % 2 ==0) :
            Result.append(i)
            Even = Even + i
    print("The Even Factors are" , Result, " & The summation Even of factors are",Even)

def Odd_Factor(No):
    Odd = 0
    Result = []
    for i in range(1 , No+1):
        if (No % i == 0) & (i % 2 !=0) :
            Result.append(i)
            Odd = Odd + i
    print("The Odd Factors are" , Result, " & The summation of Odd factors are",Odd)

 
def main():
    print("Enter the number :")
    Num = int(input())

    P1 = threading.Thread(target = Even_Factor , args = (Num ,))
    P2 = threading.Thread(target = Odd_Factor , args = (Num ,))

    P1.start()
    P1.join()

    P2.start()
    P2.join()
    

if __name__=="__main__":
    main()