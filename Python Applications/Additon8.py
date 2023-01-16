print("Application to demonstrate industrial programme")

import MarvellousModule

def main():
    print("value of __name__ from main is :", __name__)
    print("Enter First number : ")
    no1 = int(input())
    print("Enter Second number : ")
    no2 = int(input())

    sum = MarvellousModule.Addition(no1,no2)
  
    print("Addition is : " , sum)

if __name__ == "__main__":
    main()


