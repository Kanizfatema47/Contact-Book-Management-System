import file_handler

def view():
    print("\n=== View Contacts ===")
    contacts = file_handler.load_contacts()
    if not contacts:
        print("No contacts available.")
        return

    print("\nContacts:")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

# delete_contact.py
import file_handler

def remove():
    print("\n=== Remove Contact ===")
    phone = input("Enter the phone number of the contact to remove: ")
    if file_handler.remove_contact_from_file(phone):
        print("Contact removed successfully!")
    else:
        print("Contact not found.")
