class ContactPerson:

    def __init__(self, first_name, last_name, address, city, state, postal_zip, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.postal_zip = postal_zip
        self.phone_number = phone_number

    def returns_contact_person(self):
        creates_contact_person = {'first_name': self.first_name, 'last_name': self.last_name, 'address': self.address,
                                  'city': self.city, 'state': self.state, 'postal_zip': self.postal_zip,
                                  'phone_number': self.phone_number}

        return creates_contact_person
