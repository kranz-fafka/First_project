import datetime

print("To jest projekt do monitorowania wydatków \n")

def show_menu():
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Wyjście")
    print(" ")

def add_expense(expenses_list):
    print("Dodawanie nowego wydatku")

    while True:
        try:
            amount_input = input("Podaj kwotę: ").replace(",", ".").strip()
            amount = float(amount_input)
            break
        except ValueError:
            print("Błąd! Podaj wartość w formiacie 00.00!")

    category = input("Wpisz kategorię: ").strip()
    date = input("Podaj datę w formacie DD-MM-YYYY: ").strip()
    description = input("Dodaj opis: ").strip()

    if description == "":
        description = "BRAK"
    if date == "":
        date = datetime.date.today().strftime("%d-%m-%Y")

    new_expense = {
        "Kwota" : amount,
        "Kategoria" : category,
        "Data" : date,
        "Opis" : description
    }

    expenses_list.append(new_expense)
    print("Wydatek został pomyślnie dodany!\n")

def main():

    #Lista do przechowywania słowników z wydatkami
    expenses = []
    
    while True:
        show_menu()

        choice = input("Wybierz co chcesz zrobić: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            #dodać obsługę pustej listy
            print("Wyświetlanie wydatków\n")
            if len(expenses) == 0:
                print("Brak wydatków\n")
            else:
                print(f"Liczba dotychczasowych wydatkó: {len(expenses)}")
                print(expenses)
        elif choice == "3":
            print("Zamknięcie programu\n")
            break
        else:
            print("Błędny wybór! Spróbuj ponownie")

if __name__ == "__main__":
    main()