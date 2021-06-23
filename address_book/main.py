from utility import Utility


def main():
    """
    main execution starts here
    :return: pass
    """
    print("welcome to address book problem")
    util_ob = Utility()
    neo_temp = util_ob.create_address_book()
    while True:
        action = int(input('1 to add person, 2 editPerson, 3 print address book, 4 delete person, 5 quit'))
        if action == 5:
            break
        choice = {1: util_ob.add_contact_person, 2: util_ob.edit_contact_person, 3: util_ob.show_address_book,
                  4: util_ob.delete_contact_person}
        choice.get(action)(neo_temp)
        print(" ")


if __name__ == '__main__':
    main()
