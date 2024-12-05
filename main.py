import add_contact
import view_contacts
import delete_contact
import search_contact
import file_handler

def main_menu():
    while True:
        print("\n-----------Contact Book -------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("----------------------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact.add()
        elif choice == '2':
            view_contacts.view()
        elif choice == '3':
            search_contact.search()
        elif choice == '4':
            delete_contact.remove()
        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    file_handler.load_contacts()
    main_menu()
    file_handler.save_contacts()