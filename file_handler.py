import csv

CONTACTS_FILE = "contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(CONTACTS_FILE, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            contacts = [row for row in reader]
    except FileNotFoundError:
        pass
    return contacts

def save_contacts():
    contacts = load_contacts()
    with open(CONTACTS_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact_to_file(contact):
    contacts = load_contacts()
    contacts.append(contact)
    with open(CONTACTS_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def is_duplicate_phone(phone):
    contacts = load_contacts()
    return any(contact["phone"] == phone for contact in contacts)

def remove_contact_from_file(phone):
    contacts = load_contacts()
    updated_contacts = [contact for contact in contacts if contact["phone"] != phone]
    if len(contacts) == len(updated_contacts):
        return False

    with open(CONTACTS_FILE, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_contacts)
    return True

def search_contacts(query):
    contacts = load_contacts()
    return [contact for contact in contacts if query.lower() in contact["name"].lower() or query in contact["phone"] or query.lower() in contact["email"].lower()]