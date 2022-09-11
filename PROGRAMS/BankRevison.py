class bankAccount():
    '''This is a bank account class'''
    def __init__(self, account_name = "Bank Account", balance = 1500):
        self.__account_name = account_name
        self.__balance = balance

    def deposit(self, value):
        self.__balance = self.__balance + value
        print("You now have: ", self.__balance)

    def withdraw(self, value):
        self.__balance = self.__balance - value
        print("You now have: ", self.__balance)

class currentAccount(bankAccount):
    '''This is a current account class'''
    def __init__(self, account_name = "Current Account", balance = 1500):
        self.__account_name = account_name
        self.__balance = balance
        super().__init__()

    def withdraw(self, value):
        if value > 1000:
            print("You will have to phone the bank manager")
        else:
            self.__balance = self.__balance - value
            print("You now have: ", self.__balance)

class savingsAccount(bankAccount):
    '''This is a current account class'''
    def __init__(self, account_name = "Savings Account", balance = 1500):
        self.__account_name = account_name
        self.__balance = balance
        super().__init__()

    def deposit(self, value):
        self.__balance = self.__balance + (value *1.03)
        print("You now have: ", self.__balance)



currentObject = currentAccount()
savingsObject = savingsAccount()

while True:

    print("1. Current Account")
    print("2. Savings Account")
    menu_option = int(input())

    if menu_option == 1:
        print("1. Deposit funds")
        print("2. Withdraw funds")
        submenu_option = int(input())

        if submenu_option == 1:
            value = int(input("How much would you like to desposit? "))
            currentObject.deposit(value)
        elif submenu_option == 2:
            value = int(input("How much would you like to withdraw? "))
            currentObject.withdraw(value)
        else:
            print("Wrong menu choice!")
    elif menu_option == 2:
        print("1. Deposit funds")
        print("2. Withdraw funds")
        submenu_option = int(input())

        if submenu_option == 1:
            value = int(input("How much would you like to desposit? "))
            savingsObject.deposit(value)
        elif submenu_option == 2:
            value = int(input("How much would you like to withdraw? "))
            savingsObject.withdraw(value)
        else:
            print("Wrong menu choice!")
    else:
        print("Wrong menu choice!")
input()

