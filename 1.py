'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def my_func(num_1, num_2):
    try:
        num_1 / num_2
    except ZeroDivisionError:
        print('Деление на 0 невозможно')
        return
    except TypeError:
        print('Неправильный тип данных')
        return
    return num_1 / num_2


print(my_func(450, 666))

