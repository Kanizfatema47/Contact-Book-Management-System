import file_handler

def search():
    print("\n=== Search Contact ===")
    query = input("Enter name, phone, or email to search: ")
    results = file_handler.search_contacts(query)
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")