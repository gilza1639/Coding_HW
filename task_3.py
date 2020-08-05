"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""
from uuid import uuid4
import hashlib

def str_finder(some_string):
    hash_data = set()
    DICT_FOR_TEST_AND_VISUALISATION = set()
    for cut_length in range(1, len(some_string)):
        for start_position in range(len(some_string)-cut_length+1):
            hash_data.add(hashlib.sha256(some_string[start_position:start_position+cut_length+1].encode()).hexdigest())
            DICT_FOR_TEST_AND_VISUALISATION.add(some_string[start_position:start_position+cut_length+1])

    print(DICT_FOR_TEST_AND_VISUALISATION)
    print(hash_data)

str_finder('papa')
print()
str_finder('Интересное_дз')