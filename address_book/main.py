from utility import Utility
from services import Services
from logger import returns_logger as log
from address_book_exception import AddressBookException


def main():
    """
    main execution starts here
    :return: pass
    """
    custom_log = log()
    try:
        print("welcome to address book problem")
        util_ob = Utility()
        service_ob = Services()
        neo_temp = util_ob.create_address_book(custom_log)
        while True:
            action = int(input('1 to add person, 2 editPerson, 3 print address book, 4 delete person,' +
                               '\n' + '5 to search person by city or state, 6 to sort address book' +
                               '\n' + '7 to write data to json, 8 to read data from json, 9 to quit'))
            if action == 9:
                break
            choice = {1: util_ob.add_contact_person, 2: util_ob.edit_contact_person, 3: util_ob.show_address_book,
                      4: util_ob.delete_contact_person, 5: service_ob.view_person_by_city_state,
                      6: service_ob.sort_persons_by_first_name_or_city_or_state, 7: service_ob.write_data_to_json,
                      8: service_ob.read_data_from_json}
            choice.get(action)(neo_temp, custom_log)
            print(" ")
    except Exception:
        custom_log.warning("Exception occurred from main() and handled at : ")
        raise AddressBookException


if __name__ == '__main__':
    main()
