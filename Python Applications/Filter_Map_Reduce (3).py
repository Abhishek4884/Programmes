def Sortx(no):
    return (70<=no<=90)

def Increment(no):
    return(no +10)

def Product(A,B):
    return(A*B)

def FilterX(Data , Function):
    Result = []
    for no in Data:
        if (Function(no)):
            Result.append(no)
    return Result

def MapX(Data , Function):
    Result = []
    for no in Data:
        Value = Function(no)
        Result.append(Value)
    return Result


def ResduceX(Data ,Function):
    num = 1
    for no in Data:
        num = Function(num,no)
    return(num)

def main():
    print("Enter the value you want to store :")
    Size = int(input())
    Arr = list()
    print("Enter the numbers :")
    for i in range(0 ,Size):
        Value = int(input())
        Arr.append(Value)
    print("User Defined List :" , Arr)

    Data_Filter = FilterX(Arr , Sortx)
    print("Data after Filter : " , Data_Filter)
    
    Data_Mapx = MapX(Data_Filter , Increment)
    print("Data after Mapping : " , Data_Mapx)
    
    Data_ReduceX = ResduceX(Data_Mapx , Product)
    print("The Final answer is : " , Data_ReduceX)


if __name__=="__main__":
    main()
