# 1 задание
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_len(self):
        return round(2 * (3.14 * self.radius))

    def get_circle_area(self):
        return 3.14 * (self.radius) ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def get_side(self):
        return self.side * 4

    def get_square_area(self):
        return 4 * self.radius ** 2


class SquareInCircle(Circle, Square):
    def __init__(self, radius, side):
        super().__init__(radius)


    def get_circle_area(self):
        return 3.14 * (self.radius) ** 2


ball = Circle(40)
print(ball.get_len())
print(ball.get_circle_area())

tetr = Square(10)
print(tetr.get_square_area())
print(tetr.get_side())

tetr_in_ball = SquareInCircle(40, 10)
print(tetr_in_ball.get_side())
print(tetr_in_ball.get_square_area())
