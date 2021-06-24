import json


class Services:

    def view_person_by_city_state(self, adb):
        """
        it prints number of persons and their detail on bases of city or state input
        :param adb: address book on which operations are performed
        :return: pass
        """
        count = 0
        choice = int(input("press '1' to search by city, press '2' to search by state"))
        action = {1: 'city', 2: 'state'}
        city_or_state_to_search_in = input(" enter the name of" + action.get(choice) + " : ")
        for i in adb:
            if adb.get(i)[action.get(choice)] == city_or_state_to_search_in:
                print(adb.get(i))
                count += 1
        print("the number of contact person by city or state : " + str(count))

    def sort_persons_by_first_name_or_city_or_state(self, adb):
        """
        it sort the address book on the basis of person name or city or state the sorting
        is performed on the bases of user input
        :param adb: address book on which operations are performed
        :return: pass
        """
        choice = int(input("press '1' to search by city, press '2' to search by state"))
        action = {1: 'city', 2: 'state', 3: 'first_name'}
        temp = sorted(adb.items(), key=lambda x: x[1][action.get(choice)])
        res = dict(temp)
        for i in res:
            neo_i = res.get(i)
            print(" ")
            print("contact_person" + " : " + i)
            for j in neo_i:
                print(j + " : " + neo_i.get(j))

    def write_data_to_json(self, adb):
        """
        writes data to json file in json format
        :param adb: the date as address book to be written
        :return: pass
        """
        with open('data.json', 'w') as write_file:
            json.dump(adb, write_file, indent=4)

    def read_data_from_json(self, adb):
        """
        reads data from json file
        :param adb: not used here ...
        :return: pass
        """
        file_to_read = open('data.json', 'r')
        data = json.load(file_to_read)
        print(data)