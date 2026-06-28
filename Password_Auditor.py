# Password Auditor — checks how strong a password is

def password_audit(password):
    
    # Check if password meets any weak conditions
    weakpassword = password.islower() or password.endswith("123") or len(password) < 8
    
    # Worst case — password is literally "password"
    if password == "password":
        print("Result: Very weak")
    
    # Weak if too short, all lowercase, or ends with 123
    elif weakpassword:
        print("Result: Weak")
    
    # Passes all checks
    else:
        print("Result: Strong")

# Get password from user and run the audit
password = input("Enter your password: ")
password_audit(password)