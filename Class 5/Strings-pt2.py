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
# Get user input:

# userinput = input("What is your word or phrase")
# top_and_bottom_border = len(userinput) * '*'
# print(userinput)
# print(top_and_bottom_border)
# print('*'+userinput + '*')
# print(top_and_bottom_border)

# Create top and Bottom Border:

# Generate output

''' Strings Part 2'''

# Strings are immutable
# Just applying the method to the string won't change the original value
str_1 = 'BLUE' 
str_1.lower()

str_1 = str_1.lower()
# print(str_1)



day = '  TUESDAY   ' # Create a new string with no whitespace 
new_day = day.strip()

# print(len(day)) # 12 Characters
# print(len(new_day)) # 7 Characters, white space is stripped

'''Indexing, with square brackets'''

word = 'Jasmine'
# first_letter_of_word = word[0]
# print(first_letter_of_word)
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])
# print(word[6])
# print(word[7])
# print(word[8]) # INDEXERROR = STRING INDEX OUT OF RANGE


# Create a variable to capture the first letter of this string
greeting = 'whatssup!'
# first_position = greeting[0]


# Grab the last letter in a variable
# last_position = greeting[len(greeting)-1]
# print(last_position)



# Using the length and bracket notation, access the last letter in the variable below
month = 'February'

last_letter_of_month = month[-1]
# print(last_letter_of_month)

# Using bracket notation access the letter x, the letter e, and the letter d 
first_name = 'Alexandra'
# letter_x = first_name[3]
# print(letter_x)




'''Reverse indexing'''
fav_animal = 'Ostrich'
# print(fav_animal[-1])
# print(fav_animal[-2])
# print(fav_animal[-3])
# print(fav_animal[-4])
# print(fav_animal[-5])
# print(fav_animal[-6])
# print(fav_animal[-7])
# print(fav_animal[-8]) # SHOULD BE ERROR


# Using bracket notation and reverse indexing, access the letter g, the letter i, the letter p
fav_season = 'spring'
# print(fav_season[-1])
# print(fav_season[-2])
# print(fav_season[-3])
# print(fav_season[-4])
# print(fav_season[-5])
# print(fav_season[-6])


''' Slicing '''
# There are 3 parameters available with indexing with bracket notation [start:stop:step]
fav_food = 'spaghetti'
slice_of_fav_food = fav_food[2:7] # PULLS OUT 2-7


# Using slicing please create a string that accesses 'rica' in 'America'

country = 'America'
slice_of_country = country[3:7]


# Using slicing please create a string that accesses 'ora' in 'Dora the explorer'
cartoon = 'Dora the explorer'
slice_of_cartoon = cartoon[1:4]
# print(slice_of_cartoon)


# Using slicing please create a string that accesses 'explo' in 'Dora the explorer'


# Using slicing please create a string that accesses 'albo' in 'Rocky Balboa'
boxer = 'Rocky Balboa'



# Let's step through this string 2 characters at a time
superheroine = 'Wonder Woman'


# Lets step through this entire word and skip by 4
word = 'Supercalifragilisticexpialidocious'


'''Slicing in reverse 
Refer to slice image as a guide if needed

'''


'''

D A Y C A R E
0 1 2 3 4 5 6


D   A   Y   C   A   R   E
-7 -6  -5  -4  -3  -2  -1

'''
random_word = 'daycare' 

# Fun with reverse indexing
# print(random_word[1:0:-1]) # a
# print(random_word[2:0:-1]) # ya
# print(random_word[4:0:-1]) # acya
# print(random_word[5:0:-1]) # racya
# print(random_word[6:0:-1]) # eracya
# print(random_word[7:0:-1]) # eracya
# print(random_word[8:0:-1]) # eracya




'''
Write some code to print the second half of a string.
Example:
python
hon
'''

# STEP 1: CREATE A VARIABLE
var_1 = 'python'

# STEP 2: CREATE A VARIABLE TO GET HALF OF THE LENGTH OF THE WORD
var_2 = len(var_1) / 2
# print(var_1)
# print(type(var_2))
var_3 = var_1[var_2:(len(var_1))]

# STEP 3: CREATE FINAL BRACKET MOTION AND OUTPUT



# End Parameter
# print('Hello', end=' ')
# print('World', end='')
# print('!', end='\n')


# Sep Parameter
# print("Today I woke up at ", 8, " am", sep='*')

'''
Get input from the user and store it in a variable called userin.
Then print the user input. The output should follow exactly this format, including the colon and period at the end:
You entered: userin.
Where userin is what you got from the user.
You must format the print statement like this:
print("You entered",userin)
How can you add sep and end keywords to get the exact formatting shown above?
'''


'''
You need to write a script that will generate an email to a customer who has just made a purchase. You have 3 variables:
name, which stores the customer's name as a string
product, which stores the product name as a string
price, which stores the price of the product as a float
Use an f-string to generate an email message with the following text, and print it. Make sure to round the price to 2 decimal places. The email should be one multi-line string.
Dear {name},
Thank you for your purchase of a {product}. Your credit card has been charged ${price}.
We appreciate your business and look forward to serving you again.
Sincerely,
The ABC Company
'''

name = 'Josiah Wilson'
product = 'ABC Sneakers'
price = 74.95343452342





'''
Write some code that takes a string and tells if it is a palindrome (same forwards and backwards).
Hint: Use indexing/slicing and boolean expressions

Examples:
racecar: True
cat: False
'''