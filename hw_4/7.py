'''
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
for el in fibo_gen(). Функция отвечает за получение факториала числа, а в цикле необходимо выводить
только первые 15 чисел.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

'''
from functools import reduce

def fibo_gen(n):
    before_fact = 1
    factorial_list = [el for el in range(1, n+1)]
    for el in factorial_list:
        before_fact = before_fact * el
        if el<=15:
            yield before_fact
    if n>=16:
        yield before_fact
n = 1
for el in fibo_gen(20):
    if n <= 15:
        print (f"!{n} = ", el)
        n+=1
    else:
        print ('final factorial =', el)


