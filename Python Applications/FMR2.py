def main():
    print("how many elements you want to store :")
    isize = int(input())
    Data_Input = list()

    print("Enter the Values :")
    for i in range(0,isize,1):
        Value = int(input())
        Data_Input.append(Value)
    print(Data_Input)


if __name__=="__main__":
    main()