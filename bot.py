from classes import Name, Phone, Record, AddressBook

addressbook = AddressBook()

# contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено!"
        except ValueError:
            return "Неправильний формат вводу!"
        except IndexError:
            return "Неправильний формат команди!"

    return wrapper


@input_error
def add_contact(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    return addressbook.add_record(rec)
    # contacts[name] = phone
    # return f"Контакт {name} з номером {phone} успішно доданий!"


@input_error
def change_contact(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    if name in addressbook.data:
        addressbook.data[name].edit_phone(phone)
        return f"Номер телефону для контакту {name} успішно змінено на {phone}!"
    else:
        raise KeyError


@input_error
def phone_command(*args):
    name = Name(args[0])
    if name in addressbook.data:
        return f"Номер телефону для контакту {name}: {addressbook.data[name].phones[0]}"
    else:
        raise KeyError


def show_all_contacts():
    if addressbook.data:
        result = "Список контактів:\n"
        for name, phone in addressbook.data.items():
            result += f"{name}: {Record.phones[0]}\n"
        return result
    else:
        return "Список контактів порожній."


def hello_command(*args):
    return "How can I help you?"


def exit_command(*args):
    return "Good bye!"


COMMANDS = {
    hello_command: ["hello"],
    add_contact: ["add"],
    change_contact: ["change"],
    phone_command: ["phone"],
    show_all_contacts: ["show all"],
    exit_command: ["good bye", "close", "exit"],
}


@input_error
def handle_command(command):
    for cmd, keywords in COMMANDS.items():
        for keyword in keywords:
            if command.lower().startswith(keyword):
                return cmd(*command.lower().replace(keyword, "").strip().split())
    return "Невідома команда. Спробуйте ще раз."


def main():
    print("Вітаємо у боті-асистенті!")

    while True:
        command = input("Введіть команду: ")
        response = handle_command(command)
        print(response)
        if isinstance(response, str) and response == "Good bye!":
            break


if __name__ == "__main__":
    main()
