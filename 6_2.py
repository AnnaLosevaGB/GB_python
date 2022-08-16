class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count(self, mass=25, thickness=5):
        return f'{self._width * self._length * mass * thickness / 1000} т'


new_road = Road(20, 5000)
print(new_road.count())
