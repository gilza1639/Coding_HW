'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class Car():
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.going = going
        self.turn = turn
        self.move = {'direction': turn, 'move': going}

    def go(self):
        self.going = True
        self.move = {'direction': self.turn, 'move': self.going}

        return 'now you move'

    def stop(self):
        self.going = False
        self.move = {'direction': self.turn, 'move': self.going}
        return 'now you stop'

    def turn(self, direction):
        self.turn = direction
        self.move = {'direction': self.turn, 'move': self.going}
        return f'now you turning to {direction}'

    def is_cop(self):
        if self.is_police == True:
            return 'thats police car'
        else:
            return 'thats not police car'

    def show_speed(self):
        return f'your speed now is {self.speed}'


'''
TownCar, SportCar, WorkCar, PoliceCar.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
'''


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):

        super().__init__(speed, color, name, is_police, going, turn)

    def show_speed(self):

        if self.speed > 60:
            return f'your speed is too high - {self.speed}'
        else:
            return f'your speed now is {self.speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):

        super().__init__(speed, color, name, is_police, going, turn)

    def show_speed(self):
        if self.speed > 40:
            return f'your speed is too high - {self.speed}'
        else:
            return f'your speed now is {self.speed}'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):

        super().__init__(speed, color, name, is_police, going, turn)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):

        super().__init__(speed, color, name, is_police, going, turn)


work_1 = WorkCar(29, 'blue', 'truck', False, True, 'east')
work_2 = WorkCar(92, 'blue', 'truck', False, True, 'east')

town_1 = TownCar(50, 'black', 'mazda', False, False)
town_2 = TownCar(120, 'black', 'mazda', False, False)
print(work_1.show_speed())
print(work_2.show_speed())
print(town_1.show_speed())
print(town_2.show_speed())

ferrari = SportCar(220, 'red', 'ferrari', False, True, 'east')
print(ferrari.speed)
print(ferrari.color)
print(ferrari.turn)
print(ferrari.going)


'''
Вопрос преподавателю, почему не работает такой вариант, когда после super и __init__ идет сначала self?
играя с принтами понял, что значения смещаются влево, то есть значеение из 
def __init__(self, speed, color, name, is_police, going=False, turn='west')
переходит в 
super().__init__(speed, color, name, is_police, going, turn)
 то есть self.speed == color //or// self.name == is_police
 
 код:
 class TownCar(Car):
    def __init__(self, speed, color, name, is_police, going=False, turn='west'):

        super().__init__(self, speed, color, name, is_police, going, turn)

    def show_speed(self):

        if self.speed > 60:
            return f'your speed is too high - {self.speed}'
        else:
            return f'your speed now is {self.speed}'


 этот код уже не рабочий, можете заменить часть моего оригинального кода и столкнуться с ошибкой
'''