class BankAccount:
    Bank_Name = "________________Welcome to the Bank of Maharashtra________________"
    ROI = 10.5
    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Accept()

    def Accept(self):
        print("Enter your Name :")
        self.Name = input()
        print(" your Initial Amount :")
        self.Amount = int(input())

    def Display(self):
        print("Your name as per Bank Account :" , self.Name)
        print("Your amount :" , self.Amount)

    def Deposite(self , Value):
        self.Amount = self.Amount + Value 

    def Withdraw(self , Value):
        self.Amount = self.Amount - Value

    def CalculateIntrest(self ):
        print("Enter for how many years you want to deposite ")
        self.no = int(input())
        print("You will earn  intrest after Five Year : " , ((self.Amount*BankAccount.ROI*self.no)/100))

def main():
    print(BankAccount.Bank_Name)
    print("_________Enter for User one________")

    User1 = BankAccount()
    print("_________Enter for User two________")
    User2 = BankAccount()
    User1.Display()
    print("-----------------------------")

    User2.Display()

    User1.Deposite(10000)
    User2.Deposite(10000)
    print("Amount of {}  After Depositing your amount will be {}".format(User1.Name , User1.Amount ))
    print("-----------------------------")

    print("Amount of {}  After Depositing your amount will be {}".format(User2.Name , User2.Amount ))
    print("-----------------------------")
    User1.Withdraw(5652)
    User2.Withdraw(7895)
    print("Amount of {}  After Withdrawing your amount will be {}".format(User1.Name , User1.Amount ))
    print("-----------------------------")

    print("Amount of {}  After Withdrawing your amount will be {}".format(User2.Name , User2.Amount ))
    print("For {}".format(User1.Name))
    User1.CalculateIntrest()
    print("For {}".format(User2.Name))
    User2.CalculateIntrest()
  

if __name__=="__main__":
    main()