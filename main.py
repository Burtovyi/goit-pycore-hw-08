import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def list_contacts(self):
        return self.contacts



def save_data(book, filename="addressbook.pkl"):
    """Зберігає адресну книгу у файл"""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Завантажує адресну книгу з файлу або створює нову, якщо файл не існує"""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()



def main():

    book = load_data()

    while True:
        print("\nАдресна книга:")
        for name, phone in book.list_contacts().items():
            print(f"{name}: {phone}")

        print("\nДоступні дії:")
        print("1. Додати контакт")
        print("2. Видалити контакт")
        print("3. Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            name = input("Введіть ім'я: ").strip()
            phone = input("Введіть номер телефону: ").strip()
            book.add_contact(name, phone)
            print(f"Контакт {name} додано.")

        elif choice == "2":
            name = input("Введіть ім'я контакту для видалення: ").strip()
            if name in book.contacts:
                book.remove_contact(name)
                print(f"Контакт {name} видалено.")
            else:
                print(f"Контакт {name} не знайдено.")

        elif choice == "3":

            save_data(book)
            print("Дані збережено. Вихід із програми.")
            break

        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
