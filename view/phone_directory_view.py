class PhoneDirectoryView:
    def __init__(self, presenter):
        self.presenter = presenter

    def display_contacts(self, contacts):
        if not contacts:
            print("No contacts found.")
        for contact in contacts:
            print(f"\nFirst Name: {contact.first_name} \nLast Name: {contact.last_name} \nPhone: {contact.phone_number} \nAddress: {contact.address} \n")

    def show_message(self, message):
        print(message)

    def user_interface(self):
        commands = {
            "add": self.add_contact,
            "list": self.list_contacts,
            "find": self.find_contact,
            "remove": self.remove_contact,
            "exit": exit
        }

        while True:
            command = input("Enter command (add, list, find, remove, exit): ").strip().lower()
            if command in commands:
                commands[command]()
            else:
                print("Unknown command. Please try again.")

    def add_contact(self):
        first_name = input("Enter first name (or type 'cancel' to cancel): ")
        if first_name.lower() == 'cancel':
            return
        last_name = input("Enter last name (or type 'cancel' to cancel): ")
        if last_name.lower() == 'cancel':
            return
        phone_number = input("Enter phone number (or type 'cancel' to cancel): ")
        if phone_number.lower() == 'cancel':
            return
        address = input("Enter address (or type 'cancel' to cancel): ")
        if address.lower() == 'cancel':
            return
        self.presenter.add_contact(first_name, last_name, phone_number, address)

    def list_contacts(self):
        self.presenter.load_contacts()

    def find_contact(self):
        search_term = input("Enter name or part of name to find: ")
        found_contacts = self.presenter.find_contact(search_term)
        print(f"Found contacts: {found_contacts}\n")

    def remove_contact(self):
        search_term = input("Enter name or part of name to remove: ")
        self.presenter.remove_contact(search_term)
