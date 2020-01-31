'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''
import json
# чтобы добавлять компании с длинными названиями сделал отсчет от первого числа,
# то есть индексчисла минус 1 - тип собственности, а значит все что до него - название
sum_of_positive_money = [0, 0]
dict_company = {}
with open('7_py.txt', 'r', encoding='utf-8') as f_obj:
    for elem in f_obj.readlines():
        string = elem.split()
        if string == []:
            continue
        index = elem.index(string[-3])
        name_of_company = elem[:index]
        dict_company[name_of_company] = (int(string[-2]) - int(string[-1]))
        if dict_company[name_of_company] >= 0:
            sum_of_positive_money[0] += dict_company[name_of_company]
            sum_of_positive_money[1] += 1
    list_of_company = [dict_company, {"average_profit": round(sum_of_positive_money[0] / sum_of_positive_money[1], 2)}]
with open('my_file_7_py.json', 'w', encoding='utf-8') as write_f:
    json.dump(list_of_company, write_f)