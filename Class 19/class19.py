import datetime

'''Classes'''

# NOTE TO SELF: A CSS class is used to define a set of styles that can be applied to HTML elements to control their appearance, such as color and layout. A Python class is a blueprint for creating objects that bundle data and functions together, enabling object-oriented programming and encapsulation of behavior and attributes.

class Point2d():
    # This first method, is your constructor it builds your object
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    # This is our string method, it delivers a string representation
    def __str__(self):
        return f'({self.x},{self.y})'
   
    # This will control the == operator
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False
   
    def __add__(self, other):
        return Point2d(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y - other.y)
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
    # MUTATOR METHOD - a method that will change the attributes of your object
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

# ACCESSOR METHOD
def get_x(self):
    return self.x
def get_y(self):
    return self.y

 
point1 = Point2d(3, 5) # CREATED AN OBJECT OF THE CLASS
point2 = Point2d(4, 11)
 
# print(point1)
# print(point2)
 
# __eq__
print(point1 == point2)
 
#__add__
point3 = point1 + point2
print(point3)

#__sub__
point4 = Point2d(10, 11)
point5 = point4 - point3
# print(point5)

# __lt__
print(point1 < point2)

# Mutator method - set
leahs_point = Point2d(5, 11)
leahs_point.set_x(25)
leahs_point.set_y(15)
print(leahs_point)

my_x_value = leahs_point.set_x()
my_y_value = leahs_point.set_y()

# print(my_x_value, my_y_value)


'''Date Class'''
class Date:
    
    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'{self.month: 02d}/{self.day:02d}/{self.year}'
    
    def __eq__(self, other):
        if self.year == other.year and self.month == other.month and self.day == other.day:
            return True
        return False
first_date = Date(2004, 10, 4)
second_date = Date(2004, 10, 4)

print(first_date == second_date)

my_date_info = Date(2002, 9, 5)
print(my_date_info)