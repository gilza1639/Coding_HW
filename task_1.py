"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


'''
Делал по алгоритму https://habr.com/ru/post/144200/ тк подробно описан алгоритм
Если сравнивать с их данными и моими, то получается разная кодировка одинаковой длинны

Пример разных кодов:

мой код для beep boop beer!
{'b': '00', 'e': '01', 'o': '100', ' ': '101', 'p': '110', '!': '1110', 'r': '1111'}
их код для beep boop beer!
'b'	00
'e'	11
'p'	101
' '	011
'o'	010
'r'	1000
'!'	1001

Как я понял тут главное - длинна значения, тк от этого зависит общий вес текста, поэтому не замарачивался на счет последовательности

Также по длинне сверялся с этим сайтом, тк тут наглядная визуализации, если что-то пошло не так https://people.ok.ubc.ca/ylucet/DS/Huffman.html

Код полностью самописный, на примеры не смотрел. Сделал через функцию, так на мой взглядпроще и компактней
Сделал перевод в двоичный код по ключам и расшифровку

справка по коду если возникнут вопросы:
haffman_copmress - переводит изначальный текст в дерево хаффмана, сделано через list.
haff_code_dict - переводит haffman_copmress в словарь буква:код
coder - из текста и haff_code_dict создает двоичный код
decoder - из закодированного с помощью code текста и haff_code_dict выводит изначальный текст. Если ввести значение debug=True будет показан процесс формирования текста
tester - Все вышеперечисленное вместе.
'''


from collections import Counter


def haffman_copmress(some_text):
    letter_list = list(Counter(some_text).most_common())
    letter_list.reverse()

    while True:
        if len(letter_list) == 1:
            break
        for id, el in enumerate(letter_list[1:]):
            if el[1] >= letter_list[id][1]:
                letter_list.append([[[letter_list[id][0], 0], [letter_list[id + 1][0], 1]], letter_list[id][1] + letter_list[id + 1][1]])
                letter_list = sorted(letter_list[2:], key=lambda x: x[1])

                break
    return letter_list[0][0]


def haff_code_dict(input_list, curret_coding=''):

    dict_with_coding = {}
    if type(input_list[-1]) == type(1):
        curret_coding += str(input_list[-1])
    for el in input_list:
        if type(el)==type([]):
            returned_dict = haff_code_dict(el, curret_coding)
            dict_with_coding.update(returned_dict)
        elif type(el)==type(1):
            pass
        else:
            dict_with_coding[el] = curret_coding
    return dict_with_coding







def coder(input_text, dict_with_code):
    output_text = ''
    for el in input_text:
        output_text += dict_with_code[el]
    return output_text


def decoder(code, dict_with_code, debug=False):
    reversed_dict = {v:k for k,v in dict_with_code.items()}
    if debug == True:
        print(reversed_dict)
    output_text = ''
    while True:
        if debug == True:
            print(output_text)
        if len(code)==0:
            break
        else:

            for id, el in enumerate(code):
                if id == 0:
                    if el in reversed_dict.keys():
                        output_text += reversed_dict[el]
                        code.pop(0)
                        break
                else:
                    if id == len(code)-1:
                        output_text += reversed_dict[code]
                        code = ''
                        break
                    else:
                        if code[:id+1] in reversed_dict.keys():
                            output_text += reversed_dict[code[:id+1]]
                            code = code[id+1:]
                            break
    return output_text



def tester(text_to_code, decod_mode = False):

    list_with_code = haffman_copmress(text_to_code)
    dict_with_code = haff_code_dict(list_with_code)
    print(text_to_code)
    print(Counter(text_to_code).most_common())
    print(dict_with_code)
    code = coder(text_to_code, dict_with_code)
    print(f'ENCODED /// {code}')
    decode = decoder(code, dict_with_code, debug=decod_mode)
    print(f'DECODED /// {decode}')
    print()


tester('beep boop beer!')
tester('Hello world of Python! I miss you since our last meeting! Its nice to see you!')

print('====================================================================================================\n'*10)


tester('beep boop beer!', decod_mode=True)
tester('Hello world of Python! I miss you since our last meeting! Its nice to see you!', decod_mode=True)



'''
Комментарий: строчки с ===== отделяют код с пометкой decod_mode=True. 
сам же decod_mode=True влияет на decoder(debug=True), он показывает процесс формирования текста декодером




beep boop beer!
[('e', 4), ('b', 3), ('p', 2), (' ', 2), ('o', 2), ('r', 1), ('!', 1)]
{'b': '00', 'e': '01', 'o': '100', ' ': '101', 'p': '110', '!': '1110', 'r': '1111'}
ENCODED /// 0001011101010010010011010100010111111110
DECODED /// beep boop beer!

Hello world of Python! I miss you since our last meeting! Its nice to see you!
[(' ', 15), ('o', 8), ('e', 7), ('s', 6), ('t', 5), ('l', 4), ('n', 4), ('i', 4), ('y', 3), ('!', 3), ('u', 3), ('r', 2), ('I', 2), ('m', 2), ('c', 2), ('H', 1), ('w', 1), ('d', 1), ('f', 1), ('P', 1), ('h', 1), ('a', 1), ('g', 1)]
{'y': '0000', 'i': '0001', 'o': '001', 'n': '0100', 'l': '0101', 'c': '01100', 'm': '01101', 'I': '01110', 'r': '01111', 'g': '100000', 'a': '100001', 'h': '100010', 'P': '100011', 'f': '100100', 'd': '100101', 'w': '100110', 'H': '100111', 't': '1010', 's': '1011', 'u': '11000', '!': '11001', 'e': '1101', ' ': '111'}
ENCODED /// 1001111101010101010011111001100010111101011001011110011001001111000110000101010001000101001100111101110111011010001101110111110000001110001111011000101000110011011110011100001111111010110000110111010111011011101110110100001010010000011001111011101010101111101000001011001101111101000111110111101110111100000011100011001
DECODED /// Hello world of Python! I miss you since our last meeting! Its nice to see you!

====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================
====================================================================================================

beep boop beer!
[('e', 4), ('b', 3), ('p', 2), (' ', 2), ('o', 2), ('r', 1), ('!', 1)]
{'b': '00', 'e': '01', 'o': '100', ' ': '101', 'p': '110', '!': '1110', 'r': '1111'}
ENCODED /// 0001011101010010010011010100010111111110
{'00': 'b', '01': 'e', '100': 'o', '101': ' ', '110': 'p', '1110': '!', '1111': 'r'}

b
be
bee
beep
beep 
beep b
beep bo
beep boo
beep boop
beep boop 
beep boop b
beep boop be
beep boop bee
beep boop beer
beep boop beer!
DECODED /// beep boop beer!

Hello world of Python! I miss you since our last meeting! Its nice to see you!
[(' ', 15), ('o', 8), ('e', 7), ('s', 6), ('t', 5), ('l', 4), ('n', 4), ('i', 4), ('y', 3), ('!', 3), ('u', 3), ('r', 2), ('I', 2), ('m', 2), ('c', 2), ('H', 1), ('w', 1), ('d', 1), ('f', 1), ('P', 1), ('h', 1), ('a', 1), ('g', 1)]
{'y': '0000', 'i': '0001', 'o': '001', 'n': '0100', 'l': '0101', 'c': '01100', 'm': '01101', 'I': '01110', 'r': '01111', 'g': '100000', 'a': '100001', 'h': '100010', 'P': '100011', 'f': '100100', 'd': '100101', 'w': '100110', 'H': '100111', 't': '1010', 's': '1011', 'u': '11000', '!': '11001', 'e': '1101', ' ': '111'}
ENCODED /// 1001111101010101010011111001100010111101011001011110011001001111000110000101010001000101001100111101110111011010001101110111110000001110001111011000101000110011011110011100001111111010110000110111010111011011101110110100001010010000011001111011101010101111101000001011001101111101000111110111101110111100000011100011001
{'0000': 'y', '0001': 'i', '001': 'o', '0100': 'n', '0101': 'l', '01100': 'c', '01101': 'm', '01110': 'I', '01111': 'r', '100000': 'g', '100001': 'a', '100010': 'h', '100011': 'P', '100100': 'f', '100101': 'd', '100110': 'w', '100111': 'H', '1010': 't', '1011': 's', '11000': 'u', '11001': '!', '1101': 'e', '111': ' '}

H
He
Hel
Hell
Hello
Hello 
Hello w
Hello wo
Hello wor
Hello worl
Hello world
Hello world 
Hello world o
Hello world of
Hello world of 
Hello world of P
Hello world of Py
Hello world of Pyt
Hello world of Pyth
Hello world of Pytho
Hello world of Python
Hello world of Python!
Hello world of Python! 
Hello world of Python! I
Hello world of Python! I 
Hello world of Python! I m
Hello world of Python! I mi
Hello world of Python! I mis
Hello world of Python! I miss
Hello world of Python! I miss 
Hello world of Python! I miss y
Hello world of Python! I miss yo
Hello world of Python! I miss you
Hello world of Python! I miss you 
Hello world of Python! I miss you s
Hello world of Python! I miss you si
Hello world of Python! I miss you sin
Hello world of Python! I miss you sinc
Hello world of Python! I miss you since
Hello world of Python! I miss you since 
Hello world of Python! I miss you since o
Hello world of Python! I miss you since ou
Hello world of Python! I miss you since our
Hello world of Python! I miss you since our 
Hello world of Python! I miss you since our l
Hello world of Python! I miss you since our la
Hello world of Python! I miss you since our las
Hello world of Python! I miss you since our last
Hello world of Python! I miss you since our last 
Hello world of Python! I miss you since our last m
Hello world of Python! I miss you since our last me
Hello world of Python! I miss you since our last mee
Hello world of Python! I miss you since our last meet
Hello world of Python! I miss you since our last meeti
Hello world of Python! I miss you since our last meetin
Hello world of Python! I miss you since our last meeting
Hello world of Python! I miss you since our last meeting!
Hello world of Python! I miss you since our last meeting! 
Hello world of Python! I miss you since our last meeting! I
Hello world of Python! I miss you since our last meeting! It
Hello world of Python! I miss you since our last meeting! Its
Hello world of Python! I miss you since our last meeting! Its 
Hello world of Python! I miss you since our last meeting! Its n
Hello world of Python! I miss you since our last meeting! Its ni
Hello world of Python! I miss you since our last meeting! Its nic
Hello world of Python! I miss you since our last meeting! Its nice
Hello world of Python! I miss you since our last meeting! Its nice 
Hello world of Python! I miss you since our last meeting! Its nice t
Hello world of Python! I miss you since our last meeting! Its nice to
Hello world of Python! I miss you since our last meeting! Its nice to 
Hello world of Python! I miss you since our last meeting! Its nice to s
Hello world of Python! I miss you since our last meeting! Its nice to se
Hello world of Python! I miss you since our last meeting! Its nice to see
Hello world of Python! I miss you since our last meeting! Its nice to see 
Hello world of Python! I miss you since our last meeting! Its nice to see y
Hello world of Python! I miss you since our last meeting! Its nice to see yo
Hello world of Python! I miss you since our last meeting! Its nice to see you
Hello world of Python! I miss you since our last meeting! Its nice to see you!
DECODED /// Hello world of Python! I miss you since our last meeting! Its nice to see you!



'''