# Python program to create a Bankaccount
# with deposit , withdraw and display.


class Bank_account:
    def __init__(self):
        self.balance = 0
        print("Welcome to Simple Bank.....")
    
    def deposit(self):

        #take the input from the user
        amount  =  float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print("\n the amount deposited:  ", amount )

    def withdraw(self):
        amount  =  float(input("Enter the amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -=amount
            print("\n You withdrew" , amount)
        else:
            print("\n Insufficient balance.....")   

    def display (self):
        print("\n Met available balance: " ,  self.balance) 


#create an user object
user  = Bank_account()
#calling different functions
user.deposit()
user.withdraw()
user.display()
        
