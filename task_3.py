"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import timeit
import cProfile
import random
import sys
sys.setrecursionlimit(100000)


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def random_big_num(num):
    num_to_reverse = ''
    for el in range(num):
        num_to_reverse += random.choice('0123456789')
    return int(num_to_reverse)

def main(num):
    revers(num)
    revers_2(num)
    revers_3(num)

big_num_to_test = random_big_num(1000)

cProfile.run('main(big_num_to_test)')


func_list = 'revers revers_2 revers_3'.split()
print('\nTIMER\n')
for func_name in func_list:
    print(f"{func_name} -\t{timeit.repeat(stmt=func_name + f'({big_num_to_test})', setup=f'from __main__ import {func_name}', timer=timeit.default_timer, repeat=3, number=100)}")



'''
По Cprofile и timeit получается
Быстрый - revers_3
Средний - revers_2
Медленный - revers
'''

'''
вывод консоли


         1007 function calls (7 primitive calls) in 0.005 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
   1001/1    0.003    0.000    0.003    0.003 task_3.py:20(revers)
        1    0.002    0.002    0.002    0.002 task_3.py:30(revers_2)
        1    0.000    0.000    0.000    0.000 task_3.py:38(revers_3)
        1    0.000    0.000    0.005    0.005 task_3.py:50(main)
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



TIMER

revers -	[0.23854910000000001, 0.2534963, 0.2600882]
revers_2 -	[0.2508340000000001, 0.2203276999999999, 0.22409690000000015]
revers_3 -	[0.00666840000000013, 0.00651159999999984, 0.006433299999999864]

'''




