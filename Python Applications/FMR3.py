def CheckEven(No):
    return (No % 2 ==0)

def double(no):
    return(no*2)

def Sum(A,B):
    return (A+B)

def FilterX(Helper_Function , Data):
    Result = []
    for no in Data:
        if (Helper_Function(no)==True):
            Result.append(no)
    return Result
    
def Mapx(Helper_Function , Data):
    Resultx = []
    for no in Data:
        value = Helper_Function(no)
        Resultx.append(value)
    return Resultx

def Reduce(Helper_Function , Data):
    Ans  = 0
    for no in Data:
        Ans = Helper_Function(Ans , no)
    return(Ans)

def main():
    print("how many elements you want to store :")
    isize = int(input())
    Data_Input = list()

    print("Enter the Values :")
    for i in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is : " , Data_Input)
    Data_Filter = FilterX(CheckEven , Data_Input)
    print("Data after filter is : " , Data_Filter)
    Data_map = Mapx(double , Data_Filter )
    print("data after map" , Data_map)
    Data_reduce = Reduce(Sum , Data_map)
    print("Result after reduce " , Data_reduce)


if __name__=="__main__":
    main()