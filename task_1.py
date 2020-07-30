"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""
# Немного не понял задания, и сделал два варианто соответственно
# 1) Есть циклы while, но только для проверки ввода
# 2) Полностью без while

# PS - сделал float чтобы можно было вводить дробные числа

def calc_shit_with_while():
    while True:
        operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        if operation == '0':
            return
        elif operation in '+-*/':
            break
        else:
            print('Вы ввели что-то не то :(')

    while True:
        try:
            num_one = float(input('Введите первое число: '))
        except:
            print('Вы ввели строку вместо числа')
        else:
            break

    while True:
        try:
            num_two = float(input('Введите второе число: '))
            if operation == '/' and num_two==0:
                print('Ошибка: нельзя делить на 0')
                continue
        except:
            print('Вы ввели строку вместо числа')
        else:
            break

    if operation == '+':
        print(f'{num_one} {operation} {num_two} = {num_one + num_two}')
    elif operation == '-':
        print(f'{num_one} {operation} {num_two} = {num_one - num_two}')
    elif operation == '*':
        print(f'{num_one} {operation} {num_two} = {num_one * num_two}')
    elif operation == '/':
        print(f'{num_one} {operation} {num_two} = {num_one / num_two}')
    calc_shit_with_while()


def calc_shit(operation = None, num_one = None, num_two = None):
    if operation not in ['0', '+', '-', '*', '/'] and operation!= None:
        print('Вы ввели неверную операцию')
        return calc_shit()
    elif operation == None:
        operation = input('Введите операцию (+, -, *, / или 0 для выхода): ')
        return calc_shit(operation)
    else:
        if operation == '0':
            return
    if num_one == None:
        try:
            num_one = float(input('Введите первое число: '))
        except:
            print('Вы ввели не число')
            return calc_shit(operation)

    if num_two == None:
        try:
            num_two = float(input('Введите второе число: '))
        except:
            print('Вы ввели не число')
            return calc_shit(operation, num_one)
        else:
            if num_two == 0 and operation == '/':
                print('Нельзя делить на 0')
                return calc_shit(operation, num_one)

    if operation == '+':
        print(f'{num_one} {operation} {num_two} = {num_one + num_two}\n')
    elif operation == '-':
        print(f'{num_one} {operation} {num_two} = {num_one - num_two}\n')
    elif operation == '*':
        print(f'{num_one} {operation} {num_two} = {num_one * num_two}\n')
    elif operation == '/':
        print(f'{num_one} {operation} {num_two} = {num_one / num_two}\n')

    calc_shit()

calc_shit()