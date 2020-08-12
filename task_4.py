"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit

from collections import OrderedDict as o_dict

dict_for_test_one = {str(i):i for i in range(1000)}
dict_for_test_two = {str(i):i for i in range(100000, 101000)}

o_dict_for_test_one = o_dict(dict_for_test_one)

o_dict_for_test_two = o_dict(dict_for_test_two)

def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)]=i


def filling_o_dict(num):
    a = o_dict()
    for i in range(num):
        a[str(i)] = i

def for_every_kv_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value

def for_every_kv_o_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value

def list_sorting_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])

def list_sorting_o_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])

def popitem_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()

def popitem_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()

def get_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))

def get_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))

def update_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)

def update_o_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)





name_list = 'filling_dict filling_o_dict for_every_kv_dict for_every_kv_o_dict list_sorting_dict list_sorting_o_dict popitem_dict popitem_o_dict get_dict get_o_dict update_dict update_o_dict'.split()
# Для честноты эксперемента, если в функцию подается список, то для deque будет подаваться deque список, для list соотвественно list

num_time = 10000

for id, func_name in enumerate(name_list):
    if id%2==0:
        print()
    if id == 0 or id == 1:
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 10 :
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_for_test_one, dict_for_test_two)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 11:
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(o_dict_for_test_one, o_dict_for_test_two)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id%2==0:
            print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_for_test_one)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(o_dict_for_test_one)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")







'''
По сути своей ordereddict нужен как раз таки для сохранения очереди, поэтому сравненение в даном случае некорректно. 
Я бы конечно мог для обычного словаря создавать временные метки а потом сортировать, но обычный словарь создан не для этого

Результаты везде получились +- одинаковые, но ordereddict чуть хуже оптимизирован (особенно касательно функции update()   )


filling_dict -	3.8634573999999997
filling_o_dict -	4.7600676

for_every_kv_dict -	0.5706270999999994
for_every_kv_o_dict -	0.7622046000000005

list_sorting_dict -	1.2557707999999987
list_sorting_o_dict -	1.4108444000000002

popitem_dict -	0.0031391000000002833
popitem_o_dict -	0.0031778000000013407

get_dict -	0.0029935000000005374
get_o_dict -	0.003831800000000385

update_dict -	0.19145700000000154
update_o_dict -	0.8869313000000005


'''