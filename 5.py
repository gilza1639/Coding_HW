"""
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите
рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность
сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

money_earn = int(input('Введите сумму выручку: '))
money_lost = int(input('Введите сумму издержки: '))
personal_counter = int(input('Введите число сотрудников: '))

if money_earn > money_lost:
    print('Прибыль составила', money_earn - money_lost)
    print('Рентабельность составила:', (money_earn - money_lost) / money_earn)
    print('Доход на сотрудника:', (money_earn - money_lost) / personal_counter)
elif money_earn == money_lost:
    print('Расходы равны издержкам, фирма вышла в ноль')
else:
    print('Убыток составил', money_lost-money_earn)
