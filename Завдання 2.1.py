def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter a valid command."
        except IndexError:
            return "Invalid index. Please enter a valid index."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def get_contact(args, contacts):
    name = args[0]
    return f"Phone number for {name}: {contacts.get(name, 'Contact not found')}"

@input_error
def list_contacts(args, contacts):
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

@input_error
def delete_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return f"Contact {name} deleted."
    else:
        return f"Contact {name} not found."

while True:
    command = input("Enter command (add/get/list/delete/exit): ").lower()

    if command == "exit":
        break

    if command == "add":
        try:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            result = add_contact((name, phone), contacts)
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

    elif command == "get":
        try:
            name = input("Enter name: ")
            result = get_contact((name,), contacts)
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

    elif command == "list":
        try:
            result = list_contacts((), contacts)
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

    elif command == "delete":
        try:
            name = input("Enter name: ")
            result = delete_contact((name,), contacts)
            print(result)
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Invalid command. Please enter a valid command.")
