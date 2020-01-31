'''
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

f_obj = open('original_name.txt', 'w+')
while True:
    string = input('введите что-нибудь: ')
    if string == '':
        f_obj.seek(0)
        break
    else:
        f_obj.write(string + '\n')
# добавил вывод для удобства
for line in f_obj.readlines():
    print(line)