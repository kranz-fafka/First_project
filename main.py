print("To jest projekt do monitorowania wydatków \n")

def show_menu():
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Wyjście")
    print(" ")

def main():

    #Lista do przechowywania słowników z wydatkami
    expenses = []
    
    while True:
        show_menu()

        choice = input("Wybierz co chcesz zrobić: ").strip()

        if choice == "1":
            print("Dodawanie wydatku\n")
        elif choice == "2":
            print("Wyświetlanie wydatków\n")
        elif choice == "3":
            print("Zamknięcie programu\n")
            break
        else:
            print("Błędny wybór! Spróbuj ponownie")

if __name__ == "__main__":
    main()