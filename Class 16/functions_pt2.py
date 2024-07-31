
# # Functions Part 2

# # With doc string and type hinting

# def my_function(country: str = "Norway") -> None:
#     # FUNCTION RETURNS USERS COUNTRY
#     print("I am from " + country)

# my_function('Sweden', 5)
# my_function('India', 5)
# my_function()
# my_function('Brazil', 4)

# def test_function(name):
#     return name

# # test_function('Hello')
# users_name = test_function('Joe')
# # print(users_name)
'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''

def center(numbers, use_median=False):
  from statistics import mean, median
    
  if use_median:
        return median(numbers)
  else:
        return mean(numbers)


test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]

print("Mean of test_list1:", center(test_list1))          # Mean // ANSWER: 4
print("Median of test_list1:", center(test_list1, True))  # Median // ANSWER: 3.5

print("Mean of test_list2:", center(test_list2))          # Mean // ANSWER: 6.857142857142857
print("Median of test_list2:", center(test_list2, True))  # Median // ANSWER: 7


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
import statistics

my_list = [1,2,4,5,5]
def get_stats(num_list):
    mean = statistics.mean(num_list)
    median = statistics.median(num_list)
    mode = statistics.mode(num_list)
    return mean, median, mode
print(f"Mean: {get_stats(my_list)[0]}")
print(f"Median: {get_stats(my_list)[1]}")
print(f"Mode: {get_stats(my_list)[2]}")



'''Global variables'''




'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers
def add_two(x, y):
    return x + y
 
# print(add_two(5, 10))
 
# Written as a Lambda
lambda x, y: x + y
 
# Assigning the lambda to a variable
add_two_lambda = lambda x, y: x + y
 
print(add_two_lambda(9, 15))
 
print((add_two_lambda)(5,10))

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
def power(num, n):
    return num ** n

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