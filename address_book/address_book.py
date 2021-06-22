from contact_person import ContactPerson


class AddressBook:

    def input_for_number_of_contact_person(self):
        """
        takes user input for number of contact person to  be stored
        :return: returns a specific number for contact persons to be stored
        """
        number_of_contact_person = int(input("enter the number of contact person to be stored"))
        return number_of_contact_person

    def retuns_input_contact_person_details(self):
        """
        takes user input for various details of contact person
        :return: returns tuple of details for contact person
        """
        first_name = input("enter the first name : ")
        last_name = input("enter the last name : ")
        address = input("enter the address : ")
        city = input("enter the city name : ")
        state = input("enter the state name : ")
        postal_zip = input("enter the zip code : ")
        phone_number = input("enter the phone number : ")
        cp_in_detail = (first_name, last_name, address, city, state, postal_zip, phone_number)
        return cp_in_detail

    def creates_and_returns_address_book(self):
        """
        creates actual complete form of address book
        :return: returns address book
        """
        address_book = {}
        num_cp = self.input_for_number_of_contact_person()
        for i in range(0, num_cp):
            neo_cp_in_detail = self.retuns_input_contact_person_details()
            cp_ob = ContactPerson(neo_cp_in_detail[0], neo_cp_in_detail[1], neo_cp_in_detail[2],
                                  neo_cp_in_detail[3], neo_cp_in_detail[4], neo_cp_in_detail[5],
                                  neo_cp_in_detail[6],)
            address_book.update({'contact_person_'+str(i): cp_ob.returns_contact_person()})
        return address_book

