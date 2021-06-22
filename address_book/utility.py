from contact_person import ContactPerson
from address_book import AddressBook


class Utility:
    def __init__(self):
        """
        setting essential attributes
        """
        self.adb = {}
        self.ab_ob = AddressBook()

    def create_address_book(self):
        """
        this method creates a address book schema
        :return: setting adb dictionary attribute as actual address book
        """
        self.adb = self.ab_ob.creates_and_returns_address_book()

    def edit_contact_person(self):
        """
        this method edits specific contact person details
        :return: returns updated address book
        """
        name_to_edit = input("enter the first name of person to be edited")
        for i in self.adb:
            if self.adb.get(i)['first_name'] == name_to_edit:
                catch_contact_person_details = self.ab_ob.retuns_input_contact_person_details()
                cp_ob = ContactPerson(catch_contact_person_details)
                self.adb.update({i: cp_ob.returns_contact_person()})

    def delete_contact_person(self):
        """
        deletes specific contact person from dictionary
        :return: returns updated address book
        """
        name_to_delete = input("enter the first name of person to be deleted")
        for i in self.adb:
            if self.adb.get(i)['first_name'] == name_to_delete:
                del self.adb[i]

    def show_address_book(self):
        """
        simply prints all contact person in addressbook
        :return: pass
        """
        for i in self.adb:
            neo_i = self.adb.get(i)
            print(" ")
            print("contact_person" + " : " + i)
            for j in neo_i:
                print(j + " : " + neo_i.get(j))
        print("its done")
