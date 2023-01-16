
Mult_Function = lambda A,B :A*B

def main():
    print("Enter the First number :")
    Num1 = int(input())
    
    print("Enter the Second number :")
    Num2 = int(input())

    Ans = Mult_Function(Num1,Num2)
    print("The multiplication of numbers is :" , Ans)

if __name__=="__main__":
    main()
