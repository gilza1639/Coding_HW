'''
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
'''
from sys import argv
from itertools import count, cycle

script_name, start_num = argv
for el in count(int(start_num)):
    if el >= int(start_num) + 30:
        break
    else:
        print(el)
