'''
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
'''
# Генератор рандомного списка от 0 до 30 из 100 чисел
import random
my_list = [random.randint(0, 31) for i in range(100)]
print(my_list)

def original(my_list_local):
    for el in my_list:
        if my_list_local.count(el) == 1:
            yield el

print([el for el in original(my_list)])