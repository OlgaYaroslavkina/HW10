from collections import UserDict


class Field:
    def __init__(
        self, name, phone=None, address="Ukraine", email="user@com.ua"
    ) -> None:
        self.name = name
        self.phones = []
        self.address = address
        self.email = email
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        self.phones.append(phone)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, name, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        del self.data[name]

    def edit_record(self, name, new_name):
        record = self.data[name]
        record.name.value = new_name
        self.data[new_name] = record
