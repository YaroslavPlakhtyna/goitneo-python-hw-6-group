def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found, please add contact."

def show_contact(args, contacts):
    name = args[0]
    for key, value in contacts.items():
        if key == name:
            return value
    return "Contact not found, please add contact."

def show_all_contact(contacts):
    info = ""
    for name, phone in contacts.items():
        info += f'{name}: {phone}\n'
    return info

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
            print(add_contact(args, contacts))   
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()