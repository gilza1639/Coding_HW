'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.

Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
dict_obj = {}
nums_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
with open('6_py.txt', encoding='utf-8') as f_obj:
    for line in f_obj.readlines():
        sum_of_object = 0
        string_obj_and_hour = line.split(': ')
        string_hour = string_obj_and_hour[1].split()
        for obj in string_hour:
            for num in nums_list:
                if str(num) in obj:
                    index = obj.index('(')
                    number = int(obj[:index])
                    sum_of_object += number
                    break
            dict_obj[string_obj_and_hour[0]] = sum_of_object
    print(dict_obj)

