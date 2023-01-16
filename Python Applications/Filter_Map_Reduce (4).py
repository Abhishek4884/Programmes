
def ChkEven(No):
    if(No%2==0):
        return(No)
    else:
        return 0

def Square(no):
    return(no*no)

def Add(A,B):
    return(A+B)


def FilterX(Data , Function):
    Result =[]
    for no in Data:
        Value = Function(no)
        Result.append(Value)
    return Result


def MapX(Data , Function):
    Result = []
    for no in Data:
        value = Function(no)
        Result.append(value)
    return Result


def ReduceX(Data , Function):
    num = 0
    for no in Data:
        num = Function(num , no)
    return num

def main():
    print("Enter the value you want to store :")
    Size = int(input())
    Arr = list()
    print("Enter the values :")
    for i in range(0,Size):
        value = int(input())
        Arr.append(value)
    print("User Defined List :" , Arr)

    Data_FilterX = FilterX(Arr , ChkEven)
    print("Filtered Data :" , Data_FilterX)

    Data_MapX = MapX( Data_FilterX, Square)
    print("Mapping Data :" , Data_MapX)

    Data_ReduceX = ReduceX(Data_MapX  , Add)
    print("Final output :" , Data_ReduceX)



if __name__=="__main__":
    main()