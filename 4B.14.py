import re


def is_valid_email(email):
    email_pattern = r'^\S+@\S+\.\S+$'
    match = re.match(email_pattern, email)
    return match is not None


email = input("Enter an email address: ")

if is_valid_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
