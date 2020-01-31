'''
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('2_py.txt') as f_obj:
    n = 0
    z = 0
    for id, lines in enumerate(f_obj.readlines()):
        print(f'Строка №{id + 1} - {len(lines.split())} слов')
        n += 1
        z += len(lines.split())
    print(f'Всего строк - {n}, всего слов - {z}')
