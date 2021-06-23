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
        self.adb = self.ab_ob.creates_and_returns_address_book(self.adb)
        return self.adb

    def add_contact_person(self, adb):
        count = len(adb)-1
        self.ab_ob.add_new_contacts_to_address_book(count, adb)
        

    def edit_contact_person(self, adb):
        """
        this method edits specific contact person details
        :return: returns updated address book
        """
        name_to_edit = input("enter the first name of person to be edited")
        for i in adb:
            if adb.get(i)['first_name'] == name_to_edit:
                catch_contact_person_details = self.ab_ob.retuns_input_contact_person_details()
                cp_ob = ContactPerson(catch_contact_person_details)
                adb.update({i: cp_ob.returns_contact_person()})

    def delete_contact_person(self, adb):
        """
        deletes specific contact person from dictionary
        :return: returns updated address book
        """
        name_to_delete = input("enter the first name of person to be deleted")
        for i in adb:
            if adb.get(i)['first_name'] == name_to_delete:
                del adb[i]

    def show_address_book(self, adb):
        """
        simply prints all contact person in address book
        :return: pass
        """
        for i in adb:
            neo_i = adb.get(i)
            print(" ")
            print("contact_person" + " : " + i)
            for j in neo_i:
                print(j + " : " + neo_i.get(j))
        print("its done")