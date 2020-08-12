"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""

import collections

# у меня получился ужасный (наверное) пример использования collection здесь, просто попытался его хоть как-то использовать
# хотя понимаю как можно было сделать в разы эффективней

def task_1():
    business_dict = collections.OrderedDict()

    business_nam = int(input('Введите количество предприятий для расчета прибыли: '))
    for i in range(business_nam):
        name_of_business = input('Введите название предприятия: ')
        dirt_money_list = input('Через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ').split()
        clean_money = sum(map(int, dirt_money_list))
        business_dict[name_of_business] = clean_money


    business_list = collections.deque()
    business_list.extend(sorted(business_dict.items(), key=lambda t: t[1]))

    middle_profit = sum([el[1] for el in business_list])/len(business_list)

    good_business = collections.deque()
    bad_business = collections.deque()
    normal_business = collections.deque()
    good_business.extendleft([el[0] for el in business_list if el[1]>middle_profit])
    bad_business.extend([el[0] for el in business_list if el[1]<middle_profit])
    normal_business.extend([el[0] for el in business_list if el[1]==middle_profit])
    print(f'Средняя годовая прибыль всех предприятий: {middle_profit}\nПредприятия, с прибылью выше среднего значения: {good_business}\nПредприятия, с прибылью равной среднему значению: {normal_business}\nПредприятия, с прибылью ниже среднего значения: {bad_business}')






task_1()
















