class Contact:
    def __init__(self, first_name, last_name, phone_number, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
            "address": self.address
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['first_name'], data['last_name'], data['phone_number'], data['address'])
