
# Functions Part 2

# With doc string and type hinting




'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''





test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]


'''Documentation, type hinting, shorthand if-then-else'''


# Returning multiple values





'''
Exercise
Write a Python function called get_stats that takes in a list of numbers and returns the following three values: The mean, the median, and the mode of the list.
Call the function on a list, and print each statistic on a separate line.
my_list = [1,2,4,5,5]
Output:
Mean: 3.4
Median: 4
Mode: 5
'''

my_list = [1,2,4,5,5]


'''Global variables'''




'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers


# Written as a Lambda


# Write the following functions as Lambdas

def greeting(fname):
    print(f'Hello, {fname}')

# greeting("Sally")


def double_me(num):
    return num + num

# print(double_me(500))


'''
Exercise
Write a function that computes the n-th power of a number, given two arguments, num and n.
Now, write a lambda that is equivalent to the lambda.
'''
# function


# lambda




''' Higher Order Functions
These are functions that may accept a function as an argument or return a function as its output. In Python, reduce(), map() and filter() are some of the most important higher-order functions. When combined with simpler functions, they can be used to execute complex operations.

filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

map - returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
# Let's use filter() to find the even numbers in a list 
# filter(fun, iter)

# Function


# Lambda



my_list = [0,1,2,3,4,5,6,7,8,9,10]




# Let's use map() to multiply every value in this list by 3
# map(fun, iter)

triple_me = [0,1,2,3,4,5,6]
# Function




# Lambda



# Lambda with sort
# sorted(iterable, key=key, reverse=True/False)

students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]



''' 
Write a lambda function that makes a string a title case and apply the function to the list below with a map function
words = ['make', 'us', 'title', 'case']

'''



''' Write a lambda function that will add ten to a list item if that list item is greater than or equal to 50, otherwise it will subtract five

my_numbers = [50, 12, 19, 80, 5, 75]
'''

''' Write a lambda function and utilize reduce to add all the numbers in this list

add_me_up = [50, 12, 9, 100, 56, 70]
'''