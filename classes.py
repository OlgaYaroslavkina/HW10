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
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def remove_phone(self, phone: Phone):
        for idx, p in enumerate(self.phones):
            if p.value == phone.value:
                return self.phones.pop(idx)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        deleted_phone = self.remove_phone(old_phone)
        if deleted_phone:
            self.add_phone(new_phone)
            return f"phone {old_phone} change to phone {new_phone}"
        return f"contact {self.name} has no phone {old_phone}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
        return f"Record with name {record.name} add successful"

    # def remove_record(self, name):
    #     del self.data[name]

    # def edit_record(self, name, new_name):
    #     record = self.data[name]
    #     record.name.value = new_name
    #     self.data[new_name] = record


class BotAssistant:
    def __init__(self):
        self.address_book = AddressBook()

    def handle_command(self, command):
        command = command.lower()
        if command == "hello":
            return "How can I help you?"
        elif command.startswith("add"):
            try:
                _, name, phone = command.split()

                if name in self.address_book.data:
                    record = self.address_book.data[name]
                    record.add_phone(phone)

                else:
                    record = Record(name)
                    record.add_phone(phone)
                    self.address_book.add_record(record)

                    return f"Контакт {name} з номером {phone} успішно доданий!"
            except ValueError:
                return "Неправильний формат команди. Введіть ім'я та номер телефону через пробіл."

        elif command.startswith("change"):
            try:
                _, name, phone = command.split()

                if name in self.address_book.data:
                    record = self.address_book.data[name]
                    record.edit_phone(record.phones[0].value, phone)
                    return f"Номер телефону для контакту {name} успішно змінено на {phone}!"
                else:
                    return "Контакт не знайдено!"
            except ValueError:
                return "Неправильний формат команди. Введіть ім'я та номер телефону через пробіл."
        elif command.startswith("phone"):
            try:
                _, name = command.split()

                if name in self.address_book.data:
                    record = self.address_book.data[name]
                    phones = ", ".join([phone.value for phone in record.phones])
                    return f"Номери телефонів для контакту {name}: {phones}"
                else:
                    return "Контакт не знайдено!"
            except ValueError:
                return "Неправильний формат команди. Введіть ім'я контакту."
        elif command == "show all":
            if self.address_book.data:
                result = "Список контактів:\n"
                for name, record in self.address_book.data.items():
                    phones = ", ".join([phone.value for phone in record.phones])
                    result += f"{name}: {phones}\n"
                return result
            else:
                return "Список контактів порожній."
        elif command in ["good bye", "close", "exit"]:
            return "Good bye!"
        else:
            return "Невідома команда. Спробуйте ще раз."


def main():
    print("Вітаємо у боті-асистенті!")
    assistant = BotAssistant()
    while True:
        command = input("Введіть команду: ")
        response = assistant.handle_command(command)
        print(response)
        if response == "Good bye!":
            break


if __name__ == "__main__":
    main()
