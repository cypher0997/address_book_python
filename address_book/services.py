class Services:
    def view_person_by_city_state(self, adb):
        choice = int(input("press '1' to search by city, press '2' to search by state"))
        action = {1: 'city', 2: 'state'}
        city_or_state_to_search_in = input(" enter the name of city or state : ")
        for i in adb:
            if adb.get(i)[action.get(choice)] == city_or_state_to_search_in:
                print(adb.get(i))
