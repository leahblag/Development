'''
DIRECTIONS: 

Write some code that takes input from the user and prints whether it's a valid email address. Make sure to sanitize the user input with .strip()

An email address is valid if:

-It has a "." at the third-to-last index
-It has exactly one "@" symbol, at the fifth-to-last index or earlier
-There is at least one character before the "@" symbol
-It doesn't have any spaces (doesn't contain " ")
-If all these conditions are met, print True. Otherwise, print False.
-To do this, use boolean statements on your string.
-Test your code on a few inputs to make sure it works!

'''
# Leah Blagbrough :)
# Assingment 3: (DONE IN CLASS)
# June, 17 2024


# GET INPUT:

email = input ("Hello, please enter your email: ")

# CLEAN DATA:

email = email.strip() # note: CLEANING THE STRING WITH THE STRIP METHOD

# TEST 1: It has a "." at the third-to-last index test data - jsmith@gmail.coom

test_1 = (email[-4] == '.')
print(f'Test 1: Does {email} has a "." at the third-to-last index?', test_1)

# TEST 2: It has exactly one "@" symbol, at the fifth-to-last index or earlier

test_2 = ('@' in email[-5::-1])
print(f'Test 2: {email} It has exactly one "@" symbol, at the fifth-to-last index or earlier?',test_2)

# TEST 3: There is at least one character before the "@" symbol

test_3 = (email[0] != '@' )
print(f'Test 3: There is at least one character before the "@" symbol? in {email}', test_3)

# TEST 4: It doesn’t have any spaces (doesn’t contain " ")

test_4 = (' 'not in email)
print(f'Test 4: {email} doesn\'t have any spaces (doesn\'t contain " ")', test_4)


# FINAL TEST WITH 'AND' KEYWORD

all_tests = test_1 and test_2 and test_3 and test_4
print(f'Is {email} valid?', all_tests)
