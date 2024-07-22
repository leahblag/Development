''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?

user_data = {"user_id": 400,
             "fname": "Fritz"}

# print(user_data)
# print(type(user_data))

# Bracket notation - we can grab the value by referencing the key

# print(user_data["fname"])
# print(user_data["user_id"])

# Add new key/value pair
user_data['address'] = 'elm street'

# lets look at all the methods available to us
# print(dir(user_data))

# lets try one
print(user_data.__contains__("username"))

# Dict constructor
new_dict = dict()
# print(new_dict)
# print(type(new_dict))

# Let's update our name key
# user_data = dict(user_id = 400, fname)


# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Let's look at our keys
print(f'The Keys for this dog dictionary are {dog.keys()}')

# or set it as a variable?



# Lets use the values methods to get the values from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets look at our values
print(f'The Keys for this dog dictionary are {dog.values()}')

# or set to a variable
dog_information = dog.values
# Lets use clear method to remove all elements

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}
print(dog)
dog.clear()
print(dog)
# Lets use get method to get a key value

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# print(dog.get('age'))

# lets look at one of the parameters to show an error if the key doesnt exist

# print(dog.get('temperment', 'Key does not exist in dictionary'))

# Lets create a copy

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

new_dog = dog.copy() # CREATED A COPY
dog['breed'] = 'Labordoodle' # UPDATING A VALUE IN OUR ORIGINAL DICTIONARY.

# print(f'Original Dictopnary': {dog})
# print(f'Copy of original: {new_dog}')

# Lets remove a specified key with pop
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
dog.pop('breed')
# print(dog)

# Let's remove a last inserted key-value pair with pop item
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
age = dog.popitem()
# print(age)

# Get a list with each key-value pair with items
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}



# we can loop through
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

for key, value in dog.items():
    print(key, value)

# Update dictionary
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
size = {"size": "small"}
dog.update({"temperment": "happy"})
dog.update(size)

dog.update({"size": "medium"})
print(dog)


# Update can also update current key value pairs, as well as adding



# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}

# print(list[3])
# print(dict1[3])

list1[3] = 'z'
dict1[3] = 'z'

'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

# list1 = ['one', 'two', 'three']
# list2 = [4, 10, 30]

# new_dict = {}
# for i in range(len(list1)):
#     new_dict.update({list1[i] : list2[i]})
# print(new_dict)


''' Zip Solution

When you use the zip() function in Python, it takes two or more data sets and "zips" them together. This returns an object containing pairs of items derived from the data sets. 
'''

my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

result = dict(zip(my_keys, my_values))
# print(result)



'''
Exercise

Write a dictionary that five countries and their languages Then have your code print the languages of each country one at a time.
Hint: Use the items() method


'''

languages = { 'USA': 'English', 'Mexico': 'Spanish', 'France': 'French', 'Portugal':'Portugese', 'Belgium':'Dutch' }
    



# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}

# print(choices['flavors[1]])
# print(choices["sizes"][2])

# Lets make a dataframe out of this
import pandas as pd

choices_df = pd.DataFrame(choices)
# print(choices_df)

# Lets rename the columns

rename_choices_dict = {"flavors" : "column1",
                       "sizes" : "column2",
                       "region" : "column3"}

choices_df.rename(columns=rename_choices_dict, inplace=True)
choices_df.to_csv('output.csv', index=False)
print(choices_df)


'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''


'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list

output = {}

for m in my_list_items: # Loop through our list
    if m not in output:
        output[m] = 1
        # print(output)
    else:
        output[m] += 1    
        # print(output)

# What about the count method for Lists?? 
for m in my_list_items:
    output[m] = my_list_items.count(m)
    # print(output)

from statistics import mode

my_list_items = [1,2,4,1,3,4,1,1]
result = mode(my_list_items)
# print(result)


'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},
           {'name': 'David', 'title': 'developer', 'salary': 65000}]


# INITIALIZE DICTIONARY
salary_totals = {}
job_counts = {}

# ITERATE THROUGH EACH RECORD
for r in records:
    title = r['title']
    salary = r['salary']
    
    # UPDATE CUMLATIVE SUMS
    if title in salary_totals:
        salary_totals[title] += salary
        job_counts[title] += 1
    else:
        salary_totals[title] = salary
        job_counts[title] = 1

# INITIALIZE A DICTIONARY FOR AVERAGE SALARIES
average_salaries = {}

# CALCULATE AVERAGE SALARY
for title in salary_totals:
    average_salaries[title] = salary_totals[title] / job_counts[title]

print(average_salaries)

import pandas as pd













 



