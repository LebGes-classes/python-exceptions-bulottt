from ProductCard import (
    ProductCard,
)


class Menu:
    """Класс пользовательского меню."""

    def __init__(self) -> None:
        """Конструктор класса мeню."""

        self.__user_card = ProductCard()

    def show_info(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            "Выберите действие:\n\n"
            "1) Задать ID товара.\n"
            "2) Указать название товара.\n"
            "3) Указать количество товара.\n"
            "4) Указать поставщика.\n"
            "5) Указать производителя.\n"
            "6) Указать цену.\n"
            "7) Указать местоположение.\n"
            "8) Указать категорию.\n"
            "9) Добавить описание.\n"
            "10) Принять товар к учёту.\n"
            "11) Поставить товар на учёт.\n"
            "12) Списать товар.\n"
            "13) Посмотреть ID товара.\n"
            "14) Посмотреть название.\n"
            "15) Посмотреть количество.\n"
            "16) Посмотреть поставщика.\n"
            "17) Посмотреть производителя.\n"
            "18) Посмотреть цену.\n"
            "19) Посмотреть местоположение.\n"
            "20) Посмотреть категорию.\n"
            "21) Посмотреть описание.\n"
            "22) Посмотреть статус товара.\n"
            "23) Выход.\n\n"
        )

    def choice(self, choice: str) -> None:
        """Главное пользовательское меню.

        Args:
            choice: Выбор пользователя.
        """

        try:
            choice = int(choice)

        except ValueError:
            print("Введите число!")
            return

        else:
            if 0 < choice <= 23:
                match choice:

                    case 1:
                        self.__user_card.set_id(input("Введите ID товара: "))

                    case 2:
                        self.__user_card.set_name(input("Введите название товара: "))

                    case 3:
                        self.__user_card.set_quantity(input("Введите количество товара: "))

                    case 4:
                        self.__user_card.set_supplier(input("Введите поставщика: "))

                    case 5:
                        self.__user_card.set_manufacturer(input("Введите производителя: "))

                    case 6:
                        self.__user_card.set_price(input("Введите цену: "))

                    case 7:
                        self.__user_card.set_location(input("Введите местоположение: "))

                    case 8:
                        self.__user_card.set_category(input("Введите категорию: "))

                    case 9:
                        self.__user_card.set_description(input("Введите описание: "))

                    case 10:
                        self.__user_card.set_state("принято к учёту")

                    case 11:
                        self.__user_card.set_state("состоит на учёте")

                    case 12:
                        self.__user_card.set_state("списано")

                    case 13:
                        print(self.__user_card.get_id())

                    case 14:
                        print(self.__user_card.get_name())

                    case 15:
                        print(self.__user_card.get_quantity())

                    case 16:
                        print(self.__user_card.get_supplier())

                    case 17:
                        print(self.__user_card.get_manufacturer())

                    case 18:
                        print(self.__user_card.get_price())

                    case 19:
                        print(self.__user_card.get_location())

                    case 20:
                        print(self.__user_card.get_category())

                    case 21:
                        print(self.__user_card.get_description())

                    case 22:
                        print(self.__user_card.get_state())

                    case 23:
                        print("Выход")
            else:
                print("Нет такого пункта меню")
