class Demo:
    def __init__(self ,A,B):
        self.No1 = A
        self.No2 = B
    
    def fun(self):
        return self.No1 , self.No2

    def gun(self):
        return self.No1 , self.No2

def main():

    
    obj1 = Demo(11 , 21)
    obj2 = Demo(51, 101)

    Ans = obj1.fun()
    print(Ans)
    Ans = obj2.fun()
    print(Ans)
    Ans = obj1.gun()
    print(Ans)
    Ans = obj2.gun()
    print(Ans)

if __name__=="__main__":
    main()