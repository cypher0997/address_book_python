from address_book import AddressBook


def main():
    """
    main execution starts here
    :return: prints the number of contact person on address book and their details
    """
    print("welcome to address book problem")
    address_book_ob = AddressBook()
    address_book = address_book_ob.creates_and_returns_address_book()
    for i in address_book:
        neo_i = address_book.get(i)
        print(" ")
        print("contact_person"+" : "+i)
        for j in neo_i:
            print(j+" : "+neo_i.get(j))


if __name__ == '__main__':
    main()
