'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''

'''
попробовал реализовать так, чтобы дочернему классу передавать только нужный параметр
'''

# функция подсчета всей ткани вместе
def count_of_cloth(*args):
    amount = 0
    for el in args:
        amount += float(el.coat)
    return amount


class Clothes:
    def __init__(self, heigth=0, weight=0):
        self.height = heigth
        self.weight = weight

    def cloth_of_coat(self):
        return float(self.weight / 6.5 + 0.5)

    def cloth_of_costume(self):
        return float(self.height * 2 + 0.3)


class Coat(Clothes):
    def __init__(self, weight):
        super().__init__(weight=weight)

    @property
    def cloth_of_coat(self):
        self.coat = round(Clothes.cloth_of_coat(self), 2)
        return self.coat

    def __str__(self):
        return str(round(self.cloth_of_coat, 2))


class Costume(Clothes):
    def __init__(self, heigth):
        super().__init__(heigth=heigth)

    @property
    def cloth_of_costume(self):
        self.coat = round(Clothes.cloth_of_costume(self), 2)
        return self.coat

    def __str__(self):
        return str(round(self.cloth_of_costume, 2))


my_coat = Coat(10)
print(my_coat)
my_costume = Costume(20)
print(my_costume)
my_something = Coat(19)
print(my_something)

print(count_of_cloth(my_something, my_costume, my_coat))
