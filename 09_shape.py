from abc import abstractmethod, ABC

Class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

Class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height    

rect = Rectangle(4, 5)
print(rect.area())