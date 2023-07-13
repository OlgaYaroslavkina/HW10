from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return str(self)


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def __str__(self) -> str:
        phones = "; ".join(str(p) for p in self.phones) if self.phones else "not added"
        return f"Contact name - {self.name}, contact phones - {phones}"
        # phones = f"{', phones ' + '; '.join(p.replace_plus() for p in self.phones) if self.phones else ''}"
        # return "User {}, age {}{}".format(self.name, self.age, self.phones)

    def remove_phone(self, phone):
        # self.phones = [p for p in self.phones if p.value != phone]
        for idx, p in enumerate(self.phones):
            if p.value == phone.value:
                return self.phones.pop(idx)

    def edit_phone(self, old_phone, new_phone):
        deleted_phone = self.remove_phone(old_phone)
        if deleted_phone:
            self.add_phone(new_phone)
            return f"phone {old_phone} change to phone {new_phone}"
        return f"contact {self.name} has no phone {old_phone}"

    def __str__(self) -> str:
        phones = "; ".join(str(p) for p in self.phones) if self.phones else "not added"
        return f"Contact name - {self.name}, contact phones - {phones}"

    def __repr__(self) -> str:
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return f"Record with name {record.name} add successful"

    # def remove_record(self, name):
    #     del self.data[name]

    # def edit_record(self, name, new_name):
    #     record = self.data[name]
    #     record.name.value = new_name
    #     self.data[new_name] = record
