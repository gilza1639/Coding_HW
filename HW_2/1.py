'''
1. Создать список и заполнить его элементами различных типов данных.+Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type()
для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

my_list = ['Hello', 345, 12.5, True, [0, 1, 2], (0, 1, 2), None, {1, 2, 3}, {'name': 'Mike'}, range(10), complex(1, 10)]
for i in my_list:
    print (type(i))