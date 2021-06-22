from contact_person import ContactPerson


def main():
    print("welcome to address book problem")
    cp_ob = ContactPerson('anurag', 'bhardwaj', 'achrol', 'jaipur', 'rajsathan', '303002', '6350391128')
    contact_persons = cp_ob.returns_contact_person()
    for i in contact_persons.keys():
        print(i+" : "+contact_persons.get(i))


if __name__ == '__main__':
    main()
