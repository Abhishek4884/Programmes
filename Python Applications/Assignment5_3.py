class Arithmatic:
    def __init__(self):
        self.Value1 = 0 
        self.value2 = 0

    def Accept(self):
        print("Enter the First number :")
        self.Value1 = int(input())
        print("Enter the second number :")
        self.value2 = int(input())

    def Addition(self):
        Add = self.Value1 + self.value2
        return Add


    def Substraction(self):
        sub = self.Value1 - self.value2
        return sub


    def Multiplication(self):
        mult = self.Value1 * self.value2
        return mult


    def Division(self):
        div = self.Value1 / self.value2
        return div


def main():
    obj = Arithmatic()

    Ans = obj.Accept()

    Ans = obj.Addition()
    print("Addition of number : " , Ans)

    Ans = obj.Substraction()
    print("Substraction of numbers :" ,Ans)

    Ans = obj.Multiplication()
    print("Multiplication of numbers :" ,Ans)
    
    Ans = obj.Division()
    print("Division of numbers :" , Ans)

if __name__=="__main__":
    main()
