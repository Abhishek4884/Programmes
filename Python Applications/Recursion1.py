def Display(No):
    if(No > 0):
        No = No-1
        Display(No)
        print("*" , end = " ")
        

def main():
    print("___This Application will display *")
    print("Enter the number :")
    Num = int(input())
    Display(Num)

if __name__=="__main__":
    main()