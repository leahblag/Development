# LEAH BLAGBROUGH
# ASSIGNMENT #4
# PYTHON 1



# DIRECTIONS:

'''Write a function that takes a list of numbers as input and returns the average of all the numbers in that list. Have fun and be sure to test test test! '''


# FUNCTION:
def average_of_list(numbers):
    if len(numbers) == 0:
        return "This list is empty & cannot calculate an average."
    
    total_sum = sum(numbers) # adds up the numbers
    count = len(numbers) # finds out how many numbers there are
    average = total_sum / count # finds how many seperate numbers were entered
    return average

def run_program():
    # ASKS USER TO ENTER NUMBERS, SEPERATED BY SPACES
    user_input = input("Enter numbers separated by spaces: ")
    
    # SPLITS INPUT INTO A LIST OF STRINGS
    number_strings = user_input.split() 
    
    # CONVERTS LIST OF STRINGS INTO NUMBERS
    numbers = [] # Converts each substring into a float and stores them in a list called 'numbers'
    for num_str in number_strings:
        numbers.append(float(num_str))
    
    # CALCULATING AVERAGE USING THE FUNCTION
    average = average_of_list(numbers)
    
    # RESULT
    print("The average of the numbers is:", average)

# RUNS THE MAIN FUNCTION AKA PROGRAM
if __name__ == "__main__":
    run_program()

