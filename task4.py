def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter user name."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args            # ValueError, if args number !=2
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone = args        # ValueError, if args number !=2
    if name not in contacts:      # KeyError, if contact is not found
        raise KeyError
    contacts[name] = new_phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args[0]                # IndexError, if Name is not specified
    return contacts[name]         # KeyError, if contact is not found


@input_error
def show_all(contacts):
    return "\n".join(f"{n}: {p}" for n, p in contacts.items()) or "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        command, args = parse_input(input("Enter a command: "))

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            continue
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()