'''
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.

Хотел занести список в входные данные скрипта, но получалось только str, поэтому забил
Есть есть возможность, напишите, пожалуйста, как
'''
from sys import argv
from itertools import count, cycle

my_list = [54, 'Hello', True, 1, 'World', 30]

script_name, end_num = argv


n = 0
for el in cycle(my_list):
    if n == int(end_num):
        break
    else:
        print(el)
        n+=1
