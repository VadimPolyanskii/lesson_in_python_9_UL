# Импортируем родительский класс
from new_class import NumberCalculation


# Наследственный класс
class NaturalNumberTest(NumberCalculation):
    '''
    Проверим, являются ли результирующие числа целыми
    '''
    # Инициализация
    def __init__(self, x, y):
        super().__init__(x, y)

    # Произведение чисел
    def product_numbers(self):
        return self._x * self._y

    def number_check(self):
        d = 2
        while self._x * self._y % d != 0:
            d += 1
        return d == self._x * self._y


# Создадим объект-экемпляр
number = NaturalNumberTest(15, 16)
print()
print('Числа', number._x, number._y)
print('Призведение чисел', number._x, 'и', number._y, 'равно', number._x * number._y)
print('Является ли число', number._x * number._y, 'простым?', number.number_check())







    


