print("To jest projekt do monitorowania wydatków \n")

def show_menu():
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Wyjście")
    print("\n")

def main():
    
    while True:
        show_menu()

        choice = input("Wybierz co chcesz zrobić: ").strip()

        if choice == "1":
            print("Dodawanie wydatku")
        elif choice == "2":
            print("Wyświetlanie wydatków")
        elif choice == "3":
            print("Zamknięcie programu")
            break
        else:
            print("Błędny wybór! Spróbuj ponownie")

if __name__ == "__main__":
    main()