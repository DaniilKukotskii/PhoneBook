import csv
from model.contact import Contact

class PhoneDirectory:
    def __init__(self, filename='contacts.csv'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def remove_contact(self, contact):
        self.contacts.remove(contact)
        self.save_contacts()

    def find_contact(self, search_term):
        search_term = search_term.lower()
        return [contact for contact in self.contacts if search_term in contact.first_name.lower() or search_term in contact.last_name.lower()
                or search_term in contact.phone_number or search_term in contact.address.lower()]

    def load_contacts(self):
        contacts = []
        try:
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if 'first_name' in row and 'last_name' in row and 'phone_number' in row and 'address' in row:
                        contacts.append(Contact.from_dict(row))
                    else:
                        print("Invalid row found in CSV:", row)
        except FileNotFoundError:
            pass  # Файл не найден, возвращаем пустой список контактов
        return contacts

    def save_contacts(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['first_name', 'last_name', 'phone_number', 'address'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
