'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
'''

class Road():
    def __init__(self, length, width, mass=25, height=5):
        self._length = length
        self._width = width
        self._mass = mass
        self._height = height/100

    def mass_of_road(self):
        _total_mass = self._length * self._width * self._mass * self._height
        print (f'{_total_mass} кг')
        if _total_mass>=1000:
            print ('или')
            print(f'{_total_mass/1000} тонн')



my_road_1 = Road(100, 8)
my_road_1.mass_of_road()

