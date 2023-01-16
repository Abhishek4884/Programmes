
class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0

    def Accept(self):
        print("Enter the number :")
        self.Radius = int(input())

    
    def CalculateArea(self):
        Area = Circle.PI*self.Radius*self.Radius
        return Area

    def CalculateCircumferance(self):
        Circumferance = 2*Circle.PI*self.Radius
        return Circumferance

    def Display(self):
        return Circle.PI , self.Radius
        

def main():
    obj = Circle()
    obj.Accept()
    Ans = obj.CalculateArea()
    print("Area of Circle is :" , Ans)

    Ans = obj.CalculateCircumferance()
    print("Circumferance of Circle is :" , Ans)
    
    Ans = obj.Display()
    print(Ans)


if __name__=="__main__":
    main()