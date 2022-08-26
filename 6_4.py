class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} - go.')

    def stop(self):
        print(f'Car {self.name} - stop.')

    def turn(self, direction):
        print(f'Car {self.name} - turn {direction}.')

    def show_speed(self):
        print(f'Your speed {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Too fast! Your speed {self.speed}. Must be less then 60!')
        else:
            print(f'Your speed {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Too fast! Your speed {self.speed}. Must be less then 40!')
        else:
            print(f'Your speed {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police=True)


car_1 = TownCar('BMW', 'black', 100)
car_1.go()
car_1.show_speed()
print()
car_2 = TownCar('Kia', 'green', 30)
car_2.show_speed()
car_2.stop()
print()
car_3 = WorkCar('Mazda', 'red', 50)
car_3.go()
car_3.turn('left')
car_3.show_speed()
print()
car_4 = WorkCar('VW', 'white', 37)
car_4.show_speed()
car_4.stop()
print()
car_5 = SportCar('Lamborghini', 'orange', 160)
car_5.go()
car_5.turn('right')
car_5.show_speed()
print()
car_5 = PoliceCar('Ford', 'blue', 120)
car_5.go()
car_5.turn('right')
car_5.show_speed()
print(car_5.is_police)
