
import math

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + "]"

class Shape:
    def __init__(self, type="Shape"):
        self._type = type

    def __str__(self):
        return str(self._type)


class Circle(Shape):
    def __init__(self, center, radius):
        super().__init__("Круг")
        self._center = center
        self._radius = radius

    def area(self):
        return 3.14159 * self._radius**2

    def perimeter(self):
        return 2 * 3.14159 * self._radius


class Triangle(Shape):
    def __init__(self, point1, point2, point3):
        super().__init__("Треугольник")
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3

    def area(self):
        abs(self._point1.get_x()*(self._point2.get_y() - self._point3.get_y()) + self._point2.get_x()*(self._point3.get_y() - self._point1.get_y()) + self._point3.get_x()*(self._point1.get_y() - self._point2.get_y()) ) / 2.0
        return abs(self._point1.get_x()*(self._point2.get_y() - self._point3.get_y()) 
                   + self._point2.get_x()*(self._point3.get_y() - self._point1.get_y())
                   + self._point3.get_x()*(self._point1.get_y() - self._point2.get_y())) / 2.0


    def perimeter(self):
        side1 = ((self._point2.get_x() - self._point1.get_x())**2 +
                 (self._point2.get_y() - self._point1.get_y())**2)**0.5
        side2 = ((self._point3.get_x() - self._point2.get_x())**2 +
                 (self._point3.get_y() - self._point2.get_y())**2)**0.5
        side3 = ((self._point1.get_x() - self._point3.get_x())**2 +
                 (self._point1.get_y() - self._point3.get_y())**2)**0.5
        return side1 + side2 + side3


class Rectangle(Shape):
    def __init__(self, point1, point2):
        super().__init__("Прямоугольник")
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point2.get_x() - self.point1.get_x()) *
                   (self.point2.get_y() - self.point1.get_y()))

    def perimeter(self):
        return 2 * (abs(self.point2.get_x() - self.point1.get_x()) +
                    abs(self.point2.get_y() - self.point1.get_y()))


class Square(Rectangle):
    def __init__(self, point1, point2):
        super().__init__(point1, point2)
        self._type = "Квадрат"

    def area(self):
        return abs((self.point2.get_x() - self.point1.get_x())**2)

    def perimeter(self):
        return 4 * abs(self.point2.get_x() - self.point1.get_x())


class Rhombus(Shape):
    def __init__(self, point1, point2, point3, point4):
        super().__init__("Ромб")
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3
        self._point4 = point4

    def area(self):
        diagonal1 = ((self._point2.get_x() - self._point1.get_x())**2 +
                     (self._point2.get_y() - self._point1.get_y())**2)**0.5
        diagonal2 = ((self._point4.get_x() - self._point3.get_x())**2 +
                     (self._point4.get_y() - self._point3.get_y())**2)**0.5
        return (diagonal1 * diagonal2) / 2

    def perimeter(self):
        side1 = ((self._point2.get_x() - self._point1.get_x())**2 +
                 (self._point2.get_y() - self._point1.get_y())**2)**0.5
        side2 = ((self._point3.get_x() - self._point2.get_x())**2 +
                 (self._point3.get_y() - self._point2.get_y())**2)**0.5
        side3 = ((self._point4.get_x() - self._point3.get_x())**2 +
                 (self._point4.get_y() - self._point3.get_y())**2)**0.5
        side4 = ((self._point1.get_x() - self._point4.get_x())**2 +
                 (self._point1.get_y() - self._point4.get_y())**2)**0.5
        return side1 + side2 + side3 + side4

point1 = Point(0, 0)
point2 = Point(3, 0)
point3 = Point(0, 4)
point4 = Point(2, 6)

circle = Circle(point1, 5)
triangle = Triangle(point1, point2, point3)
rectangle = Rectangle(point2, point3)
square = Square(point2, point3)
rhombus = Rhombus(point1, point2

, point3, point4)

print(circle)
print("Площадь:", circle.area())
print("Периметр:", circle.perimeter())

print(triangle)
print("Площадь:", triangle.area())
print("Периметр:", triangle.perimeter())

print(rectangle)
print("Площадь:", rectangle.area())
print("Периметр:", rectangle.perimeter())

print(square)
print("Площадь:", square.area())
print("Периметр:", square.perimeter())

print(rhombus)
print("Площадь:", rhombus.area())
print("Периметр:", rhombus.perimeter())