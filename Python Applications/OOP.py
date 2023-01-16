class Arithmatic:
    def __init__(self , A , B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Add(self):
        Ans = self.No1 + self.No2
        return  Ans

    
    def Sub(self):
        Ans = self.No1 - self.No2
        return  Ans
    
def main():

    obj = Arithmatic(11,10)
    objX = Arithmatic(21,10)

    Ans = obj.Add()
    print("Addition is  :" , Ans)
    Ans = obj.Sub()
    print("Substraction is :" , Ans)

    Ans = objX.Add()
    print("Addition is  :" , Ans)
    Ans = objX.Sub()
    print("Substraction is :" , Ans)
    print("Inside main Method")


if __name__=="__main__":
    print("Inside Starter")
    main()