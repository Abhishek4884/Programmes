# Instance vairable : Name , Amount , Adress , Account_No
# Instance Method = CreatAccount()
import random
class Bank_Account:

    Bank_Name = "HDFC bank PVT LTD"   # Class Variable
    ROI_On_FD = 6.7                   # Class Variable

    def __init__(self):
        self.Name = ""                # Instance Variable
        self.Amount = 0
        self.Adress = ""
        self.Account_No = 0

    def CreatAccount(self):
        print("Enter your Name :")
        self.Name = input()

        print("Enter your intial Amount:")
        self.Amount = int(input())

        print("Enter your Adress:")
        self.Adress = input()

        # print("Enter your Account Number:")
        self.Account_No = random.randint(100 , 1000)

    def DisplayAccountInfo(self):
        print("____________Your Account Information is as below_______________")
        print("Name of Account Holder ==  " , self.Name)
        print()
        print(" Account Number == " , self.Account_No)
        print()
        print("Adress of Account Holder ==" , self.Adress)
        print()
        print("current Amount of Account Holder == " , self.Amount)

    @classmethod
    def DisplayBankInformation(cls):
        
        print("_____________Welcome to banking Console_______________ ")
        print()
        print("name of our Bank is :" , cls.Bank_Name)
        print("Rate Of Intrest we offer on fixed deposite :" , cls.ROI_On_FD)

    

    
def main():

    Bank_Account.DisplayBankInformation()
    user1 = Bank_Account()
    user2 = Bank_Account()

    print("*****Creating the First Account*****")
    user1.CreatAccount()
    print("*****Creating the First Account*****")
    user2.CreatAccount()

    user1.DisplayAccountInfo()
    user2.DisplayAccountInfo()


if __name__=="__main__":
    main()