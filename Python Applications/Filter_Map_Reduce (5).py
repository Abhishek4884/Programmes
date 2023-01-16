def Multiply(No):
    return(No*2)


def ReduceX(Data):
    MaxX = 0
    for no in Data:
        if MaxX < no:
            MaxX = no
    return MaxX  


def FilterX(Data):
    Result = []
    for i in Data:
        for j in range(2 , int(i)):
            if i % j == 0:
                break
        else:
            Result.append(i)
    return Result

def MapX(Data , Function):
    Result = []
    for no in Data:
        value = Function(no)
        Result.append(value)
    return(Result)


def main():
    print("Enter the value you want to store :")
    Size = int(input())
    Arr = list()
    print("Enter the Values :")
    for i  in range(0,Size):
        Value = int(input())
        Arr.append(Value)
    print("User input list :" , Arr)

    Data_FilterX = FilterX(Arr)
    print("Data After Filter :" , Data_FilterX)

    Data_MapX = MapX( Data_FilterX , Multiply)
    print("Data After Map :" , Data_MapX)

    Data_ReduceX = ReduceX( Data_MapX  )
    print(" After Reduce :" , Data_ReduceX)


if __name__=="__main__":
    main()