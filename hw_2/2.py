'''
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
 с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().

'''


my_list = input().split()

num = len(my_list)

final_list = my_list.copy()

for id, name in enumerate(my_list):
    if num % 2 == 0 and id == num - 1:
        break
    if id % 2 == 1:
        final_list.pop(id)
        final_list.insert(id - 1, name)
print(final_list)
print(my_list)
