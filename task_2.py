"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
# использоал готовый memorize модуль
# https://pypi.org/project/memorize/
# pip install memorize

from memorize import memorize
import random
import timeit
import sys
sys.setrecursionlimit(100000)

# Введенная вами функция некорректно работает:
# recursive_reverse_1(1234567890)
#09876543210

def recursive_reverse_1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_1(number // 10)}'



@memorize()
def recursive_reverse_2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse_2(number // 10)}'



def revers_shit_1(num):
    num = str(num)
    if len(num)==1:
        return num
    else:
        last = num[-1]
        num = num[:-1]
        return last + revers_shit_1(num)



@memorize()
def revers_shit_2(num):
    num = str(num)
    if len(num)==1:
        return num
    else:
        last = num[-1]
        num = num[:-1]
        return last + revers_shit_2(num)




print(f'recursive_reverse_1 - {recursive_reverse_1(1234567890)}\nrecursive_reverse_2 - {recursive_reverse_2(1234567890)}\nrevers_shit_1 - {revers_shit_1(1234567890)}\nrevers_shit_2 - {revers_shit_2(1234567890)}\n')

def random_big_num(num):
    num_to_reverse = ''
    for el in range(num):
        num_to_reverse += random.choice('0123456789')
    return int(num_to_reverse)






func_list = 'recursive_reverse_1 recursive_reverse_2 revers_shit_1 revers_shit_2'.split()
print('\nTIMER 1 test 10 repeat\n')
for func_name in func_list:
    random_num = random_big_num(1000)
    result_list = timeit.repeat(stmt=func_name + f'({random_num})', setup=f'from __main__ import {func_name}', timer=timeit.default_timer, repeat=10, number=1)
    print(f"{func_name} -\tavg = {sum(result_list)/len(result_list)} -\t{result_list}")



print('\nTIMER 1000 test 5 repeat\n')
for func_name in func_list:
    random_num = random_big_num(1000)
    result_list = timeit.repeat(stmt=func_name + f'({random_num})', setup=f'from __main__ import {func_name}', timer=timeit.default_timer, repeat=5, number=1000)
    print(f"{func_name} -\tavg = {sum(result_list)/len(result_list)} -\t{result_list}")

'''
Аналитика: добавил memorize в вашу фукнцию, потом взял свою функию с ДЗ второго урока (стандартную и с memorize)

Чтобы вам не тестировать, мой вывод консоли:
recursive_reverse_1 - 09876543210
recursive_reverse_2 - 09876543210
revers_shit_1 - 0987654321
revers_shit_2 - 0987654321


TIMER 1 test 10 repeat

recursive_reverse_1 -	avg = 0.0025645100000000003 -	[0.0029550000000000062, 0.0025179000000000035, 0.0024383000000000044, 0.002781600000000002, 0.002492099999999997, 0.0024634999999999935, 0.0024475999999999942, 0.0024998999999999993, 0.0025040999999999952, 0.0025451000000000085]
recursive_reverse_2 -	avg = 0.00044138000000000234 -	[0.0043895999999999935, 2.1000000000048757e-06, 1.6000000000043757e-06, 1.1000000000038757e-06, 1.1000000000038757e-06, 1.000000000001e-06, 1.000000000001e-06, 1.430000000000875e-05, 1.000000000001e-06, 1.000000000001e-06]
revers_shit_1 -	avg = 0.0010552699999999999 -	[0.0010648000000000046, 0.0010012000000000076, 0.0009646000000000099, 0.00100299999999999, 0.0011367999999999934, 0.0009839000000000098, 0.0012073999999999974, 0.0012261999999999967, 0.0010161999999999949, 0.0009485999999999939]
revers_shit_2 -	avg = 0.00037276999999999867 -	[0.0037167999999999923, 2.299999999996749e-06, 1.1000000000038757e-06, 1.000000000001e-06, 1.1000000000038757e-06, 1.0999999999899979e-06, 1.0999999999899979e-06, 1.1000000000038757e-06, 1.1000000000038757e-06, 1.000000000001e-06]

TIMER 1000 test 5 repeat

recursive_reverse_1 -	avg = 2.5096608400000004 -	[2.5368724, 2.4735946, 2.5296395, 2.5171683000000007, 2.4910294000000004]
recursive_reverse_2 -	avg = 0.0016641000000003458 -	[0.004888199999999898, 0.0008921000000015056, 0.0008543999999996998, 0.0008543999999996998, 0.0008314000000009258]
revers_shit_1 -	avg = 0.8818956400000001 -	[0.8844641000000006, 0.8397864000000013, 0.8659569999999999, 0.9240100000000009, 0.8952606999999979]
revers_shit_2 -	avg = 0.0015963799999987316 -	[0.0042252999999981, 0.0010337000000006924, 0.0009322999999987758, 0.000956899999998484, 0.0008336999999976058]

'''



'''
Пока делал появилась идея для своего аналога memorize
Тот memorize что вы показывали на уроке и мой импортированный работают через словарь по типу dict[12345]=54321
А если локально для этой задачи заполнить memorize всеми вариантами чисел от 0 до 9999999999 (То есть все варианты десяти чисел, это 10**10 вариантов)
А потом брать наше число для реверса, скажем 123455432167676767 и извлекать по 10 символов за раз (в нашем случае 1234554321), брать заранее заготовленное
значение из словаря на это число, это число, которое мы зареверсили добавлять в строку, и затем повторять пока не кончится число, которое нужно перевернуть

Это ведь самый эффективнй вариант. После первой работы, которая конечно займет не особо мало времени, все будет выполняться очень быстро
Быстрее будет только '12345'[::-1], но это уже не реверс

Если я прав или нет по этому поводу, напишите в комментарий к дз

///////

Спустя пару тестов с записью понял, что это очень медленно. Для записи использовал 
import shelve
'''

