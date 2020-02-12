'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''


class Storage:
    def __init__(self):
        Storage.storages = []
        Storage.id = 100100100

    @classmethod
    def new_storage(cls, name, location, place, temperature, guard, items=[]):
        storage = [cls.id, name, location, place, temperature, guard, items]
        cls.id += 1
        cls.storages.append(storage)
        cls.storages[-1][-1] = []

    @classmethod
    def storage_list(cls):
        for el in cls.storages:
            yield el


class Orgtechnique:
    def __init__(self, name, weight, price, amount, extra):
        self.name = name
        self.weight = weight
        self.price = price
        self.amount = amount
        self.extra = extra

    def send_to_storage(self, id_my=0):
        if id_my == 0:
            id_my = int(input('Введите id склада для отправки: '))
        dict_of_item = {
            'name': self.name,
            'weight': self.weight,
            'price': self.price,
            'amount': self.amount,
            'extra': self.extra
        }
        for id, el in enumerate(Storage.storage_list()):
            if el[0] == id_my:
                Storage.storages[id][-1].append(dict_of_item)
                break


class Printer(Orgtechnique):
    def __init__(self, name, weight, price, amount, discription, material, owntype, time_to_print):
        if type(weight) != int and type(weight) != float or type(price) != int and type(price) != float or type(amount) != int or type(time_to_print) != int and type(time_to_print) != float:
            print('один из типов данных (weight or price or amount or time_to_scan or time_to_print) не соответсвует типу int or float')
        else:
            extra = {
                'discription': discription,
                'material': material,
                'owntype': owntype,
                'time_to_print': time_to_print
            }
            super().__init__(name, weight, price, amount, extra)

    def global_send_to_storage(self, id_my=0):
        if id_my == 0:
            id_my = int(input('Введите id склада для отправки: '))
        dict_of_item = {
            'name': self.name,
            'weight': self.weight,
            'price': self.price,
            'amount': self.amount,
            'extra': self.extra
        }
        for id, el in enumerate(Storage.storage_list()):
            if el[0] == id_my:
                Storage.storages[id][-1].append(dict_of_item)
                break


class Scaner(Orgtechnique):
    def __init__(self, name, weight, price, amount, discription, material, time_to_scan):
        if type(weight) != int and type(weight) != float or type(price) != int and type(price) != float or type(amount) != int or type(time_to_scan) != int and type(time_to_scan) != float:
            print('один из типов данных (weight or price or amount or time_to_scan or ) не соответсвует типу int or float')
        else:
            extra = {
                'discription': discription,
                'material': material,
                'time_to_scan': time_to_scan
            }
            super().__init__(name, weight, price, amount, extra)

    def send_to_storage(self, id_my=0):
        if id_my == 0:
            id_my = int(input('Введите id склада для отправки: '))
        dict_of_item = {
            'name': self.name,
            'weight': self.weight,
            'price': self.price,
            'amount': self.amount,
            'extra': self.extra
        }
        for id, el in enumerate(Storage.storage_list()):
            if el[0] == id_my:
                Storage.storages[id][-1].append(dict_of_item)
                break


class Xerox(Orgtechnique):
    def __init__(self, name, weight, price, amount, discription, material, time_to_scan, time_to_print):
        if type(weight) != int and type(weight) != float or type(price) != int and type(price) != float or type(amount) != int or type(time_to_scan) != int and type(time_to_scan) != float or type(time_to_print) != int and type(time_to_print) != float:
            print('один из типов данных (weight or price or amount or time_to_scan or time_to_print) не соответсвует типу int or float')
        else:
            extra = {
                'discription': discription,
                'material': material,
                'time_to_scan': time_to_scan,
                'time_to_print': time_to_print,
                'total_time': time_to_scan + time_to_print
            }
            super().__init__(name, weight, price, amount, extra)

    def send_to_storage(self, id_my=0):
        if id_my == 0:
            id_my = int(input('Введите id склада для отправки: '))
        dict_of_item = {
            'name': self.name,
            'weight': self.weight,
            'price': self.price,
            'amount': self.amount,
            'extra': self.extra
        }
        for id, el in enumerate(Storage.storage_list()):
            if el[0] == id_my:
                Storage.storages[id][-1].append(dict_of_item)
                break


# testing

Storage()  # чтобы данные на 22 23 строках смогли работать
Storage.new_storage('На пушкина', 'Москва', 8750, 31, True)
Storage.new_storage('Ленинградская', 'Питер', 500, 25, True)
Storage.new_storage('Большая 31а', 'Хабаровск', 720.5, -20, False)
Storage.new_storage('Зона 51', '[ДАННЫЕ УДАЛЕНЫ]', 750890, 26.5, True)

for el in Storage.storage_list():
    print(el)

print('\n')
print('=' * 20)
print('\n')

# (self, name, weight, price, amount, discription, material, time_to_scan, time_to_print)


'''Можно вводить id програмно или вручную если ничего не ввел в send_to_storage()'''


Xerox('Самсунг 2201', 7.5, 25899, 250, 'Необыкновенное описание как же это круто вау', 'пластик', 3, 6).send_to_storage(100100101)
# (self, name, weight, price, amount, discription, material, time_to_scan):
Scaner('LG 1337', 2, 2500, 20, 'Необыкновенное описание как же это круто вау', 'пластик', 1).send_to_storage(100100102)
# (self, name, weight, price, amount, discription, material, owntype, time_to_print)
# чтобы показать как выглядит несколько товаров в одном здании сделал почти одинковые принтеры
Printer('Panasonic', 3, 7700, 2, 'Необыкновенное описание как же это круто вау', 'пластик', 'Черно-белый лазерный',6).send_to_storage(100100103)
Printer('Lg', 2, 2500, 100, 'Необыкновенное описание как же это круто вау', 'пластик', 'цветной', 6).send_to_storage(100100103)
Printer('Samsung', 1, 3200, 270, 'Необыкновенное описание как же это круто вау', 'пластик', 'НЕТ_ДАННЫХ',6).send_to_storage(100100103)

def informer():
    for el in Storage.storage_list():
        print('\n'+(('='*100+'\n')*3)+'\n')
        print(f'ID: \t\t\t{el[0]}')
        print(f'Storage_Name: \t{el[1]}')
        print(f'Location: \t\t{el[2]}')
        print(f'Square m^2: \t{el[3]}')
        print(f'Temp C: \t\t{el[4]}')
        print(f'Guard: \t\t\t{el[5]}')
        print('Products:')
        for elem in el[-1]:
            print('\tProduct_Name: ' + str(elem['name']))
            print('\tWeight: ' + str(elem['weight']))
            print('\tPrice: ' + str(elem['price']))
            print('\tAmount: ' + str(elem['amount']))
            print('\tExtras:')
            for key, value in elem['extra'].items():
                print(f'\t\t{key.title()}: \t{value}')
            print ('\n')

informer()
