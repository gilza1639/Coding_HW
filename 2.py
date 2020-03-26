'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''

def info_func_1(name='None', surname='None', year='None', city='None', email='None', phone='None'):
    print('Имя - ' + name + ' // ', end=' ')
    print('Фамилия - ' + surname + ' //', end=' ')
    print('Год рождения - ' + year + ' //', end=' ')
    print('Город - ' + city + ' //', end=' ')
    print('email - ' + email + ' //', end=' ')
    print('Телефон - ' + phone + ' //', end=' ')


def info_func_2(name='None', surname='None', year='None', city='None', email='None', phone='None'):
    inf = ('Имя - ' + name + ' // ' + 'Фамилия - ' + surname + ' // ' + 'Год рождения - ' + year +
            ' // ' + 'Город - ' + city + ' // ' + 'email - ' + email + ' // ' + 'Телефон - ' + phone)
    return inf


