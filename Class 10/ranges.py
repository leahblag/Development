'''
Ranges
    - Must be integers, whole numbers
    - Used to iterate
    - Does not store all the numbers, but knows what they should be
    - Simple to write and create
    -saves memory
'''

# COUNTING TO 20 USING RANGE FUNCTION:

# twenty_count = range(21)
# for t in twenty_count:
#     print(t, end=' ')

# for i in range(3, 2):
#     print(i)


''' Let's try these '''

# for i in range(16, 2, -3):
#     print(i, ends=' ')

# for i in range(4):
#     print(i, i+1, sep=', ')

'''
Write a range that is every five years from 1960 to 2000.
'''
# every_five_years = range(1960, 2001, 5)

# for e in every_five_years:
#     print(e, end=' ')

'''
range(start, stop, step)
'''


'''
Write a range that counts down from 30 to 0
'''
# countdown = range(30, -1, -1)
# for c in countdown:
#     print(c, end=' ')


'''
Exercise
Rewrite the for loop we made last class that goes through a list and prints each item in the list, along with its index. (Hint: you can use a range, and you won't need a separate counter variable.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
'''

planets = ["mercury", "venus", "earth", "mars"]
output = ' '

counter = 0

# for p in range(len(planets)):
    # output += f'{p}: {planets[p]}'



''' Exercise
You have a list of employees, and a list of job titles. Assume the lists are the same length and in the same order.
Use one for loop to go through both lists and print the job title of each employee.
For example, if these are your lists:
employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']
This should be your output:
Bob's job title is accountant.
Cynthia's job title is engineer.
Abdul's job title is recruiter.

'''

employees = ['Bob', 'Cynthia', 'Abdul']
job_titles = ['accountant', 'engineer', 'recruiter']


# Determine the length of the lists (assuming they are the same length)

num_employees = len(employees)

# Iterate through each index

# for i in range(num_employees):
#     employee = employees[i]
#     job_title = job_titles[i]
#     print(f"{employee}'s job title is {job_title}.")


'''
Write some code that creates a range based on what the user enters. 
Challenge: you can make a range with 1, 2, or 3 numbers. How would you allow the user to pick any of these options?
'''
# ASK USER TO CHOOSE PARAMETERS:

# while True:
    # num_count = input("Enter the number of values for the range (1, 2, or 3): ")
    # if num_count.isdigit() and int(num_count) in [1, 2, 3]:
        # num_count = int(num_count)
        # break  # EXIT THE LOOP IF INPUT IS VALID
    # else:
        # print("Invalid input. Please enter 1, 2, or 3 only.")

# GET NUMBERS FROM USERS, BASED ON THEIR CHOICE:

# if num_count == 1:
    # num1 = int(input("Enter the number for the range: "))
    # my_range = range(num1, num1 + 1)
# elif num_count == 2:
    # num1 = int(input("Enter the first number for the range: "))
    # num2 = int(input("Enter the second number for the range: "))
    # my_range = range(num1, num2 + 1)
# elif num_count == 3:
    # num1 = int(input("Enter the start number for the range: "))
    # num2 = int(input("Enter the end number for the range: "))
    # num3 = int(input("Enter the step size for the range: "))
    # my_range = range(num1, num2, num3)

# PRINT THE GENERATED RANGE:

# print("Generated range:", list(my_range))
