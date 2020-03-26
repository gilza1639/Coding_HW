'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора *.
Второй — более сложная реализация без оператора *, предусматривающая использование цикла.
'''



# 1 вариант

def my_func_1(x, y):
    return x ** y


# 2 вариант

def my_func_2(x, y):
    x_on_y = x
    for i in range(abs(y) - 1):
        x_on_y = x_on_y * x
    return 1 / x_on_y


# Функция для проверки двух предыдущих функций

def test(x, y):
    print(my_func_1(x, y))
    print(my_func_2(x, y))


