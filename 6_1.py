import time


class TrafficLight:
    __color = 'red'

    def running(self):
        for i in range(10):
            self.__color = 'red'
            print(self.__color)
            time.sleep(7)
            self.__color = 'yellow'
            print(self.__color)
            time.sleep(3)
            self.__color = 'green'
            print(self.__color)
            time.sleep(12)


trf_1 = TrafficLight()
trf_1.running()
