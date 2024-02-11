import re

def is_valid_email(email):
    # Regular expression for validating an email address
    pattern = r'^[\w\.-]+@[a-zA-Z0-9\.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
email1 = "example@example.com"
email2 = "invalid_email.com"

if is_valid_email(email1):
    print(f"{email1} is a valid email address.")
else:
    print(f"{email1} is not a valid email address.")

if is_valid_email(email2):
    print(f"{email2} is a valid email address.")
else:
    print(f"{email2} is not a valid email address.")
