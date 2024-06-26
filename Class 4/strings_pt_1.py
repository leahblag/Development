''' Strings 

Strings are how we store text in python.
Strings are actually a sequence of characters.
Strings are immutable - this means that if we want to change a string we have to completely remake the string. (More on this next class)

'''

''' Printing Exercise

You have a variable called hours which equals 24, the number of hours in a day.
Print There are 24 hours in a day. Make sure to use your variable.
First, print using commas. Remember that using commas automatically adds spaces!
Now, print using string concatenation. Remember to cast hours to a string and manually add the spaces!


'''
# Commas
hours = 24


# Concatenating



# Formatted Strings


''' Concatenation and Multiplication '''


# Concatenation



# Multiplication

greeting = 'hip hip hooray'


'''
Create a variable called fav_food, and assign a string value of your favorite food. Create a second variable, called result, which multiplies your fav_food variable by 10
'''


'''
Using the 'in' keyword solve the following

Is 'a' in giraffe?
Is 'z' in birthday?
Is 'w' in wrapper?

'''



'''
Using the len function find the number of characters in the following strings

Pardon
Halloween
Ice Cream
Tank
Laptop
'''




''' Let's try some string methods '''

# capitalize() Converts the first character to upper case

color = 'blue'
color = color.capitalize()


# casefold() Converts string into lower case

name_one = 'sIMoN'
name_two = 'SimON'


# center() Returns a centered string
# print('hello'.center(100))


# count() Returns the number of times a specified value occurs in a string
my_string = 'abracadabra'



# start end parameter



# expandtabs() Sets the tab size of the string

testing_tabs = 'Happy\tWednesday\tEveryone!'



# find() Searches the string for a specified value and returns the position of where it was found
day = 'Tuesday'
month = 'June'
movie = 'Lord of The Rings'

# Find position of e in day


# Find position of J in month


# Find the position of R in movie



# Note: Find returns -1 if the character is not in the string


# Find the position of b in movie


# index() Searches the string for a specified value and returns the position of where it was found

fav_sport = 'football'


# Error if letter doesnt exist


'''
Create a variable called index_of_y and apply the index string method to locate the index position of the letter y.  What happens if we try to locate a letter that does not exist in our string?
'''
fav_car = 'toyota'


''' More string methods '''

# isalnum() Returns True if all characters in the string are alphanumeric (Letters and Numbers)
word_one = '%^&*'
word_two = 'hello'
word_three = 'abc123'



# isalpha() Returns True if all characters in the string are in the alphabet (Letters only)
word_four = 'abc123'
word_five = 'abcdef'
word_six = 'abc$%*()'



# isdecimal() Returns True if all characters in the string are decimals
num_one = '12345'
num_two = '4.123'
num_three = 'abcde'




# isdigit() Returns True if all characters in the string are digits
num_four = '12345'
num_five = '4.53'
num_six = 'five'



'''
isdigit & isnumeric & isdecimal

https://miguendes.me/python-isdigit-isnumeric-isdecimal

'''
# Isdigit
# all characters in the string are digits
# print('102030'.isdigit())

# 'a' is not a digit
# print('102030a'.isdigit())

# isdigit fails if there's whitespace
# print(' 102030'.isdigit())

# it must be at least one char long
# print(''.isdigit())


# dots '.' are also not digit
# print('12.5'.isdigit())


''' Is decimal'''
# isdecimal
# print('5'.isdecimal())

# superscripts are not decimal
# print('⁵'.isdecimal())

# superscripts, false
# print('5⁵'.isdecimal())

# negative sign, false
# print('-4'.isdecimal())

# decimal point, false
# print('4.5'.isdecimal())


# islower() Returns True if all characters in the string are lower case
house_type = 'MULTI-FAMILY'


''' Try the islower method to test if the following strings are upper and lower case'''
animal = 'GIRAFFE'
car = 'truck'
season = 'SUMMERTIME'



# isupper() Returns True if all characters in the string are upper case


# isnumeric() Returns True if all characters in the string are numeric


val = '5005'


val = '10534875'


val = '5⁵'


val = '⁵'


val = '⅕'




# isspace() Returns True if all characters in the string are whitespaces
my_word = '    '

my_new_word = '   hello'



# istitle() Returns True if the string follows the rules of a title

song_one = 'Time To Say Goodbye'
song_two = 'eye of the tiger'
song_three = 'Sing for the moment'





# join() Joins the elements of an iterable to the end of the string
my_colors = ['blue', 'yellow', 'red']



# lower() Converts a string into lower case
weather = 'RAINY'



# Partition - looks for the match and separates into a tuple with before match, match, after match

string = "Let's see if this really works!"



# replace() Returns a string where a specified value is replaced with a specified value
test_name = 'abraham'



# split() Splits the string at the specified separator, and returns a list

string = 'I would like to split up this string'


# # splitlines splits at new line
txt = "Thank you for the music\nWelcome to the jungle"


# startswith() Returns true if the string starts with the specified value
str = 'zootopia'



# strip() Returns a trimmed version of the string

# txt = "     banana     "



# reference vs value equality: == vs is

x = 'hello'
str2 = "HELLO".lower()



# What is your name


# Let's shorten our code


# Let's sanitize our string!




'''
Example

Write some code that will take a string from the user and print if it is a number or not.

Examples:
apple
False

4
True


'''



'''
Take a word from the user. Then take a number from the user. Then print whether the word is longer than the number.

Examples:
apple
6
False

python
4
True

Hint: use len() to find the length of the string, and don’t forget to cast to int()

'''





'''
Write some code that takes a string from the user, and prints how many vowels are in the string. (Vowels are a, e, i, o, u)
How will you count both uppercase and lowercase vowels?
What string method can you use to count the number of vowels?

'''




''' Exercise - Challenge

Write some code that will print a box around a string.

Examples:
User input: hello
*******
*hello*
*******

User input: programming is fun
********************
*programming is fun*
********************
Hint: You will have to use the len() function, string concatenation (+), and string multiplication (*)

'''

