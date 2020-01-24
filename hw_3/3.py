'''
3. Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших двух аргументов.

Если я правильно понял, то сумму мы можем сделать либо с помощью int / float, либо сложить все символы str
С листом париться не стал тк если в листе десять вложений, будет трудоемко посчитать где всетаки больше и добраться
-----------------------------------
Спустя время поставил себе задачу написать решение. Необходимо было создать вторую функцию для подсчета
всех элементов внутри list, tuple, set, froznset и во внутренних вложениях

единственное, что вызывает ошибку - это чтото на подобие
 print(list_counter([1, 2, 3,{0, 1, 4, 81, 64, 9, 16, 49,(5, 4, 3, 2, 1), {100, 1, 2, 3, 4}, 25, 36}, [1, 5,1, 9, [1, 2, 3, (5, 7, 8)]]]))
TypeError: unhashable type: 'set'

print(list_counter([1, 2, 3,{0, 1, 4, 81, 64, 9, 16, 49,(5, 4, 3, 2, 1), [100, 1, 2, 3, 4], 25, 36}, [1, 5,1, 9, [1, 2, 3, (5, 7, 8)]]]))
TypeError: unhashable type: 'list'

когда внутрь set кладешь что угодно кроме str /int / float

наешл на одном из сайтов <<В set не могут находиться изменяемые елементы(list например), так что значение>>

функция list_counter вроде как называется реверсивной

Единственное на что забил - считать количество слов/букв и складывать их.

'''


def list_counter(my_list):
    count = 0
    if type(my_list) == int:
        return my_list
    for i in my_list:
        if type(i) == int or type(i) == float:
            count += i
        elif type(i) == list or type(i) == tuple or type(i) == set or type(i) == frozenset:
            check = list_counter(i)
            if check == None:
                return None
            else:
                count += check
        else:
            return None
    return count


def my_func(num_1, num_2, num_3):
    my_list = [num_1, num_2, num_3]
    if type(num_1) == type(num_2) == type(num_3) == int or type(num_1) == type(num_2) == type(num_3) == float:
        my_list.sort()
        return my_list[-1] + my_list[-2]
    elif type(num_1) == type(num_2) == type(num_3) == str:
        biggest_str = [['', 0], ['', 0], ['', 0]]
        for id, num in enumerate(my_list):
            if id == 2 and biggest_str[0][1] > biggest_str[1][1] and len(num) > biggest_str[1][1]:
                biggest_str[1][0] = num
                return biggest_str[0][0] + biggest_str[1][0]
            elif id == 2 and biggest_str[0][1] < biggest_str[1][1] and len(num) > biggest_str[0][1]:
                biggest_str[0][0] = num
                return biggest_str[0][0] + biggest_str[1][0]
            biggest_str[id][0] = num
            biggest_str[id][1] = len(num)
        return biggest_str[0][0] + biggest_str[1][0]
    elif type(num_1) == list or type(num_1) == list or type(num_1) == list:
        if type(num_1) == str or type(num_1) == str or type(num_1) == str:
            return None
        else:
            count_num_1 = list_counter(my_list[0])
            count_num_2 = list_counter(my_list[1])
            count_num_3 = list_counter(my_list[2])
            all_counter = [count_num_1, count_num_2, count_num_3]
            all_counter = sum(all_counter) - min(all_counter)
            return all_counter


# примеры num_(1,2,3) и их данные
x_1 = [1, 2, 3, 4, 5, 6, {5, 4, 3}, (1, 2, 3), [1, 2, 3, (1, 2, 3, {1, 5555, 1})]]
# 5607
x_2 = [538, 700, 21]
# 1259
x_3 = 1500
# 1500

print(my_func(x_1, x_2, x_3))
print(my_func('ivan', 'petya', 'valera'))
# None - если разные типы данных или str находится в листе/кортеже/set
print(my_func(1, 'petya', 2))
