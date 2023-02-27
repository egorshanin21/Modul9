from collections import UserDict
from datetime import datetime, timedelta



class AddressBook(UserDict):
    def iterate(self, n=1):
        for key, value in self.data.items():
            d_list = list(self.data.values())
            for i in range(0, len(d_list), n):
                yield key, d_list[i:i + n]

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phone=None, email=None, birthday=None):
        self.name = name
        self.email = email
        self.birthday = birthday

        self.phones = []
        if phone:
            self.phones.append(phone)
        print(self.phones)

    def add_phone(self, phone):
        self.phones.append(phone)
        print(self.phones)

    def days_to_birthday(self):
        if self.birthday:
            now = datetime.now().date()
            bday2 = self.birthday.value.split('.')
            b = datetime(year=now.year, month=int(bday2[1]),day=int(bday2[0])).date()
            next = b - now
            if next.days < 0:
                b = datetime(year=now.year + 1, month=int(bday2[1]),
                             day=int(bday2[0])).date()
                print(b - now)
            else:
                next = b - now
                print(next)


class Field:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value


class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not value.startswith('+'):
            raise ValueError
        if len(value) != 13:
            raise ValueError


class Email(Field):
    pass


class Birthday(Field):
    @property
    def value(self):
        return self._value

    @value.setter
    def set_value(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except:
            raise ValueError


if __name__ == "__main__":

    vasia_name = Name("Vasia")
    # vasia_phone = Phone('09090909')
    vasia_phone = Phone('+380662514798')

    vasia_email = Email('lolo@gm.com')
    vasia_birthday = Birthday('21.01.1992')

    vasia1_name = Name("Vasia1")
    # vasia_phone = Phone('09090909')
    vasia1_phone = Phone('+380662514798')

    vasia1_email = Email('lolo@gm.com')
    vasia1_birthday = Birthday('21.01.1992')

    vasia2_name = Name("Vasia2")
    # vasia_phone = Phone('09090909')
    vasia2_phone = Phone('+380662514798')

    vasia2_email = Email('lolo@gm.com')
    vasia2_birthday = Birthday('21.01.1992')


    record_v = Record(vasia_name, vasia_phone, vasia_email, vasia_birthday)
    record2_v = Record(vasia1_name, vasia1_phone, vasia1_email, vasia1_birthday)
    record3_v = Record(vasia2_name, vasia2_phone, vasia2_email, vasia2_birthday)
    record_v.add_phone(Phone("+380662514798"))
    record_v.days_to_birthday()
    address_book = AddressBook()
    address_book.add_record(record_v)
    address_book.add_record(record2_v)
    address_book.add_record(record3_v)
    for record in address_book.iterate(n=3):
        print(f"LIST {record}")
