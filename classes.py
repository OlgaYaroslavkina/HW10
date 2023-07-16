from collections import UserDict


class Field:
    def __init__(self, value) -> None:
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
    def __init__(self, name: Name, phone: Phone = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"phone {phone} add to contact {self.name}"
        return f"{phone} present in phones of contact {self.name}"

    def change_phone(self, old_phone, new_phone):
        for idx, p in enumerate(self.phones):
            if old_phone.value == p.value:
                self.phones[idx] = new_phone
                return f"old phone {old_phone} change to {new_phone}"
        return f"{old_phone} not present in phones of contact {self.name}"

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]
        for idx, p in enumerate(self.phones):
            if p.value == phone.value:
                return (
                    f"Phone:{self.phones.pop(idx)} - was remove in contact {self.name}"
                )

    def __str__(self) -> str:
        phones = "; ".join(str(p) for p in self.phones) if self.phones else "not added"
        return f"Contact name - {self.name}, contact phones - {phones}"

    def __repr__(self) -> str:
        return str(self)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())
