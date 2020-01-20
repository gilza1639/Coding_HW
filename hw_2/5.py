'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 3, 2]

print(my_list)
while True:
    while True:
        print('\n\n---------\nВведите число равное или больше 0\n---------')
        num = int(input())
        if num >= 0:
            break
    if num in my_list:
        my_list.reverse()
        my_list.insert(my_list.index(num), num)
        my_list.reverse()
    else:
        # переменная чтобы запомнить максимальное число до нашего, находящееся в списке
        before_num = 0
        for i in range(num + 1):
            if i > my_list[0]:
                my_list.insert(my_list.index(before_num), num)
                break
            if (i in my_list) and i > before_num:
                before_num = i
            if i == 0 and i == num:
                my_list.insert(len(my_list), num)
                break
            if i == num:
                my_list.insert(my_list.index(before_num), num)
                break

    print(my_list)
