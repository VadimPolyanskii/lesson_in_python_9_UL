import random


# Создадим класс
class NumberCalculation:
    '''
    Считаем произведение и сумму чисел x и y
    '''

    # Инициализация
    def __init__(self, x, y):
        # Добавим переменные и инкапсулируем их
        self._x = random.randint(1, 15)
        self._y = random.randint(1, 10)

    # Методы
    # Произведение чисел
    def product_numbers(self):
        n1 = self._x * self._y
        return n1

    # Сумма чисел
    def sum_numbers(self):
        n2 = self._x + self._y
        return n2


if __name__ == '__main__':
    # Создадим объект-экземпляр класса
    obj = NumberCalculation(5, 5)
    print(obj)
    # Выведем объект с атрибутами класса и результирующее число
    print('--'*10)
    print('Числа:', obj._x, obj._y)
    print('Произведение чисел', obj._x, 'и', obj._y, 'равно', obj.product_numbers())
    print('Сумма чисел', obj._x, 'и', obj._y, 'равна', obj.sum_numbers())