class ContactPerson:

    def __init__(self, first_name, last_name, address, city, state, postal_zip, phone_number):
        """
        creates details for an contact_person
        :param first_name: describes first_name of contact person
        :param last_name: describes last_name of contact person
        :param address: describes address of contact person
        :param city: describes city of contact person
        :param state: describes state of contact person
        :param postal_zip: describes zip code of contact person
        :param phone_number: describes phone number of contact person
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.postal_zip = postal_zip
        self.phone_number = phone_number

    def returns_contact_person(self):
        """
        it creates a storage unit for contact person details
        :return: returns the dictionary of contact person details
        """
        creates_contact_person = {'first_name': self.first_name, 'last_name': self.last_name, 'address': self.address,
                                  'city': self.city, 'state': self.state, 'postal_zip': self.postal_zip,
                                  'phone_number': self.phone_number}

        return creates_contact_person
