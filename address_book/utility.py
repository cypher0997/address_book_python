from contact_person import ContactPerson
from address_book import AddressBook
from address_book_exception import AddressBookException


# this is utility class ,holds methods for various utility functionality like create ,edit,delete,print
class Utility:
    def __init__(self):
        """
        setting essential attributes
        """
        self.adb = {}
        self.ab_ob = AddressBook()

    def create_address_book(self, rec_log):
        """
        this method creates a address book schema
        :return: setting adb dictionary attribute as actual address book
        """
        self.adb = self.ab_ob.creates_and_returns_address_book(self.adb, rec_log)
        return self.adb

    def add_contact_person(self, adb, rec_log):
        """
        it adds new contact person to address book
        :param adb: the address book where all operations are performed
        :param rec_log: custom logger
        :return: pass
        """
        count = len(adb) - 1
        self.ab_ob.add_new_contacts_to_address_book(count, adb, rec_log)

    def edit_contact_person(self, adb, rec_log):
        """
        this method edits specific contact person details
        :param adb: the address book we are working on
        :param rec_log: custom logger
        :return: returns updated address book
        """
        try:
            name_to_edit = input("enter the first name of person to be edited")
            if not name_to_edit:
                raise Exception
            for i in adb:
                if adb.get(i)['first_name'] == name_to_edit:
                    catch_contact_person_details = self.ab_ob.returns_input_contact_person_details(adb)
                    cp_ob = ContactPerson(catch_contact_person_details)
                    adb.update({i: cp_ob.returns_contact_person()})
        except Exception:
            rec_log.exception("message")
            raise AddressBookException

    def delete_contact_person(self, adb, rec_log):
        """
        deletes specific contact person from dictionary
        :param adb: the address book we are working on
        :param rec_log: custom log
        :return: returns updated address book
        """
        try:
            name_to_delete = input("enter the first name of person to be deleted")
            if not name_to_delete:
                raise Exception
            for i in adb:
                if adb.get(i)['first_name'] == name_to_delete:
                    del adb[i]
        except Exception:
            rec_log.exception("message")
            # rec_log.debug("exception occurred at edit func() at : ")
            raise AddressBookException

    def show_address_book(self, adb, rec_log=None):
        """
        simply prints all contact person in address book
        :param adb: address book we are working on
        :param rec_log: custom log
        :return: pass
        """
        for i in adb:
            neo_i = adb.get(i)
            print(" ")
            print("contact_person" + " : " + i)
            for j in neo_i:
                print(j + " : " + neo_i.get(j))
        print("its done")

