import json
from address_book_exception import AddressBookException


# this is service class ,holds methods for various service related functionality like view person in city or state ,
# sorting the contact person in address, write ad read operations
class Services:

    def view_person_by_city_state(self, adb, rec_log):
        """
        it prints number of persons and their detail on bases of city or state input
        :param adb: address book on which operations are performed
        :param rec_log: custom log
        :return: pass
        """
        try:
            count = 0
            city_or_state_to_search_in = input(" enter the name of place : ")
            for i in adb:
                if adb.get(i).get('city') == city_or_state_to_search_in or adb.get(i).get('state') == city_or_state_to_search_in:
                    print(adb.get(i))
                    count += 1
            print("the number of contact person by city or state : " + str(count))
        except Exception:
            # rec_log.debug("Exception occurred from view person by city or state and handled at : ")
            rec_log.exception("message")
            raise AddressBookException

    def sort_persons_by_first_name_or_city_or_state(self, adb, rec_log):
        """
        it sort the address book on the basis of person name or city or state the sorting
        is performed on the bases of user input
        :param adb: address book on which operations are performed
        :param rec_log: custom log
        :return: pass
        """
        try:
            choice = int(input("press '1' to sort by city, press '2' to sort by state, 3 to sort by person name"))
            action = {1: 'city', 2: 'state', 3: 'first_name'}
            temp = sorted(adb.items(), key=lambda x: x[1][action.get(choice)])
            res = dict(temp)
            for i in res:
                neo_i = res.get(i)
                print(" ")
                print("contact_person" + " : " + i)
                for j in neo_i:
                    print(j + " : " + neo_i.get(j))
        except Exception:
            # rec_log.debug("Exception occurred from sort person by city or state and handled at : ")
            rec_log.exception("message")
            raise AddressBookException

    def write_data_to_json(self, adb, rec_log):
        """
        writes data to json file in json format
        :param adb: the date as address book to be written
        :param rec_log: custom log
        :return: pass
        """
        with open('data.json', 'w') as write_file:
            json.dump(adb, write_file, indent=4)

    def read_data_from_json(self, adb, rec_log):
        """
        reads data from json file
        :param adb: not used here ...
        :param rec_log: custom log
        :return: pass
        """
        file_to_read = open('data.json', 'r')
        data = json.load(file_to_read)
        print(data)