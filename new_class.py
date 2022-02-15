import random


# Создадим класс
class NumberCalculation:
    '''
    Считаем произведение и сумму чисел x и y
    '''

    # Инициализирующий метод, подаём объект и атрибуты
    def __init__(self, x, y):
        # Добавим переменные и инкапсулируем их
        self._x = random.randint(100, 200)
        self._y = random.randint(10, 20)

    # Добавим методы

    # Произведение чисел
    def product_numbers(self):
        z1 = self._x * self._y
        return z1

    # Сумма чисел
    def sum_numbers(self):
        z2 = self._x + self._y
        return z2


# Создадим объект-экземпляр класса
p = NumberCalculation(100, 3)


print(p)    # Видим, что у нас есть объект-экземпляр класса NumberCalculation в модуле __main__, а также адрес объекта
# Выведем объект с атрибутами класса и результирующее число
print('--'*10)
print('Числа:', p._x, p._y)
print('Произведение чисел', p._x, 'и', p._y, 'равно:', p.product_numbers())
print('Сумма чисел', p._x, 'и', p._y, 'равна:', p.sum_numbers())
