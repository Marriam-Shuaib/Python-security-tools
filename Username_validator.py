# Username Validator — checks if a username is valid

def username_validator(username):
    
    # Clean the input first
    username = username.strip().lower()
    
    # Check if username starts with a number
    if username[0].isdigit():
        print("Invalid: cannot start with a number")
    
    # Check if username is too short
    elif len(username) < 3:
        print("Invalid: too short")
    
    # Check if username contains spaces
    elif " " in username:
        print("Invalid: no spaces allowed")
    
    # Check if username is a reserved word
    elif "admin" in username or "root" in username:
        print("Warning: reserved username detected")
    
    # Passes all checks
    else:
        print("Valid username")

# Get username from user and validate it
username = input("Enter your username: ")
username_validator(username)