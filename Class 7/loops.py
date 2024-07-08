

''' While Loops

While loops run as long as the given condition returns a True boolean.
'''

''' Example
Create a while loop that prints every integer from 1 to 10.
'''

i = 0 # INITIALIZATION

# while i <= 10: # CONDITION
print(i) #
i += 1 # INCREMENT OR DECREMENT


# We can also assign it to a variable
# end = 10
# counter = 0

# while counter <= end:
#     print(counter)
#     counter += 1

# we can choose our end point. our starting point is 0. We will count up by one and display it to the user as long as start is less than end.

# end = int(input('Enter your number:'))

# while counter <= end:
#     print(counter)
#     counter += 1


# Let's create and infinite loop, a condition we will never see fulfilled, kill your terminal with ctrl + c

end = 10
start = 0

# while start < 10:
#     print(start)
#     start -= 1




''' While loops and user input 

This will keep asking us to input a word until we input "stop" Let's follow it line by line

'''

# userin = ' ' # initialize your variable

# while userin != 'stop':
#     userin = input("Enter something: ")
#     # userin = userin.lower()
#     print(userin)

# print("Done collecting user input")

'''
Improve the login system we wrote last class to allow multiple attempts. Youre developing a login system for a website. Write a Python program that checks whether the user has entered the correct username and password. Just like before:
Create two variables called username and password.
Prompt the user to enter their username and password.
Use conditionals and logical operators to check whether the username and password entered by the user match the username and password variables.
As long as the username and password are incorrect, print “Incorrect username or password”, and keep asking the user for their username and password.
If they match, print “Login successful” and end the program.
'''


# # Initialize all of our variables-
# system_username, system_password = 'admin', 'password'
# username, password = '', ''
# # print(system_username, system_password)


# # While Loop with conditional to handle user input-
# while system_username != username and system_password != password:
#     print("Incorrect username or password")
#     username = input("Please enter your username")
#     username = input("Please enter your password")

# print('Login Successful')

''' For Loops
For loops are used to iterate through something.
For loops perform an action on a group of objects
For loops can be performed on iterables: 

Strings
Lists
Tuples
Dictionaries
Sets

# The Temporary Variable (item, goes out of scope after for loop ends)
for item in collection:
	print(item)

'''

'''
Lets loop through the string "Hello World"

'''
# my_string = 'Hello World'

# for m in my_string:
#     print(m)


'''
Lets loop through a list of colors

'''
colors = ['red', 'green', 'orange', 'yellow']

for c in colors:
    # print(f'My favorite color is {c}')


# ''' Lets loop through a tuple '''
# my_fav_food = ('pizza', 'subs', 'chicken')


    '''Example
Write a for loop that loops through a string, counts all the letters, and then print how long the string is.
'''
# HINT THE COUNTER IS YOUR FRIEND!!!

# season = 'Summer'
# counter = 0

# for s in season:
#     counter += 1
#     # print(s, counter)

# print(f'{season} has {counter} letter(s)')


'''
Exercise - Lets try to add conditionals to the mix

Take a string from the user. Verify that its a number.
Write a for loop that adds all the digits together. Then print the total.

Example:
'14253'
15

Hint: remember to cast to int() for each digit in the loop

'''

# initialize variables and get user input
# userin = input("Please enter your data")

# total = 0 # THIS VARIABLE WILL CAPTURE THE VALUES AS WE LOOP


# # # Verify Decimal, if it is, lets do our fun loop, else we will send the user home with a nice message

# if userin.isnumeric(): # IF THE STRING VALUE IS NUMERIC WE CAN LOOP THROUGH
#     for u in userin:
#         u = int(u)
#         total += u
# else: 
#     print("Sorry, this is not a valid number")

# print(total)

''' More conditionals in loops'''

# words = 'hello'

# vowels = ['a','e','i','o','u'] # [] = LIST

# for word in words: # THIS WILL LOOP THROUGH THE WORDS VARIABLE
#     if word in vowels: # IF THE LETTERS IN WORDS, IS IN VOWELS
#         print(f'{word} is a vowel')
#     else:
#         print(f'{word} is a consonant')



''' Cleaning Strings

You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

test_string = 'a56b32ra87ca++d#@a*&b21r23a'

'''
test_string = 'a56b32ra87ca++d#@a*&b21r23a' # WE ONLY WANT 'A-Z'
output = '' # WE WILL ADD THE LETTERS THAT PASS TESTING TO THIS LIST

for t in test_string: # WE ARE LOOPING THROUGH 
    if t.isalpha():
        output += t

print(output)