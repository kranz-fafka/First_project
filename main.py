import datetime

print(" ")
print("To jest projekt do monitorowania wydatków")

def show_menu():
    print("=" * 10)
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Usuń wydatek")
    print("4. Wyjście")
    print("=" * 10)

def add_expense(expenses_list):
    print("Dodawanie nowego wydatku")

    while True:
        try:
            amount_input = input("Podaj kwotę: ").replace(",", ".").strip()
            amount = float(amount_input)
            break
        except ValueError:
            print("Błąd! Podaj wartość w formiacie 00.00!")

    while True:
        category = input("Wpisz kategorię: ").capitalize().strip()

        if category == "":
            category = "Inne"
            break
        if category.isalpha():
            break
        else:
            print("Błąd! Wpisz poprawną kategorię!")

    date = input("Podaj datę w formacie DD-MM-YYYY: ").strip()
    if date == "":
            date = datetime.date.today().strftime("%d-%m-%Y")

    description = input("Dodaj opis: ").strip()
    if description == "":
            description = "Brak opisu"

    new_expense = {
        "Kwota" : amount,
        "Kategoria" : category,
        "Data" : date,
        "Opis" : description
    }

    expenses_list.append(new_expense)
    print("Wydatek został pomyślnie dodany!\n")

def show_expenses(expenses_list):
    print("Wyświetlanie wszystkich wydatków\n")

    if len(expenses_list) == 0:
        print("Brak wydatków\n")
        return
    else:
        print(f"Liczba dotychczasowych wydatków: {len(expenses_list)}\n")

    for index, expense in enumerate(expenses_list, start = 1):
        date = expense["Data"]
        category = expense["Kategoria"]
        amount = expense["Kwota"]
        desc = expense["Opis"]

        print(f"Wydatek nr {index}:\n {date} | {category} | {amount} zł | {desc}")
        print("=" * 10)

def sum_expenses(expenses_list):

    total = 0

    for expense in expenses_list:
        total += expense["Kwota"]

    print(f"Suma wydatków wynosi {total} zł.")

def main():

    #Lista do przechowywania słowników z wydatkami
    expenses = []
    
    while True:
        show_menu()

        choice = input("Wybierz co chcesz zrobić: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
            sum_expenses(expenses)
        elif choice == "3":
            print("Usuwanie wydatku!")
        elif choice == "4":
            print("Zamknięcie programu\n")
            break
        else:
            print("Błędny wybór! Spróbuj ponownie")

if __name__ == "__main__":
    main()