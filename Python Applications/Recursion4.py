def Display(No):
    if(No > 0):
        print(No , end=" ")
        No = No -1
        Display(No)
        

def main():
    print("___This Application will display number in reverse order____")

    print("Enter the number :")
    Num = int(input())
    Display(Num)


if __name__=="__main__":
    main()