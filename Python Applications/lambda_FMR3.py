from functools import reduce


def main():
    print("how many elements you want to store :")
    isize = int(input())
    Data_Input = list()

    print("Enter the Values :")
    for i in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)
    print("Data is : " , Data_Input)

    Data_Filter = reduce(list(map(filter(lambda No :No%2==0,lambda No :No*2,lambda A,B : A+B, Data_Input))))
    print("Data after filter is : " , Data_Filter)

    # Data_map = list(map(lambda No :No*2, Data_Filter ))
    # print("data after map" , Data_map)

    # Data_reduce =(lambda A,B : A+B, )
    # print("Result after reduce " ,Data_Filter)


if __name__=="__main__":
    main()