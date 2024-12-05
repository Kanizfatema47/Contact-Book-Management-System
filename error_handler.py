import re

def validate_name(name):
    return isinstance(name, str) and name.strip() != ""

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 11

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
