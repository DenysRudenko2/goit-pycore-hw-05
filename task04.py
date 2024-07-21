import json
import sys


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, KeyError) as err:
            return str(err)
        except ValueError:
            match func.__name__:
                case 'add_username_phone':
                    return "Give me name and phone please."
                case 'change_username_phone':
                    return "Give me name and phone please."
                case 'phone_username':
                    return "Give me name please."
                case 'parse_input':
                    return "Available commands: hello, add, change, phone, all, close."

    return inner


@input_error
def parse_input(user_input):
    if user_input == "":
        raise ValueError("Empty input.")

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        raise KeyError(f"Contact {name} already exists.")

    contacts[name] = phone
    return "Contact added."


@input_error
def change_username_phone(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found.")


@input_error
def phone_username(args, contacts):
    [name] = args
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found.")


def all_contacts(contacts):
    return json.dumps(contacts, sort_keys=True, indent=4)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_username_phone(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print("No contacts.") if not contacts else print(all_contacts(contacts))
        else:
            print("Available commands: hello, add, change, phone, all, close.")


if __name__ == "__main__":
    main()
