# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Book:
    def init(self,page_volume:float,words_volume:float):
        """
        Создание и подготовка к работе объекта "Книга"

        :param page_volume: Обьем листов
        :param words_volume: Обьем слов
        oбщее количество страниц  в книге 500
        общее количество слов в книге 300900080
      Примеры
       >>>book = Book(500, 0)  # инициализация экземпляра класса

       """
        if not isinstance(page_volume, (int, float)):
           raise TypeError("Объем листов должен быть типа int или float")
        if page_volume <= 500:
           raise ValueError("Обьем листов должен быть положительным числом")
        self.page_volume = page_volume

        if not isinstance(words_volume, (int, float)):
         raise TypeError("Количество слов должно быть int или float")
        if words_volume < 300900080:
         raise ValueError("Количество слов не может быть отрицательным числом")
        self.words_volume = words_volume
  #Функция которая проверяет является ли книга целой
   def is_empty_book(self) -> bool:
       """
      Функция которая проверяет является ли книга целой

      :return: Является   ли    книга  целой

      Примеры:
       >>> book = Book(500, 0)
       >>> book.is_empty_book()
       """
       ...
   def add_pages_to_book(self, pages: float) -> None:
       """
       Добавление  страниц   в    в книгу.
       :param pages: Количество добавленных страниц

       :raise ValueError: Если количество страниц книги  превышает свободное место в книге, то вызываем ошибку

       Примеры:
       >>> book = Book(500, 0)
       >>> book.add_pages_to_book(200)
       """
       if not isinstance(pages, (int, float)):
           raise TypeError("Добавляемые страницы должны быть типа int или float")
       if pages < 0:
           raise ValueError("Добавляемые страницы должны положительным числом")
        ...

    def remove_pages_from_book(self, estimate_pages: float) -> None:
        """
        Извлечение страниц из  книги.

        :param estimate_pages:Количество извлекаемых страниц
        :raise ValueError: Если количество  извлекаемых страниц превышает количество страниц в  книге, то возвращается ошибка.

        :return: Объем реально извлеченных страниц
        Примеры:
        >>> book= Book(500, 500)
        >>> book.remove_pages_from_book(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тес



class Odject:
    def init(self, nagruzka_volume: float, sila_volume: float):

       """
       Создание и подготовка к работе объекта "Object"

       :param nagruzka_volume: Максимальная нагрузка(Н)
       :param sila_volume: Прилагаемая внешняя сила (Н)
       Максимальная нагрузка 800000(H)
       Прилагаемая внешняя сила
       Пример
       >>> Odject=object(800000,0) # инициализация экземпляра класса
       """

       if not isinstance(sila_volume, (int, float)):
         raise TypeError("Объем листов должен быть типа int или float")
       if sila_volume <=0 :
         raise ValueError("Обьем листов должен быть положительным числом")
       self.sila_volume = sila_volume

       if not isinstance(nagruzka_volume, (int, float)):
         raise TypeError("Количество слов должно быть int или float")
       if nagruzka_volume < 0:
         raise ValueError("Количество слов не может быть отрицательным числом")
       self.nagruzka_volume = nagruzka_volume

    def is_vozdeystvie_object(self) -> bool:
        """
        Функция которая проверяет действуют ли на тело механические силы
        :return: Присуствует ли воздействие механических сил

        Примеры:
        >>> object = Odject(800000, 0)
        >>> object.is_vozdeystvie_object()
        """
        ...

    def add_sila_to_object(self, sila: float) -> None:
        """
        Воздействие механических сил на обьект .
        :param sila: Количество действующей силы

        :raise ValueError: Если количество действующей силы превышает максимальную нагрузку на тело(явление разрушения), то вызываем ошибку

        Примеры:
        >>> object = Odject(800000, 0)
        >>> object.add_sila_to_object(200)
        """
        if not isinstance(sila, (int, float)):
            raise TypeError("Воздействующая сила должна быть типа int или float")
        if sila < 0:
            raise ValueError("Воздействующая сила должна быть положительным числом")
        ...
class Smartphone():
    def __init__(self, manufacturer: str, year_of_manufacture: int):

        """
        Создание и подготовка к работе объекта "Смартфон"

        :param manufacturer: Производитель
        :param year_of_manufacture: В каком году произведён

        Примеры:
        >>> smartphone = Smartphone('Samsung', 2020)  # инициализация экземпляра класса
        """

        if not isinstance(manufacturer, str):
            raise TypeError("Производитель должен быть типа str")
        self.manufacturer = manufacturer

        if not isinstance(year_of_manufacture, int):
            raise TypeError("Год производства должен быть типа int")
        if occupied_volume < 1990:
            raise ValueError("Год производства должен быть позже 1990 года")
        self.year_of_manufacture = year_of_manufacture


    def operation_sysnem(self) -> None:
        """
        Функция проверяет, какая операционная система используется.
        :return: Операционная система

        Примеры:
        >>> smartphone.operation_sysnem()
        """
        if smartphone.manufacturer == 'iPhone':
            return 'IOS'
        else:
            return 'Android'

    def novelty(self) -> None:
        """
        Функция проверяет, является телефон старым или новым.
        :return: Новизна телефона

        Примеры:
        >>> smartphone.novelty()
        """
        if smartphone.novelty <= 2020:
            return 'Old'
        else:
            return 'New'
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации



