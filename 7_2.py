from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.__size = size

    def cloth(self):
        return round(self.__size / 6.5 + 0.5, 2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int) or isinstance(new_size, float):
            self.__size = new_size
        else:
            print('Size must be a number.')


class Suit(Clothes):
    def __init__(self, height):
        self.__height = height

    def cloth(self):
        return self.__height * 2 + 0.3

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if isinstance(new_height, int) or isinstance(new_height, float):
            self.__height = new_height
        else:
            print('Height must be a number.')


coat_1 = Coat(13)
print(coat_1.cloth())
suit_1 = Suit(1.6)
print(suit_1.cloth())
print(coat_1.size)
coat_1.size = 15
print(coat_1.cloth())
print(suit_1.height)
suit_1.height = 1.8
print(suit_1.cloth())
