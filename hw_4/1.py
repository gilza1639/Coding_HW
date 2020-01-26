from sys import argv

'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
'''



def salary ():
    try:
        script_name, work_hour, pay_for_hour, add_money = argv
        return int(work_hour) * int(pay_for_hour) + int(add_money)
    except ValueError:
        return 'Недостаточно параметров скрипта'

print(salary())






