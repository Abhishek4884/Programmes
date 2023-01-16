def main():
    try:
        print("Enter the First number")
        No1 = int(input())

        print("Enter the Second number")
        No2 = int(input())
        Ans = No1 / No2
        print("Division is : " , Ans)

    except ZeroDivisionError:
        print("Exception Occured")

    except NameError:
        print("Inside Name Error")

    except ValueError:
        print("Inside value ERROR")

    finally:
        print("Finally")

if __name__=="__main__":
    main()

