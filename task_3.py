from random import randint
import operator
"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

company_names_list = 'Amazon Microsoft Apple Google Yandex Netflix Yahoo YouTube Intsagram VK GeekBrains'.split()

# **********************************************************
# first vault // list with list // 4n + 1 не считая создания бд и вывода
# **********************************************************

list_with_list_of_companys_profit = [[company_names_list[el], randint(100, 75000)] for el in range(len(company_names_list))]
print(f'first vault - {list_with_list_of_companys_profit}')

leaders_companies = []
for i in range(3):
    leader_money = 0
    for id, el in enumerate(list_with_list_of_companys_profit):
        if el in leaders_companies:
            pass
        else:
            if el[1]>leader_money:
                leader_money = el[1]
                company_id = id
    leaders_companies.append(list_with_list_of_companys_profit[company_id])


for el in leaders_companies:
    print(el)
print()




# **********************************************************
# second vault // text // n + 3*(5n+1)
# **********************************************************

text_of_companys_profit = ''
for el in company_names_list:
    text_of_companys_profit+=f'{el} '
    text_of_companys_profit+=f'{randint(100, 75000)} '
print(f'second vault - {text_of_companys_profit}')

full_company_list = text_of_companys_profit.split()
company_lists = full_company_list[1::2]
max_profit_ids = []
for i in range(3):
    max_profit = 0
    for id, el in enumerate(company_lists):
        if id in max_profit_ids:
            continue
        if int(el)>max_profit:
            max_profit = int(el)
            max_id = id
    max_profit_ids.append(max_id)


for el in max_profit_ids:
    print(f'{full_company_list[el*2]} {int(full_company_list[el*2+1])}')
print()


# **********************************************************
# third vault // list with list // без понятия как считать лямбда функию, но на глаз от 2n до n^2
# **********************************************************

list_with_list_of_companys_profit_V2 = [[company_names_list[el], randint(100, 75000)] for el in range(len(company_names_list))]
print(f'third vault - {list_with_list_of_companys_profit_V2}')

list_with_list_of_companys_profit_V2.sort(key=lambda i: i[1], reverse=True)
for el in list_with_list_of_companys_profit_V2[0:3]:
    print(el)



'''
Вывод - если последний (третий) вариант не квадратичен, то он самый лаконичный и эффективный, и причем самый понятный для читателя кода



'''
