'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

import random
from time import sleep

def randome_list_gen(long, hight):
    output_list = []
    for i in range(hight):
        in_list = []
        for j in range(long):
            in_list.append(random.randint(0, 100))
        output_list.append(in_list)
    return output_list




class Matrix():
    def __init__(self, list_of_lists):
        self.my_matrix = list_of_lists


    def __str__(self):
        output = ''
        for list_el in self.my_matrix:
            for el in list_el:
                output += str(el)
                output += '\t'
            output += '\n'
        return output

    def matr_len(self):
        return [len(self.my_matrix), len(self.my_matrix[0])]

    def __add__(self, other):
        if self.matr_len() == other.matr_len():
            new_matrix = []
            for i in range (self.matr_len()[0]):
                long_matrix = []

                for j in range(self.matr_len()[1]):
                    long_matrix.append(self.my_matrix[i][j] + other.my_matrix[i][j])
                new_matrix.append(long_matrix)
            output = ''
            for list_el in new_matrix:
                for el in list_el:
                    output += str(el)
                    output += '\t'
                output += '\n'
            return [output, new_matrix]



test_1 = Matrix(randome_list_gen(4, 8))
print(test_1)
print ('-'*50)
test_2 = Matrix(randome_list_gen(4, 8))
print(test_2)
print ('-'*50)
print ('складываем')
print ('-'*50)
# если поменять [0] на [1] получим return в виде списка
print ((test_1 + test_2)[0])
