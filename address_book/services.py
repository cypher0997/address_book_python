class Services:
    def view_person_by_city_state(self, adb):
        count = 0
        choice = int(input("press '1' to search by city, press '2' to search by state"))
        action = {1: 'city', 2: 'state'}
        city_or_state_to_search_in = input(" enter the name of" + action.get(choice) + " : ")
        for i in adb:
            if adb.get(i)[action.get(choice)] == city_or_state_to_search_in:
                print(adb.get(i))
                count += 1
        print("the number of contact person by city or state : " + str(count))

    def sort_persons_by_first_name(self, adb):
        temp = sorted(adb.items(), key=lambda x: x[1]['first_name'])
        res = dict(temp)
        for i in res:
            neo_i = res.get(i)
            print(" ")
            print("contact_person" + " : " + i)
            for j in neo_i:
                print(j + " : " + neo_i.get(j))
