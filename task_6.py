from random import randint
"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def try_to_guess(num_of_life = 10, number = None, cheatmode = False):
    if number == None:
        number = randint(0, 100)
        if cheatmode == True:
            print(number)
    if num_of_life==0:
        print(f'Вы проиграли, жизни кончились! Загаданное число {number}')
        return
    num_of_life -= 1
    guess = int(input(f'Попытка {10-num_of_life}. Попробуйте угадать число: '))
    if guess == number:
        print(f'Вы победили! Загаданное число {number}. Количество попыток - {num_of_life}')
        return
    elif guess>number:
        print('Введенное число больше загаданного\n')
    elif guess<number:
        print('Введенное число меньше загаданного\n')
    return try_to_guess(num_of_life, number)

# чтобы честно играть - отключите cheatmode
# cheatmode=False
# или просто try_to_guess()
try_to_guess(cheatmode=True)