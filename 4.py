'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
'''

str_number = str(input('Введите число, а я выведу самую большую цифру в числе \n   Число: '))
# Переменная для перебора цифр
n = 0
max_num = 0
while True:

    if int(str_number[n]) > max_num:
        max_num = int(str_number[n])

    if n == (len(str_number) - 1):
        break
    n += 1

print(max_num)
