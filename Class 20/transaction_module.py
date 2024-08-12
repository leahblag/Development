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

    def __init__(self, owner: str, transactions: list, balance: float):
        self.owner = owner
        self.transactions = transactions
        self.balance = balance
