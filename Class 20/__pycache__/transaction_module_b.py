import datetime
from datetime import datetime

''' Bank Account Class Requirements

Attributes:

owner: a string representing the name of the account owner
balance: a float representing the current balance of the account
transactions: a list representing the history of transactions made on the account

Methods:

deposit(amount, date): adds the specified amount to the account's balance and records the transaction in the transactions list

withdraw(amount): subtracts the specified amount from the account's balance (if there are sufficient funds) and records the transaction in the transactions list

__str__(): returns a string representation of the bank account. What information do you want to display in this string? What might be okay to leave out? How do you want to format it?

get_balance(): returns the current balance of the account

get_transactions(): returns a list of all the transactions made on the account

get_transaction_count(): returns the total number of transactions made on the account

get_transaction_history(): returns a string representation of the transaction history, including the type (deposit or withdrawal) and amount for each transaction

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
    ''' This docstring will show all the documentation for the class'''
    
    # Your init, your constructor, builds the object
    def __init__(self, owner: str, transactions: list, balance: float):
        self.owner = owner # Tara Jones
        self.transactions = transactions
        self.balance = balance
    
    # Controls what the user sees when they use print
    def __str__(self):
        return f'Acct owner Name: {self.owner}\nInitial Deposit: {self.balance}'
    
    '''deposit(amount, date): adds the specified amount to the account's balance and records the transaction in the transactions list'''
    def deposit(self, dep_amt, date):
        dep_tran = {'type':'deposit', 'amount':dep_amt, 'transaction date': date}
        self.transactions.append(dep_tran)

    
    ''' withdraw(amount): subtracts the specified amount from the account's balance (if there are sufficient funds) and records the transaction in the transactions list Lets check for all deposit amounts'''
    def withdrawal(self, withd_amt, date):
        sufficient_funds = self.balance - withd_amt
        if sufficient_funds < 0:
            print(f'Transaction cancelled, Insufficient balance {sufficient_funds}')
        else:
            withd_tran = {'type': 'withdrawal', 'amount':withd_amt, 'transaction date':date}
            self.transactions.append(withd_tran)
            print(self.transactions)
    
    ''' get_balance(): returns the current balance of the account WE NEED TO FIX THIS'''
    def get_balance(self):
        tot_dep = 0
        tot_with = 0
        for t in self.transactions:
            if t['type'] == 'deposit':
                tot_dep += t['amount']
            if t['type'] == 'withdrawal':
                tot_with -= t['amount']
        print(f'Your balance is {(self.balance + tot_dep) + tot_with}')
    
    def get_transactions(self):
        print(f'{self.transactions}')



    '''get_transaction_count(): returns the total number of transactions made on the account'''


    '''get_transaction_history(): returns a string representation of the transaction history, including the type (deposit or withdrawal) and amount for each transaction this should be in ascending chronolical order'''


    
        

    