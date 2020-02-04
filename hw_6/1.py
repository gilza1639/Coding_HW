'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав
экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
выводить соответствующее сообщение и завершать скрипт.

'''
import time
import itertools


class TrafficLight():
    def __init__(self, color):
        self.__color = color.lower()

    def changer(self, __color_now, ):
        self.__colors = ['green', 'yellow', 'red']
        __time_and_color = [['green', 10], ['yellow', 2], ['red', 7]]
        print(__color_now)
        index = self.__colors.index(__color_now)
        for time_left in range(__time_and_color[index][1], 0, -1):
            print(time_left)
            time.sleep(1)

    def running(self):
        if self.__color == 'yellow':
            self.changer('yellow')
            self.changer('red')
        elif self.__color == 'red':
            self.changer('red')

        while True:
            for el in itertools.cycle(self.__colors):
                self.changer(el)


a = TrafficLight('yellow')
a.running()
