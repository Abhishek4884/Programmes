def DisplayEven(No):
    for i in range(No):
        if(i%2==0):
            print("Even number :" , i)

def DisplayOdd(No):
    for i in range(No):
        if(i%2!=0):
            print("Odd number :" , i)




def main():
    DisplayEven(2000000)
    DisplayOdd(2000000)

if __name__== "__main__":
    main()