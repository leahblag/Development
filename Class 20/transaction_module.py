import datetime
from datetime import datetime

''' Bank Account Class Requirements

Attributes:

owner: a string representing the name of the account owner
balance: a float representing the current balance of the account
transactions: a list representing the history of transactions made on the account

Methods:

1.) deposit(amount): adds the specified amount to the account's balance and records the transaction in the transactions list

2.) withdraw(amount): subtracts the specified amount from the account's balance (if there are sufficient funds) and records the transaction in the transactions list

3.) __str__(): returns a string representation of the bank account. What information do you want to display in this string? What might be okay to leave out? How do you want to format it?

4.) get_balance(): returns the current balance of the account

5.) get_transactions(): returns a list of all the transactions made on the account

6.) get_transaction_count(): returns the total number of transactions made on the account

7.) get_transaction_history(): returns a string representation of the transaction history, including the type (deposit or withdrawal) and amount for each transaction

Let's expand our BankAccount class so each transaction has a date. Make sure to keep track of transactions in chronological order.

When we make classes in Python, each class should be its own Python file.
The Python file is considered a module.
If you write code in a different file that uses the class, you must import the class.
Let's say your class is called BankAccount, your class is in the file module.py, and your code using your class is in the same folder.
To import the entire module, use this line of code:
import module
To import just the class, use this line of code:
from module import BankAccount

'''

class BankAccount():
# THIS DOCSTRING WILL SHOW ALL OF THE DOCUMENTATION FOR THE CLASS - BankAccount

# YOUR INIT, AKA INSTRUCTOR, BUILDS THE OBJECT
    def __init__(self, owner: str, transactions: list, balance: float):
        self.owner = owner
        self.transactions = transactions
        self.balance = balance

# CONTROLS WHAT THE USER SEES WHEN THEY USE PRINT
    def __str__(self):
        return f'Account Owners Name: {self.owner}\nInitial Deposit: {self.balance}'

# DEPOSIT(AMOUNT, DATE): ADDS THE SPECIFIED AMOUNT TO THE ACCOUNT'S BALANCE AND RECORDS THE TRANSACTION IN THE TRANSACTION LIST
    def deposit(self, dep_amt, date):
        dep_tran = {'type':'deposit', 'amount':dep_amt, 'transaction date': date}
        self.transactions.append(dep_tran)
        print(self.transactions)

# WITHDRAW(AMOUNT): SUBTRACTS THE SPECIFIED AMOUNT FROM THE ACCOUNT'S BALANCE (IF THERE ARE SUFFICIENT FUNDS) & RECORDS THE TRANSACTION IN THE TRANSACTION LIST
def withdrawl(self, withd_amt, date):
        sufficient_funds = self.balance - withd_amt
        if sufficient_funds < 0:
            print(f'Transaction cancelled, Insufficient balance {sufficient_funds}')
        else:
             withd_tran = {'type': 'withdrawal', 'amount':withd_amt, 'transaction date':date}
             self.transactions.append(withd_tran)
             print(self.transactions)

# RETURNS THE CURRENT BALANCE OF THE ACCOUNT - get_balance(): 
def get_balance(self):
     tot_dep = 0
     tot_with = 0
     for t in self.transactions:
          if t['type'] == 'deposit':
               tot_dep += t['amount']
          if t ['type'] == 'withdrawal':
               tot_with -= t['amount']
     print(f'Your balance is {(self.balance + tot_dep) + tot_with}')       


def get_transactions(self):
     print(f'{self.transactions}')

               
                  
