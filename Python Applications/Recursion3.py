def Display(No):

    if(No < 10):
        return No
    else:
        return ((No%10) + Display(int(No//10)))
    


def main():
    print("___This Application will display number in reverse order____")

    print("Enter the number :")
    Num = int(input())
    print("The sum of digits of number is " , Display(Num))


if __name__=="__main__":
    main()