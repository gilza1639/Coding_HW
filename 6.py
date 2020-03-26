'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских
букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(string):
    small_letter = 'abcdefghijklmnopqrstuvwxyz'
    big_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = string.split()
    for id, word in enumerate(string):
        s_letter = word[0]
        index = small_letter.index(s_letter)
        b_letter = big_letter[index]
        string[id] = b_letter + word[1:]
        output = ''
        for i in string:
            output += i + ' '
    return output


print(int_func('hi this is my first day in yhis fucking world'))
print(int_func('abs efe ge'))
