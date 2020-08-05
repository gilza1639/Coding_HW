"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""

from uuid import uuid4
import hashlib
def password_hasher():
    while True:
        salt = uuid4().hex
        password = input('Введите пароль: ')
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        print(f'В базе данных хранится строка: {hashed_password}')
        try_to_pass = input('Введите пароль еще раз для проверки: ')
        if hashlib.sha256(salt.encode() + try_to_pass.encode()).hexdigest() == hashed_password:
            print('Вы ввели правильный пароль')
        else:
            print('Вы допустили ошибку')
        answer = input('\nЧтобы начать сначала введите Y\nДля выхода введите N или END\nВвод: ').lower()
        if answer == 'y':
            continue
        elif answer == 'n' or answer == 'end':
            break
        else:
            print('Вы ввели какую-то хрень, поэтому будем считать это как попытку выхода')
            break



password_hasher()
