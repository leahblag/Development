# LEAH BLAGBROUGH
# ASSIGNMENT #1: 
# PYTHON 1: PROGRAMMING

'''Note for Jean: Hi Jean! I hope you're doing well. I made a small tweak to your template. I thought it made more sense to show the username requirements first and then, after validating the username, show the password requirements. Hope that's okay!'''


# PRINT STATEMENTS OUTLINING DOCUMENT:
print("HI! Welcome to Leah's website sign up!!")

# INITIALIZING VARIABLES:
username = ""
password = ""
taken_usernames = ['admin', 'admin123', 'user1', 'superuser']

# A LIST TO HANDLE ERROR MESSAGES:
error_messages = []

# FUNCTION TO VALIDATE THE USERNAME:
def valid_username(username):
    if not username:
        error_messages.append("Username CANNOT be left empty!")
        return False
    if not username[0].islower():
        error_messages.append("Username MUST start with a lowercase letter.")
        return False
    if not username.isalnum() and '_' not in username:
        error_messages.append("Username can ONLY contain letters, numbers, and underscores.")
        return False
    if username in taken_usernames:
        error_messages.append("Sorry, this username has already been taken.")
        return False
    return True

# FUNCTION TO VALIDATE THE PASSWORD:
def valid_password(password):
    if len(password) < 8:
        error_messages.append("Password MUST be at LEAST 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        error_messages.append("Password MUST contain at least ONE UPPERCASE LETTER.")
        return False
    if not any(char.islower() for char in password):
        error_messages.append("Password MUST contain at least ONE LOWERCASE LETTER.")
        return False
    if not any(char.isdigit() for char in password):
        error_messages.append("Password MUST contain at least ONE DIGIT.")
        return False
    if not any(char in "!@#$%^&*_-?" for char in password):
        error_messages.append("Password MUST contain at least ONE SPECIAL CHARACTER! such as: !, ?, @, #, $, ^, &, *, _, -")
        return False
    if ' ' in password:
        error_messages.append("Password CANNOT contain spaces.")
        return False
    return True

'''USERNAME INFORMATION / REQUIRMENTS'''

# START THE WHILE LOOP FOR USERNAME:
while True:
    error_messages.clear()
   
# SHOW USERNAME REQUIREMENTS:
    print("Username Requirements: your username MUST...")
    print("1. Start with a lowercase letter")
    print("2. Can ONLY contain letters, numbers, and underscores")
    print("3. Cannot be one of the following taken usernames: admin, admin123, user1, superuser")
   
# GET USERNAME:
    username = input("Please enter a username: ")
   
# TESTING USERNAME & ENFORCING LOGIC:
    if not valid_username(username):
        print("Sorry, this is an invalid username.")
        for error in error_messages:
            print(error)
        continue
    
# IF USER IS VALID, BREAK LOOP:
    break

'''PASSWORD INFORMATION / REQUIRMENTS'''

# START THE WHILE LOOP FOR PASSWORD:
while True:
    error_messages.clear()
   
# SHOW PASSWORD REQUIREMENTS:
    print("Password requirements: your password MUST...")
    print("1. Be at least 8 characters long")
    print("2. Contain at least one uppercase letter")
    print("3. Contain at least one lowercase letter")
    print("4. Contain at least one digit")
    print("5. Contain at least one special character: !, ?, @, #, $, ^, &, *, _, -")
    print("6. Cannot contain any spaces")
   
# GET PASSWORD:
    password = input("Please enter a password: ")
   
# TESTING PASSWORD & ENFORCING LOGIC:
    if not valid_password(password):
        print("Invalid password.")
        for error in error_messages:
            print(error)
        continue
    
# If PASS IS VALID, BREAK LOOP:
    break

'''LOGIN ATTEMPTS'''

# IF PASSED, ASK USER TO LOGIN:
print("Congratulations! Sign up successfull! Now, please log in.")

# LOOP FOR LOGIN ATTEMPT:
while True:
    login_username = input("Enter your username to log in: ")
    login_password = input("Enter your password to log in: ")
   
# CORRECT INFO INPUT = PROGRAM COMPLETE:
    if login_username == username and login_password == password:
        print("Login successful!")
        exit()
    else:
# SEND USER BACK TO THE BEGINNING IF INCORRECT
        print("Incorrect username or password. Please try again.")
