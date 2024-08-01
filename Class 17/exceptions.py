import math


''' Functions pt 2 completed '''

# Lambda with sort

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]

students_by_name = sorted(students, key= lambda s: s['name'], reverse=True)
# print(students_by_name)

students_by_age = sorted( students, key= lambda s: s['grade'])
# print(students_by_age)

# Let's look at reduce
from functools import reduce


my_list = [1, 2, 3, 4, 5]
lets_try_reduce = reduce(lambda a, b: a * b, my_list)
# print(lets_try_reduce)



''' More fun with functions'''


''' 
Write a lambda function that makes a string a title case and apply the function to the list below with a map function
words = ['make', 'us', 'title', 'case']

'''
words = ['make', 'us', 'title', 'case']

result = map(lambda w : w.title(), words)
# print(list(result))



''' Write a lambda function that will add ten to a list item if that list item is greater than or equal to 50, otherwise it will subtract five

my_numbers = [50, 12, 19, 80, 5, 75]
'''

my_numbers = [50, 12, 19, 80, 5, 75]

def add_if(n):
    if n>= 50:
        return n + 10
    else:
        return n - 5
    
# print(add_if(50))

math = list(map(lambda x: x+10 if x>=50 else x-5, my_numbers))
# print(math)




''' Write a lambda function and utilize reduce to add all the numbers in this list

add_me_up = [50, 12, 9, 100, 56, 70]
'''
from functools import reduce

add_me_up = [50, 12, 9, 100, 56, 70]

# Use reduce with a lambda function to sum the numbers
total = reduce(lambda x, y: x + y, add_me_up)

# print(total)



''' Compile time errors / static errors'''
# SyntaxError: unterminated string literal 
# print('Wed) 

# SyntaxError: unterminated string literal
# name = 'John  

# SyntaxError: '(' was never closed
# print("I hope you have a great day" 

# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# if x = 10: 

# SyntaxError: expected ':'
# if x == 10 


''' Exceptions / Runtime errors'''

''' ValueError '''
# ValueError: could not convert string to float: 'testing'
# print(float("testing")) 

# ValueError: math domain error
# print(math.sqrt(-5)) 

# ValueError: not enough values to unpack (expected 3, got 2)
# fname, lname, middlename = 'fritz', 'lewis' 

''' AttributeError '''
# AttributeError: 'int' object has no attribute 'append'
# num = 10
# num.append(5) 


# AttributeError: 'str' object has no attribute 'append'
# str1 = 'hello'
# str1.append('buddy')  

''' NameError '''
# NameError: name 'x' is not defined
# print(x) 

# Name error: name 'c' is not define
# for i in range(c): 
#     print(i)  

''' TypeError '''
#TypeError: can only concatenate str (not "int") to str
# color = 'blue'
# age = 25
# result = color + age 


# TypeError: 'str' object is not callable
car = 'chevy'
# car() 

# TypeError: list indices must be integers or slices, not str
fav_animals = ['dog', 'cat', 'bird']
index_value = '1'
# print(fav_animals[index_value]) 


# TypeError: 'int' object is not iterable
# for i in 155:
#     print(i) 

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
def add_two(num1, num2):
    return num1 + num2 
# add_two(5, 'hello')


# Keyboard interruption exception

# i = 2
# while i > 0:
#     i += 1
#     print(i)  # KeyboardInterrupt


# Dividing by zero



# Let's prevent this




# Lets implement a try, except, than test







'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customer's age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

'''




# With Except / Else
# try:
#     customer_age = int(input("Enter your age please: "))
# except ValueError:
#     print("Age must be an integer value")
# else: 
#     print('Ineligable for discount') if customer_age >= 65 else print('Eligible for discount')

# With Except / Else / Finally
# try:
    # customer_age = int(input("Enter your age please: "))
# except ValueError:
    # print("Age must be an integer value")
# else: 
    # print('Ineligable for discount') if customer_age >= 65 else print('Eligible for discount')
# finally:
    # print("Hello, I run no matter what!")

''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

'''





''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''
import math

# def get_positive_float(prompt):
#     """Prompt the user to enter a positive float."""
#     while True:
#         try:
#             # Take input from the user
#             user_input = input(prompt)
#             # Convert the input to a float
#             number = float(user_input)
            
#             # Check if the number is negative
#             if number < 0:
#                 # Raise a ValueError if the number is negative
#                 raise ValueError("Cannot calculate the square root of a negative number.")
            
#             return number  # Return the valid positive float
        
#         except ValueError as ve:
#             # Catch the ValueError and print an error message
#             print(f"Invalid input: {ve}. Please enter a valid positive number.")

# def main():
#     """Main function to compute the square root."""
#     number = get_positive_float("Enter a positive number to find its square root: ")
    
#     # Calculate the square root
#     square_root = math.sqrt(number)
    
#     # Display the result
#     print(f"The square root of {number} is {square_root:.2f}")

# # Execute the main function
# if __name__ == "__main__":
#     main()


# Propogating exceptions (functions)


