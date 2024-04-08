import math

from .abc import Shape

type size = int | float


class Circle(Shape):
    def __init__(self, radius: size) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Triangle(Shape):
    def __init__(self, a: size, b: size, c: size) -> None:
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        # Используем формулу Герона для вычисления площади треугольника
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right_angled(self):
        # Проверка на прямоугольность треугольника
        return (
            self.a**2 + self.b**2 == self.c**2
            or self.a**2 + self.c**2 == self.b**2
            or self.b**2 + self.c**2 == self.a**2
        )


class ShapeFactory:
    def __new__(cls, *args, **kwargs):
        match len(args):
            case 1:
                return Circle(args[0])
            case 3:
                return Triangle(*args)
            case _:
                raise ValueError("Неверное количество аргументов для создания фигуры")  # noqa: E501
