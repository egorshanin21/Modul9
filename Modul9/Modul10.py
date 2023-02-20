from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone = None, email = None):
        self.name = name
        self.email = email

        self.phones = []
        if phone:
            self.phones.append(phone)
        print(self.phones)

    def add_phone(self, phone):
        self.phones.append(phone)
        print(self.phones)


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Email(Field):
    pass


if __name__ == "__main__":

    vasia_name = Name("Vasia")
    vasia_phone = Phone('09090909')
    vasia_email = Email('lolo@gm.com')

    record_v = Record(vasia_name, vasia_phone, vasia_email)
    record_v.add_phone(Phone("9994949"))
    address_book = AddressBook()
    address_book.add_record(record_v)
