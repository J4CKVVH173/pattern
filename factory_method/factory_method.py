import abc


class Create(abc.ABC):
    """
    Класс Create с фабричным методом. Помимо фабричного метода, данный класс может обладать бизнес логикой.
    """

    @abc.abstractmethod
    def factory_method(self):
        pass

    # класс содержит методы с дополнительной логикой
    def extra_logic(self):
        shape = self.factory_method()

        # у всех фигур есть общий интерфейс
        name = f'Shape name: {shape.name}'

        return name


# На основании базового класса, создаются классы с конкретной реализацией логики, которые возвращают
# конкретно созданную фигуру, у которых есть общий интерфейс

class CreateCircle(Create):

    def factory_method(self):
        return Circle(1)


class CreateRectangle(Create):

    def factory_method(self):
        return Rectangle(1, 2, 3, 4)

    # логика работы и у CreateCircle и CreateRectangle одна общая, и она не меняется несмотря на то что
    # работаю они с разными фигурами, это достигнута за счет единого интерфейса для обеих фигур


class Shape(abc.ABC):
    """
    Общий класс для всех фигур, объявляет что у всех классов фигур, должен быть интерфейс name, так будет
    обеспечано возможность работы  фабричного метода, нет разницы какая конкретная фигура была создана,
    у них у всех общий интерфейс.
    """

    @abc.abstractmethod
    def name(self):
        pass


class Rectangle(Shape):
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.name = 'rectangle'

    def name(self):
        return self.name


class Circle(Shape):
    def __init__(self, r):
        self.r = r
        self.name = 'circle'

    def name(self):
        return self.name

# Теперь у нас есть классы для разных фигур, но они могут спокойно использоваться в класса наследниках Create
# с одной конкретной реализацией общего интерфейса


print(CreateCircle().extra_logic())
print(CreateRectangle().extra_logic())

# Теперь можно создать один единый класс, который в зависимости от ситуации будет создавать объект CreateCircle или
# CreateRectangle, и при этом не нужно будет прописывать разную логику работы для этих дух объектов по причине
# того что у них один общий интерфейс


class SingleCreate(Create):
    # В данном классе используется подход, где созданием класса занимается фабричный метод, и дальше во всем
    # коде просто используется данная переменная. Позволит очень легко расширять и создавать новые фигуры и добавлять
    # в текущий код. Все благодаря общему интерфейсу.

    def __init__(self, shape):
        self.shape = shape

    def factory_method(self):
        if self.shape == 'rectangle':
            return Rectangle(1, 2, 3, 4)
        if self.shape == 'circle':
            return Circle(2)


print(SingleCreate('circle').extra_logic())
