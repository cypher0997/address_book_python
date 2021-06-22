class ContactPerson:

    def __init__(self, neo_cp_in_detail):
        """

        :param neo_cp_in_detail:
        """
        self.first_name = neo_cp_in_detail.get('1')
        self.last_name = neo_cp_in_detail.get('2')
        self.address = neo_cp_in_detail.get('3')
        self.city = neo_cp_in_detail.get('4')
        self.state = neo_cp_in_detail.get('5')
        self.postal_zip = neo_cp_in_detail.get('6')
        self.phone_number = neo_cp_in_detail.get('7')

    def returns_contact_person(self):
        """
        it creates a storage unit for contact person details
        :return: returns the dictionary of contact person details
        """
        creates_contact_person = {'first_name': self.first_name, 'last_name': self.last_name, 'address': self.address,
                                  'city': self.city, 'state': self.state, 'postal_zip': self.postal_zip,
                                  'phone_number': self.phone_number}

        return creates_contact_person
