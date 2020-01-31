'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
в новый текстовый файл.
'''
temp = {
        'one' : 'Один',
        'two' : 'Два',
        'three' : 'Три',
        'four': 'Четыре',
        'five': 'Пять',
        'six': 'Шесть',
        'seven': 'Семь',
        'eight': 'Восемь',
        'nine': 'Девять',
        'ten': 'Десять',
    }
f_obj_1 = open('original_name.txt', 'w', encoding='utf-8')
with open('4_py.txt', 'r', encoding='utf-8') as f_obj_2:
    for string in f_obj_2:
        string = string.split()
        if string == []:
            continue
        else:
            string[0] = temp[string[0].lower()]
            print(f"{string[0]} {string[1]} {string[2]}", file=f_obj_1)
f_obj_1.close()