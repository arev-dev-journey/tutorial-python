'''
Create a bank account class with two attributes and two methods and
display the attributes and call the methods
'''
class Account:
    ''' Account class with two methods and two attributes'''
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: ${self.balance}'

    def deposit(self,dep_amt):
        ''' Deposit amount to balance '''
        self.balance += dep_amt
        print(f"{self.balance} funds available")

    def withdraw(self,wd_amt):
        ''' Withdraw amount from balance '''
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f"{self.balance} funds available")
        else:
            print("Funds Unavailable!")

# 1. Instantiate the class

acct1 = Account("Alex",3500)

# 2. Print the object
print(acct1)

# 3. Show the owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the account balance
acct1.withdraw(5000)
