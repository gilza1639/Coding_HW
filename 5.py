'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с
одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
'''

my_list_dz = [7, 5, 3, 3, 3, 2]

'''
!!! Когда я в прошлый раз делал это дз, вы сказали что использовать реверс списка 
не совсем често, в этот раз попробую без него

Работает даже с float

Ps делал в виде функции для удобного тестирования, плюс полезно командой return резко прекратить работу программы
при фатальных ошибках как в строке 21-25
'''


def Rating(my_list=[]):
    if type(my_list) != list:
        print('=' * 50)
        print(f'\033[7mНа входе в функцию должен быть список (list), а не {type(my_list)}\033[0m')
        print('=' * 50)
        return 'Error'
    print(f'{"=" * 50}\nИзначальный рейтинг - {my_list}\n{"=" * 50}\n')
    while True:
        while True:
            print('\n-------- Введите число равное или больше 0 --------')
            print('----------  Или End для завершения ----------\n')
            try:
                num = input('Ввод: ')
                num = int(num)
            except ValueError:
                try:
                    num = float(num)
                except ValueError:
                    if num.lower() == 'end':
                        print('Текуший рейтинг:')
                        print(my_list)
                        return my_list
                    print('\033[31mОшибка\033[0m: вы ввели не число')
                    continue
            if num >= 0:
                break
            else:
                print('\033[31mОшибка\033[0m: введенное число меньше чем 0')
        while True:
            if len(my_list) == 0:
                my_list.append(num)
                red_num_index = 0
                break
            elif num in my_list:
                if num == min(my_list):
                    my_list.append(num)
                    red_num_index = len(my_list) - 1
                    break
                else:
                    red_num_index = (my_list.index(num)) + my_list.count(num)
                    my_list.insert((my_list.index(num)) + my_list.count(num), num)
                    break
            elif num not in my_list:
                if num > max(my_list):
                    my_list.insert(0, num)
                    red_num_index = 0
                    break
                elif num < min(my_list):
                    my_list.append(num)
                    red_num_index = len(my_list) - 1
                    break
                else:
                    # Тут усложнил, тк планирую вставить до меньшего числа, чем num
                    # Перебором делать не хочу, вдруг у нас сисок на 27 миллионов, поэтому сделаю чуть сложнее
                    n_count = 0
                    while True:
                        if num < my_list[n_count]:
                            n_count += my_list.count(my_list[n_count])
                        else:
                            my_list.insert(n_count, num)
                            red_num_index = n_count
                            break
                    break
            else:
                print(('=' * 50 + '\n') * 3 + 'UNEXPECTED ERROR' + ('=' * 50 + '\n') * 3)
        while True:
            # red_num_index нужен чтобы выделить цветом новый элемент
            # Чтобы не делать перебор вставлял интервалы списка, переводил эти интервалы в str
            # и убирал последний символ первого интервала и первый список второго
            # чтобы не было [...] red_num [...] а было [... , red_num, ...]
            if red_num_index == 0:
                if len(my_list) == 1:
                    print(f'[\033[31m{my_list[0]}\033[0m]')
                    break
                else:
                    print(f'[\033[31m{my_list[0]}\033[0m, ', end='')
                    output_back = str(my_list[1:])
                    print(output_back[1:])
                    break
            elif red_num_index == len(my_list) - 1:
                output_front = str(my_list[:(len(my_list) - 1)])
                print(f'{output_front[:len(output_front) - 1]}, ', end='')
                print(f'\033[31m{my_list[-1]}\033[0m]')
                break
            else:
                output_front = str(my_list[:red_num_index])
                output_back = str(my_list[(red_num_index + 1):])
                print(f'{output_front[:len(output_front) - 1]}, ', end='')
                print(f'\033[31m{my_list[red_num_index]}\033[0m, ', end='')
                print(output_back[1:])
                break

print ('\033[7m test 1 \033[0m')
Rating(1)

print ('\n\n\n\033[7m test 2 \033[0m')
Rating(my_list_dz)




# Старая версия


'''
print(my_list)
while True:
    while True:
        print('\n\n---------\nВведите число равное или больше 0\n---------')
        num = int(input())
        if num >= 0:
            break
    if num in my_list:
        my_list.reverse()
        my_list.insert(my_list.index(num), num)
        my_list.reverse()
    else:
        # переменная чтобы запомнить максимальное число до нашего, находящееся в списке
        before_num = 0
        for i in range(num + 1):
            if i > my_list[0]:
                my_list.insert(my_list.index(before_num), num)
                break
            if (i in my_list) and i > before_num:
                before_num = i
            if i == 0 and i == num:
                my_list.insert(len(my_list), num)
                break
            if i == num:
                my_list.insert(my_list.index(before_num), num)
                break

    print(my_list)
'''
