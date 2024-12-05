import file_handler
import error_handler

def add():
    print("\n=== Add Contact ===")
    name = input("Enter Name: ")
    if not error_handler.validate_name(name):
        print("Invalid name. Please try again.")
        return

    phone = input("Enter Phone Number: ")
    if not error_handler.validate_phone(phone):
        print("Invalid phone number. Please try again.")
        return

    if file_handler.is_duplicate_phone(phone):
        print("Phone number already exists. Please try again.")
        return

    email = input("Enter Email: ")
    if not error_handler.validate_email(email):
        print("Invalid email. Please try again.")
        return

    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    file_handler.add_contact_to_file(contact)
    print("Contact added successfully!")