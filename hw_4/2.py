'''
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''

def generator(my_list):
    for el in my_list:
        try:
            if el>max_num:
                max_num = el
                yield max_num
        except UnboundLocalError:
            max_num = el


print([nums for nums in generator([1, 4, 5, 2, 7, 3, 4, 54, 23, 74, 34, 12, 1, 23, 98, 34, 2, 1, 44])])
