"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from time import process_time as timer

def list_inputer(num):
    output_list = []
    for el in range(num):
        output_list.append([el, el**2])

def dict_inputer(num):
    output_list = {}
    for el in range(num):
        output_list[el] = el**2


def middle_time_calculator(func, num_of_try, num_to_test):
    list_of_try = []
    for el in range(num_of_try):
        start = timer()
        func(num_to_test)
        end = timer()
        list_of_try.append(end-start)
    return sum(list_of_try)/num_of_try

print(f'List time = {middle_time_calculator(list_inputer, 10, 10 ** 6)}')
print(f'Dict time = {middle_time_calculator(dict_inputer, 10, 10 ** 6)}')
