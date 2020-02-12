'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''

class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        print('Сумма z1 и z2 равна')
        num_1_together = self.num_1 + other.num_1
        num_2_together = self.num_2 + other.num_2
        return (f'z = {num_1_together} + {num_2_together} * i')

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        #z=z1⋅z2=(a1a2−b1b2)+(a1b2+b1a2)i
        return f'{((self.num_1 * other.num_1)-(self.num_2 * other.num_2))} + {(self.num_1 * other.num_2)+(self.num_2 * other.num_1)} * i'

    def __str__(self):
        return f'z = {self.num_1} + {self.num_2} * i'


z_1 = ComplexNumber(10, 5)
z_2 = ComplexNumber(-4, 7)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)

