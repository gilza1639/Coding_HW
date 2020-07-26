"""
Задание 5.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""

class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)

def pal_checker(string):
    string = string.lower()
    dc_obj = DequeClass()

    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        while first == ' ':
            first = dc_obj.remove_from_front()
        if dc_obj.size() == 0:
            break
        last = dc_obj.remove_from_rear()
        while last == ' ':
            last = dc_obj.remove_from_rear()
        if dc_obj.size() == 0:
            break
        if first != last:
            still_equal = False

    return still_equal

print(pal_checker('топот'))
print(pal_checker('Топот ага ага топот'))
print(pal_checker('молоко делили ледоколом'))
print(pal_checker('а роза упала на лапу азора'))
print(pal_checker('тт'))
print(pal_checker('ттт'))
print(pal_checker('тЫт'))

# Для удобства сделал для любого регистра, чтобы ТоПоТ == топот и тд (37 строчка кода)