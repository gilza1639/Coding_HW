"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from pysize import get_size
from pympler import asizeof



from collections import deque as deque, OrderedDict as o_dict
import random


list_with_range = [el for el in range(10000)]
deque_with_range = deque()
deque_with_range.extendleft(list_with_range)
print(f'list_with_range - {get_size(list_with_range)}')
print(f'deque_with_range - {get_size(deque_with_range)}\n')



list_with_range_random = [random.randint(1, 100) for el in range(10000)]
deque_with_range_random = deque()
deque_with_range_random.extend(list_with_range)
print(f'list_with_range_random - {get_size(list_with_range_random)}')
print(f'deque_with_range_random - {get_size(deque_with_range_random)}\n')

left_list_with_range_random = [random.randint(1, 100) for el in range(10000)]
left_deque_with_range_random = deque()
left_deque_with_range_random.extendleft(list_with_range)
print(f'left_list_with_range_random - {get_size(left_list_with_range_random)}')
print(f'left_deque_with_range_random - {get_size(left_deque_with_range_random)}\n')

# ключи уникальные, но значения повторяются многократно
simple_dict = {int(el):random.randint(1, 10) for el in range(10000)}
simple_o_dict = o_dict()
simple_o_dict = {int(el):random.randint(1, 10) for el in range(10000)}

print(f'simple_dict - {get_size(simple_dict)}')
print(f'simple_o_dict - {get_size(simple_o_dict)}\n')

not_simple_dict = {int(el):random.randint(1, 100000) for el in range(10000)}
not_simple_o_dict = o_dict()
not_simple_o_dict = {int(el):random.randint(1, 100000) for el in range(10000)}

print(f'not_simple_dict - {get_size(not_simple_dict)}')
print(f'not_simple_o_dict - {get_size(not_simple_o_dict)}\n')




'''

list_with_range - 183806
deque_with_range - 181494
list_with_range_random - 45208
deque_with_range_random - 181494
simple_dict - 303890
simple_o_dict - 303890
not_simple_dict - 456954
not_simple_o_dict - 457116

Сделал сначала задание номер 2, потом приступил к этому, поэтому для меня это неожиданно

Неожиданный вывод: deque не оптимизирует списки
'''




