'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # самое сложное было разобраться с super(), минут 40 просидел
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')
        # or
        return (f'{self.name} {self.surname}')

    # Почему такой вариант не работает?
    #    def get_total_income(self):
    #        print (self.wage + self.bonus)
    #        # or
    #        return (self.wage + self.bonus)
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])
        # or
        return (self._income['wage'] + self._income['bonus'])

    def work(self):
        print(self.position)
        # or
        return (self.position)


somebody = Position('Shustov', 'Nikita', 'President', 20000, 750000)
somebody.get_full_name()
somebody.get_total_income()
somebody.work()
