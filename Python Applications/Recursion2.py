def Display(No):
    if(No > 1):
        No = No -1
        Display(No)
        print(No , end=" ")



def main():
    print("___This Application will display number____")

    print("Enter the number :")
    Num = int(input())
    Display(Num)


if __name__=="__main__":
    main()