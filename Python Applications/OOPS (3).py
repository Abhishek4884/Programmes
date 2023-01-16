class Numbers:
    welcome = "___________Welcome to Mathamatics Hub_______________"
    def __init__(self):
        self.No = 0
        self.Accept()

    def Accept(self):
        print("Enter the Number :")
        self.No=int(input())

    def ChkPrime(self):
        for i in range(2 , int(self.No/2)+1):
            if (self.No % i == 0):
                return False
            else:
                return True

    def ChkPerfect(self):
        Num = 0
        for i in range(1 , self.No):
            if (self.No % i == 0):
                Num = Num + i
        return Num

    def Factors(self):
        Num = []
        for i in range(1 , self.No):
            if (self.No % i == 0):
                Num.append(i)
        return Num

    def SumPerfect(self):
        Num = 0
        for i in range(1 , self.No):
            if (self.No % i == 0):
                Num = Num + i
        return Num

def main():
    obj = Numbers()

    print(Numbers.welcome)
    Ans = obj.ChkPrime()
    if (Ans == True):
        print("The Number {} is prime".format(obj.No))
    else:
        print("The Number {} is Not  prime".format(obj.No))
    print("-----------------------------")

    Ans = obj.Factors()
    print("The Factors of {} number is".format(obj.No) , Ans)
    print("-----------------------------")

    Ans = obj.SumPerfect()
    print("The Sum of Factors of {} is".format(obj.No) , Ans)
    print("-----------------------------")

    Ans = obj.ChkPerfect()
    if (Ans == obj.No):
        print("The Number {} is perfect".format(obj.No))
    else:
        print("The Number {} is Not perfect".format(obj.No))
    print("-----------------------------")

if __name__=="__main__":
    main()