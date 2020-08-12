"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""



#Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП (в частности по перегрузке методов)
# На мой взгляд тут нет смысла в ООП вообще, это ненужное усложнение
# без collections сложность задачи накак не меняется

import collections


# A2 c4F
def calculator_with_collection():
    print('Введите два шестнадцатеричных числа\n')
    num_one = collections.deque(input('Первое число: '))
    num_two = collections.deque(input('Второе число: '))

    beauty_num_one = ''.join(num_one)
    beauty_num_two = ''.join(num_two)

    good_num_one = int(f"0x{beauty_num_one}", 16)
    good_num_two = int(f"0x{beauty_num_two}", 16)

    hex_ans_plus = hex(good_num_one+good_num_two)
    hax_ans_mult = hex(good_num_one*good_num_two)

    print(f'{num_one} + {num_two} = {collections.deque(hex_ans_plus[2:])}')
    print(f'{num_one} * {num_two} = {collections.deque(hax_ans_mult[2:])}')

    # or

    print(f'{list(num_one)} + {list(num_two)} = {list(collections.deque(hex_ans_plus[2:]))}')
    print(f'{list(num_one)} * {list(num_two)} = {list(collections.deque(hax_ans_mult[2:]))}')

    # or

    print(f'{beauty_num_one} + {beauty_num_two} = {hex_ans_plus[2:]}')
    print(f'{beauty_num_one} * {beauty_num_two} = {hax_ans_mult[2:]}')


def calculator_without_collection():
    print('Введите два шестнадцатеричных числа\n')
    num_one = list(input('Первое число: '))
    num_two = list(input('Второе число: '))

    beauty_num_one = ''.join(num_one)
    beauty_num_two = ''.join(num_two)

    good_num_one = int(f"0x{beauty_num_one}", 16)
    good_num_two = int(f"0x{beauty_num_two}", 16)

    hex_ans_plus = hex(good_num_one + good_num_two)
    hax_ans_mult = hex(good_num_one * good_num_two)

    print(f'{list(num_one)} + {list(num_two)} = {list(collections.deque(hex_ans_plus[2:]))}')
    print(f'{list(num_one)} * {list(num_two)} = {list(collections.deque(hax_ans_mult[2:]))}')

    # or

    print(f'{beauty_num_one} + {beauty_num_two} = {hex_ans_plus[2:]}')
    print(f'{beauty_num_one} * {beauty_num_two} = {hax_ans_mult[2:]}')


calculator_without_collection()
calculator_without_collection()