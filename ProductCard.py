class ProductCard:
    """Класс карточки"""

    def __init__(self) -> None:
        """Конструктор класса ProductCard."""

        self.__id = None
        self.__name = None
        self.__quantity = None
        self.__state = 'в обработке'
        self.__supplier = None
        self.__manufacturer = None
        self.__price = None
        self.__location = None
        self.__category = None
        self.__description = None

    def get_id(self) -> int:
        """Геттер id товара.

        Returns:
            id: id товара.
        """

        return self.__id

    def get_name(self) -> str:
        """Геттер имени товара.

        Returns:
            name: имя товара.
        """

        return self.__name

    def get_quantity(self) -> int:
        """Геттер количества товара.

        Returns:
            quantity: Количество товара.
        """

        return self.__quantity

    def get_state(self) -> str:
        """Геттер состояния товара.

        Returns:
            state: Состояние товара.
        """

        return self.__state

    def get_supplier(self) -> str:
        """Геттер поставщика товара.

        Returns:
            supplier: Поставщик товара.
        """

        return self.__supplier

    def get_manufacturer(self) -> str:
        """Геттер производителя товара.

        Returns:
            supplier: Производитель товара.
        """

        return self.__manufacturer

    def get_price(self) -> int:
        """Геттер стоимости товара.

        Returns:
            price: Стоимость товара.
        """

        return self.__price

    def get_location(self) -> str:
        """Геттер местоположения товара.

        Returns:
            location: Местоположение товара.
        """

        return self.__location

    def get_category(self) -> str:
        """Геттер категории товара.

        Returns:
            category: Категория товара.
        """

        return self.__category

    def get_description(self) -> str:
        """Геттер описания товара.

        Returns:
            description: Описание товара.
        """

        return self.__description

    def set_id(self, id: int) -> None:
        """Сеттер id товара.

        Args:
            id: id товара
        """

        try:
            id = int(id)

            if id <= 0:
                raise ValueError("ID должен быть положительным числом")

        except ValueError:
            print("Ошибка! ID должен быть целым числом")
            
        else:
            self.__id = id
            print('✔')

    def set_name(self, name: str) -> None:
        """Сеттер имени товара.

        Args:
            name: Наименование товара.
        """

        self.__name = name
        print('✔')

    def set_quantity(self, quantity: int) -> None:
        """Сеттер количества товара.

        Args:
            quantity: Количество товара.
        """

        try:
            quantity = int(quantity)

            if quantity > 0:
                self.__quantity = quantity
                print('✔')
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_state(self, state: str) -> None:
        """Сеттер состояния товара.

        Args:
            state: Состояние товара.
        """

        state = state.lower()

        if state == "списано":
            if self.__state in ["принято к учёту", "состоит на учёте"]:
                self.__state = state
                print("Успешно списано")
            else:
                print("Товар не числится на учёте")
        else:
            self.__state = state
            print("Статус успешно изменён")

    def set_supplier(self, supplier: str) -> None:
        """Сеттер поставщика товара.

        Args:
            supplier: Поставщик товара.
        """

        self.__supplier = supplier
        print('✔')

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер производителя товара.

        Args:
            manufacturer: Производитель товара.
        """

        self.__manufacturer = manufacturer
        print('✔')

    def set_price(self, price: int) -> None:
        """Сеттер стоимости товара.

        Args:
            price: Стоимость товара.
        """

        try:
            price = int(price)

            if price > 0:
                self.__price = price
                print('✔')
            else:
                print("Введено некорректное значение!")

        except ValueError:
            print("Введено некорректное значение!")

    def set_location(self, location: str) -> None:
        """Сеттер местоположения товара.

        Args:
            location: Местоположение товара.
        """

        self.__location = location
        print('✔')

    def set_category(self, category: str) -> None:
        """Сеттер категории товара.

        Args:
            category: Категория товара.
        """

        self.__category = category
        print('✔')

    def set_description(self, description: str) -> None:
        """Сеттер описания товара.

        Args:
            description: Описание товара.
        """

        self.__description = description
        print('✔')
