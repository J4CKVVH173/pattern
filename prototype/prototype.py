from abc import abstractmethod, ABC


class Shepa(ABC):

    def __init__(self, x, y, color):
        self.X = x
        self.Y = y
        self.color = color

    @abstractmethod
    def copy(self):
        pass


class Circle(Shepa):

    def __init__(self, x, y, color, radius):
        super().__init__(x, y, color)
        self.radius = radius

    def copy(self):
        copy_circle = Circle(self.X, self.Y, self.color, self.radius)
        return copy_circle

    def show_params(self):
        print(self.X, self.Y, self.color, self.radius)


small_circle = Circle(0, 0, 'green', 5)

small_circle.show_params()

small_circle_copy = small_circle.copy()

small_circle_copy.show_params()

