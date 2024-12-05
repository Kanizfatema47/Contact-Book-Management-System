import file_handler

def remove():
    print("\n=== Remove Contact ===")
    phone = input("Enter the phone number of the contact to remove: ")
    if file_handler.remove_contact_from_file(phone):
        print("Contact removed successfully!")
    else:
        print("Contact not found.")