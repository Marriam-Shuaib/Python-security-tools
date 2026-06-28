# Python-security-tools
Small Python projects built while learning cybersecurity
Python for cybersecurity in my first year of BSc Cybersecurity.

## Tools

### Password Auditor
Checks password strength based on length, common patterns, 
and weak passwords. Built using Python functions and string methods.

How to run:
python password_auditor.py

Checks for:
- Passwords shorter than 8 characters
- Passwords ending with 123
- All lowercase passwords
- Common passwords like "password"

### Username Validator
Validates usernames against basic security rules.

How to run:
python username_validator.py

Checks for:
- Usernames starting with a number
- Usernames that are too short
- Spaces in usernames
- Reserved names like admin or root

### Connection Checker
Tests if a connection can be made to a hostname 
on a specific port. Uses try/except for error handling.

How to run:
python check_connection.py

### System Info
Grabs your machine's hostname, IP address, and 
current directory. Saves output to system_info.txt.

How to run:
python system_info.py

## What I learned
- Python functions and parameters
- String methods and input validation
- File handling — reading and writing to files
- Error handling with try/except
- Importing and using os and socket libraries
- If/elif/else logic for security checks

## Technologies
- Python 3
- VS Code
- Libraries: os, socket
