"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

import timeit


'''
[2, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523]
'''

def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    if i == 0:
        return 1
    else:
        return n


def eratosfen(count_number):
    simple_num_list = [2, 3, 5]
    while len(simple_num_list) < count_number:
        start_num = simple_num_list[-1] + 2
        while True:
            if all(start_num % el != 0 for el in simple_num_list):
                break
            else:
                start_num+=2
        simple_num_list.append(start_num)
    return simple_num_list[count_number-1]



def eratosfen_try_to_optimized(count_number):
    simple_num_list = [2, 3, 5]
    start_num = simple_num_list[-1]
    num_to_optimize = 0
    while len(simple_num_list) < count_number:

        while True:
            if num_to_optimize%3==2 or num_to_optimize%5==0 or (num_to_optimize-1)%7==0:
                if len(simple_num_list) == 3 and (num_to_optimize-1)%7==0:
                    break
                num_to_optimize+=1
                start_num+=2
            elif all(start_num % el != 0 for el in simple_num_list):
                break
            else:
                num_to_optimize +=1
                start_num+=2
        simple_num_list.append(start_num)
    return simple_num_list[count_number-1]



def tester(num_list):
    a = [simple(el) for el in range(1, num_list+1)]
    print(a)
    b = [eratosfen(el) for el in range(1, num_list+1)]
    print(b)
    c = [eratosfen_try_to_optimized(el) for el in range(1, num_list+1)]
    print(c)

tester(100)



func_list = 'simple eratosfen eratosfen_try_to_optimized'.split()
print('\nTIMER\n')
for func_name in func_list:
    for el in [10, 100, 1000]:
        print(f"{func_name}; {el} number -\t{timeit.timeit(stmt=func_name + f'({el})', setup=f'from __main__ import {func_name}', number=10)}")
    print()

'''
Оптимизировать эретосфена не получилось, первый вариант все-таки быстрее

Алгоритм переписывать не стал, сделал немного по-своему, но по тому же принципу
'''


'''
Консоль:

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

TIMER

simple; 10 number -	0.00019839999999998748
simple; 100 number -	0.025571599999999972
simple; 1000 number -	6.3028138

eratosfen; 10 number -	0.0001100999999996688
eratosfen; 100 number -	0.005564700000000755
eratosfen; 1000 number -	0.5338248999999999

eratosfen_try_to_optimized; 10 number -	0.00015300000000006975
eratosfen_try_to_optimized; 100 number -	0.009272300000000122
eratosfen_try_to_optimized; 1000 number -	1.0642809999999994


'''