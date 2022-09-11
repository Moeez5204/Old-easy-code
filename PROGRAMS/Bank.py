class bankaccount():
    def __init__(self,owner='Mr.qURESHI',balance=5000):
        self.owner = owner
        self.__balance = balance

    def balanceSetter(self,balance,amount):
        if amount > balance or amount < 0 :
            print('error')
        else:
            balance -= amount
            print('new balance :',balance)

    def deposit(self,balance,amount):
        Balance = balanceGetter(self)
        Balance += amount
        print('new balance :',balance)

    

def balanceGetter(self):
        print(self.__balance)
account = bankaccount('MR.Qureshi',5000)
true =1 
while true == 1:
    print('1.Check account balance')
    print('2.Withdraw Funds')
    print('3.deposit Funds')
    Input = int(input())
    if Input == 1:
        balanceGetter(account)
    elif Input == 2:
        amount = int(input('How much would you like to withdraw?'))
        account.balanceSetter(account,balanceGetter(account),amount)
    elif Input == 3:
        amount = int(input('How much would you like to deposit?'))
        deposit(account,balanceGetter(account),amount)
    else:
        print('error')

    
        
