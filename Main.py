from Menu import (
    Menu,
)


def run():
    """Метод запуска работы."""

    menu = Menu()
    is_running = True

    while is_running:
        menu.show_info()
        choice = input("Ваш выбор: ").strip()

        if choice == "23":
            print("Выход...")
            is_running = False
        else:
            menu.choice(choice)

run()
