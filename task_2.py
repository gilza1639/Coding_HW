from random import randint
"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

def list_gen(amount):
    return [el for el in [randint(-1000, 1000) for el in range(amount)]]



def first_findmin(list_data):

    for num in list_data:
        for id, other_num in enumerate(list_data):
            if num>other_num:
                break
            elif id==len(list_data)-1:
                minnum = num
    return minnum



print(f'list num 1.1 - {[35, 12, 46, 11, 11, 25, 91, 17, 46, 777, 666]}')
print(f'minnum = {first_findmin([35, 12, 46, 11, 11, 25, 91, 17, 46, 777, 666])}')
lst_1 = list_gen(50)
print(f'list num 1.2 - {lst_1}')
print(f'minnum = {first_findmin(lst_1)}')
print('\n'*2, '*'*50, '\n'*2)



def second_findmin(list_data):
    minnum = list_data[0]
    for el in minnum[1:]:
        if el<minnum:
            minnum = el
    return minnum


print(f'list num 2.1 - {[35, 12, 46, 11, 11, 25, 91, 17, 46, 777, 666]}')
print(f'minnum = {first_findmin([35, 12, 46, 11, 11, 25, 91, 17, 46, 777, 666])}')
lst_2 = list_gen(50)
print(f'list num 2.2 - {lst_2}')
print(f'minnum = {first_findmin(lst_2)}')