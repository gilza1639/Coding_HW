'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open('3_py.txt', 'r', encoding='utf-8') as f_obj:
    total_money = [0, 0]
    names_less_20 = []
    for line in f_obj.readlines():
        line = line.split()
        line[1] = float(line[1])
        if line[1] < 20000:
            names_less_20.append(line[0])
        total_money[0] += 1
        total_money[1] += line[1]
    if len(names_less_20) > 0:
        print('Зарплату менее 20000 получают:')
        for name in names_less_20:
            print(name)
        print('-' * 50)
    print(
        f'Число сотрудников - {total_money[0]}\nОбщая зарплата - {total_money[1]}\nСредняя зарплата - {(total_money[1] / total_money[0]):.2f}')
