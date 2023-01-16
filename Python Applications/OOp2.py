class Numbers:
    def __init__(self):
        self.size = 0
        self.Arr = list()
        self.Accept()

    def Accept(self):
        print("Enter how many elements you want :")
        self.size = int(input())
        print('Enter the values :')
        value = 0
        for i in range (0 , self.size):
            value = int(input())
            self.Arr.append(value)


    def Addition(self ):
        Num = 0
        for i in range(0 , self.size):
            Num = Num + self.Arr[i]
        return Num

    def Average(self ):
        Num = 0
        for i in range(0 , self.size):
            Num = Num + self.Arr[i]
        return (Num/self.size)

    def Maximum(self ):
        Max = self.Arr[0]
        for i in range(0 , self.size):
            if(self.Arr[i] > Max):
                Max = self.Arr[i]
        return (Max)

    
    def Minimum(self ):
        Max = self.Arr[0]
        for i in range(0 , self.size):
            if(self.Arr[i] < Max):
                Max = self.Arr[i]
        return (Max)


    def Display(self):
        print("List is = " , self.Arr)

def main():
    obj = Numbers()
    obj.Display()
    Ans = obj.Addition()
    print("Addiition of numbers in list is :" ,Ans)
    Ans = obj.Average()
    print("Average of numbers in list is :" ,Ans)
    Ans = obj.Maximum()
    print("Maximum of numbers in list is :" ,Ans)
    Ans = obj.Minimum()
    print("Minimum of numbers in list is :" ,Ans)

if __name__=="__main__":
    main()