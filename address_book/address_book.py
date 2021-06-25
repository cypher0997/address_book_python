from contact_person import ContactPerson
from address_book_exception import AddressBookException


# this is an address book class , all the operation responsible for creating address book with proper structure
class AddressBook:

    def input_for_number_of_contact_person(self):
        """
        takes user input for number of contact person to  be stored
        :return: returns a specific number for contact persons to be stored
        """
        try:
            number_of_contact_person = int(input("enter the number of contact person to be stored"))
            return number_of_contact_person
        except Exception:
            raise AddressBookException

    def check_return_first_name(self, ck_f_name, take_new_neo_rec_log):
        try:
            self.checked_first_name = input("enter the first name : ")
            if len(ck_f_name) == 0:
                return self.checked_first_name
            for i in ck_f_name:
                if ck_f_name.get(i)['first_name'] == self.checked_first_name:
                    print("name already taken, enter another name")
                    self.check_return_first_name(ck_f_name)
            return self.checked_first_name
        except Exception:
            # take_new_neo_rec_log.debug("Exception occurred from check first name and handled at : ")
            take_new_neo_rec_log.exception("message")
            raise AddressBook

    def returns_input_contact_person_details(self, ck_f_name, new_neo_rec_log):
        """
        takes user input for various details of contact person
        :return: returns tuple of details for contact person
        """
        try:
            first_name = self.check_return_first_name(ck_f_name, new_neo_rec_log)
            last_name = input("enter the last name : ")
            address = input("enter the address : ")
            city = input("enter the city name : ")
            state = input("enter the state name : ")
            postal_zip = input("enter the zip code : ")
            phone_number = input("enter the phone number : ")
            print(" ")
            cp_in_detail = {
                '1': first_name, '2': last_name, '3': address, '4': city, '5': state, '6': postal_zip, '7': phone_number
            }
            return cp_in_detail
        except Exception:
            new_neo_rec_log.exception("message")
            raise AddressBookException

    def creates_and_returns_address_book(self, rec_adb, neo_rec_log):
        """
        creates actual complete form of address book
        :param rec_adb:
        :param neo_rec_log: custom log
        :return: returns address book
        """
        address_book = {}
        num_cp = self.input_for_number_of_contact_person()
        for i in range(0, num_cp):
            neo_cp_in_detail = self.returns_input_contact_person_details(rec_adb, neo_rec_log)
            cp_ob = ContactPerson(neo_cp_in_detail)
            address_book.update({'contact_person_' + str(i): cp_ob.returns_contact_person()})
        return address_book

    def add_new_contacts_to_address_book(self, start, take, neo_rec_log):
        num_cp = self.input_for_number_of_contact_person()
        for i in range(0, num_cp):
            start += 1
            neo_cp_in_detail = self.returns_input_contact_person_details(take, neo_rec_log)
            cp_ob = ContactPerson(neo_cp_in_detail)
            take.update({'contact_person_' + str(start): cp_ob.returns_contact_person()})
        return
