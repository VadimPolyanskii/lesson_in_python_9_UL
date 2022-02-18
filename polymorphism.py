# Импортируем родительский класс
from new_class import NumberCalculation


# Полиморфизм
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

    # Проверка числа на простоту
    def number_check(self):
        d = 2
        while self._x * self._y % d != 0:
            d += 1
        return d == self._x * self._y


class Quotient(NumberCalculation):
    '''
    Деление суммы чисел на 2 и получение частного
    '''

    # Инициализация
    def __init__(self, x, y):
        super().__init__(x, y)

    # Делим сумму
    def sum_division(self):
        return (self._x + self._y) / 2


# Создадим объекты-экземпляры
number = NaturalNumberTest(15, 16)
print()
print('Числа', number._x, 'и', number._y)
print('Призведение чисел', number._x, 'и', number._y, 'равно', number._x * number._y)
print('Является ли число', number._x * number._y, 'простым?', number.number_check())
print()
q = Quotient(2, 9)
print('Числа', q._x, 'и', q._y)
print('Сумма чисел', q._x, 'и', q._y, ', поделённая на 2, равна', q.sum_division())