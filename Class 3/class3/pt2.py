# Operator, Boolean Expessions and comments

# I am a comment
temperature = 95 # I am an inline comment

# I am a standard single line comment
first_name = 'Thomas' '''Multi-line comment inline'''
last_name = 'The train' """inline comment with double quotes"""

#Comment me

length = 5 #rectangle-length
width = 7 #rectangle-width

# Calculating perimeter of a rectangle
perimeter = 2 * (length + width)

#Output
# print(perimeter)

'''Script to convert temperature'''

farenheit = 89 

 #Formula to find output
celius = (farenheit - 32) * 5/9

#output
# print(celsius)

''' Shortcut operators'''
# Add 5 to me
age = 25
age +=25
# print(age)

# add 10 years
year = 2024
year += 10 #adding 10 via shortcut
# print(year)

#Subtract 20
num_one = 55
num_one -= 20
# print(num_one)

#Subtract 15
num_two = 11
num_two -=15

#Multiply by 3
my_value = 9
my_value *=3
# print(my_value)
 
#Multiply by 10
mileage = 15
mileage *=10
# print(mileage)
 
# Divide by 2
pizza_slices = 8
pizza_slices /= 2
# print(pizza_slices)

# Divide by 7
fees = 8.90
fees /= 7


# Raise to the third power **
num_three = 6
num_three **=3
# print(num_three)

# Raise to the second power **
data =16
data **=2
# print(data)

#Integer division, how many times does 3 go into 16?
val_one = 16
val_one //=16
# print(val_one)

#Integer divide by 4 //
val_two = 9
val_two //=9
# print (val_two)

# Modulus we use often to find if a value is odd or even
# Find the remainder if divided by 3 %
val_three = 10
val_three %=3
# print(val_three)

# Find the remainder if divided by 5 %
val_four = 14
val_four %=5
# print(val_four)

farenheit = 89 

 #Formula to find output
celius = (farenheit - 32) * 5/9
# print(celsius)

farenheit -=32
farenheit *= 5/9
celsius = farenheit
# print(celsius)

''' Boolean Operators'''

#Is 7 less than 5? <
# print(7 < 5)
result = (7 < 5)
print( "Is seven less than five?" ,result)

print(4 <= 4)
result = 4 <= 4
print("is 4 less than or equal to 4?", result)

# Is 6 greater than 2? >
print (6 > 2)
result = (6 > 2)
print("Is 6 greater than 2?", result)

# Is 5 greater than or equal to 6? >=
print (5 >= 6)
result = (5 <= 6)
print("Is 5 greater than or equal to 6?", result)

# Is 5 equal to 5? =
print

# Is 100 not equal to 75? !=

# and 
# print(5 == 5 and 4 == 4) # True
# print(2 == 2 and 3 == 1) # False
# print(1 == 2 and 2 == 10) # False

log_1 = (5 == 3)
log_2 = (4 == 7)
print('Log 1', log_1)
print('Log 2', log_2)
print('Log 1' and 'Log 2', log_1 and log_2)

#or 
# print(5 == 5 and 5 == 3) # True if at least 1 is true

# not
is_it_autumn = True
# print(not is_it_autumn)

x = 5
y = 10
 
#are we the same object
fname = 'Taylor'
first_name = 'Taylor'
# print(fname is first_name)


# in
# print('J' in 'January')
# print('F' in 'March')

#Formatted string
pet = 'dog' # my variable to be used in my formatted string
print(f'I own a {pet}')


