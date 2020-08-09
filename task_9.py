"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
def task_9():
    row = int(input('Задайте количество строк в матрице: '))
    table = int(input('Задайте количество столбцов в матрице: '))
    all_rows = []
    for i in range(row):
        text_row = input(f'{i+1} строка: ').split()
        if len(text_row)!=table:
            print('Количество чисел не совпадает с количеством столбцов')
            return
        all_rows.append(text_row)
    new_list = []
    for el in all_rows:
        new_list.append(list(map(lambda x: int(x), el)))
    vertical_list = [[]]
    for i in range(table):
        vertical_list.append([])
        for el in new_list:
            vertical_list[-1].append(el[i])
        vertical_list[0].append(min(vertical_list[-1]))


    return vertical_list[0]

print(task_9())

'''
Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
1 строка: 36 20 42 38
2 строка: 46 27  7 33
3 строка: 13 12 47 15
[13, 12, 7, 15]

'''