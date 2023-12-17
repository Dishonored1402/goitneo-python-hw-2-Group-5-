class Field:
    def init(self, value):
        self.value = value

    def str(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def init(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Некоректний формат номера телефону")
        super().init(value)


class Record:
    def init(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                break

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def str(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"


class AddressBook:
    def init(self):
        self.data = {}

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


book = AddressBook()

while True:
        print("\nМеню:")
        print("1. Додати новий запис")
        print("2. Видалити запис")
        print("3. Редагувати запис")
        print("4. Пошук за іменем")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я: ")
            new_record = Record(name)
            book.add_record(new_record)
            print(f"Запис для {name} додано.")

        elif choice == "2":
            name = input("Введіть ім'я для видалення: ")
            book.delete(name)
            print(f"Запис для {name} видалено.")

        elif choice == "3":
            name = input("Введіть ім'я для редагування: ")
            record = book.find(name)
            if record:
                new_phone = input("Введіть новий телефон: ")
                record.add_phone(new_phone)
                print(f"Запис для {name} відредаговано.")
            else:
                print("Запис не знайдено.")

        elif choice == "4":
            name = input("Введіть ім'я для пошуку: ")
            record = book.find(name)
            if record:
                print(record)
            else:
                print("Запис не знайдено.")

        elif choice == "5":
            print("Дякую за користування!")
            break

        else:
            print("Неправильний вибір. Спробуйте ще раз.")