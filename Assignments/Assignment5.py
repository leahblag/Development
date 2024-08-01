# LEAH BLAGBROUGH
# ASSIGNMENT #5
# PYTHON 1

# DIRECTIONS:
'''
 You have been assigned the task of creating a sales tax calculator for an e-commerce company.
 Write a Python function called calculate_final_price that takes the price of a product and the sales tax rate,
and return the final price including tax. The price should be a positive number, and the tax rate should be
between 0 and 1 (exclusive). If either of them are outside of the valid range, raise a custom ValueError with
 an appropriate error message. Now, test your implementation by asking the user to input a product price and
sales tax rate, and call your function. Catch any potential ValueError raised by the function.
'''
# NOTE to self: THE COMMENTS IN CAPS-LOCK ARE DESCRIPTIVE LABELS
# NOTE to self: The lowercase comments on the same line describe the action taken by that line of code.

# MY WORK:

# DEFINE A FUNCTION TO CALCULATE FINAL PRICE INCLUDING TAX:
def calculate_final_price(price, tax_rate):

    # CHECK IF PRICE IS A POSITIVE NUMBER:
    if price <= 0:  # ensures the price is greater than zero.

        # RAISE A CUSTOM VALUE-ERROR IF PRICE IS NOT POSITIVE:
        raise ValueError("The price should be a positive number.")  # raises an error if the price is not positive.
    
    # CHECK IF TAX RATE IS BETWEEN 0 AND 1 (EXCLUSIVE):
    if not (0 < tax_rate < 1):  # ensures the tax rate is within the valid range.

        # RAISE A CUSTOM VALUE-ERROR IF TAX RATE IS OUTSIDE OF VALID RANGE:
        raise ValueError("The tax rate should be between 0 and 1 (exclusive).")  # raises an error if the tax rate is not between 0 and 1.
    
    # CALCULATE FINAL PRICE INCLUDING TAX:
    final_price = price * (1 + tax_rate)  # computes the final price by adding tax
    
    # RETURN THE FINAL PRICE:
    return final_price  # returns the calculated price to the caller.

# MAIN FUNCTION TO HANDLE USER INPUT AND ERROR CATCHING:
def main():
    try:
        # ASK THE USER TO INPUT THE PRODUCT PRICE:
        user_price = float(input("Enter the product price: "))  # gets the price from user input.
        
        # ASK THE USER TO INPUT THE SALES TAX RATE:
        user_tax_rate = float(input("Enter the sales tax rate (between 0 and 1): "))  # gets the tax rate from user input.
        
        # CALL THE FUNCTION TO CALCULATE FINAL PRICE:
        result = calculate_final_price(user_price, user_tax_rate)  # calculates the final price using the provided inputs.
        
        # PRINT THE FINAL PRICE:
        print(f"The final price including tax is: ${result:.2f}")  # displays the final price to the user.
    
    except ValueError as e:

        # CATCH AND PRINT ANY VALUE-ERROR THAT OCCURS:
        print(f"Error: {e}")  # handles errors and display an appropriate message.

# RUN MAIN FUNCTION IF SCRIPT IS EXECUTED DIRECTLY:
if __name__ == "__main__":  # checks if this script is being run directly.
    main()  # calls the main function.

