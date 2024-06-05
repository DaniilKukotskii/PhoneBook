from model.contact import Contact

class PhoneDirectoryPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_contact(self, first_name, last_name, phone_number, address):
        contact = Contact(first_name, last_name, phone_number, address)
        self.model.add_contact(contact)
        self.view.display_contacts(self.model.contacts)

    def remove_contact(self, search_term):
        contacts = self.model.find_contact(search_term)
        if contacts:
            self.model.remove_contact(contacts[0])
            self.view.display_contacts(self.model.contacts)
        else:
            self.view.show_message("Contact not found.")

    def load_contacts(self):
        self.model.load_contacts()
        self.view.display_contacts(self.model.contacts)

    def find_contact(self, search_term):
        contacts = self.model.find_contact(search_term)
        if contacts:
            self.view.display_contacts(contacts)
        else:
            self.view.show_message("Contact not found.")
