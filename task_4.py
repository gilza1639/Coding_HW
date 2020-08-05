"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете условжнить задачу, реализовав ее через ООП
"""
from uuid import uuid4
import hashlib

def url_hasher():
    some_database = {}
    while True:
        url = input('Введите URL для проверки налиция кэша веб старницы: ')
        if some_database.get(url) == None:
            salt = uuid4().hex
            hashed_url = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
            # Добавил словарь в словарь, чтобы поместить параментр соли. Вдруг понадобится
            some_database[url]={
                                'hash' : hashed_url,
                                'salt' : salt
                                }
            print('URL добавлен в базу данных!')
            print(f'Хэш {url} - {some_database[url]["hash"]}\n')
        else:
            print(f'Хэш есть в БД: {url} - {some_database[url]["hash"]}\n')

url_hasher()