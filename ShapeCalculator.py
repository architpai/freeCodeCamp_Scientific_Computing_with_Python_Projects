class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            s = ''
            for i in range(1, self.height + 1):
                s += '*' * self.width + '\n'
        return s

    def get_amount_inside(self, shape):
        width_of_shape = shape.width
        height_of_shape = shape.height
        no_due_to_width = self.width // width_of_shape
        no_due_to_height = self.height // height_of_shape
        total = no_due_to_width * no_due_to_height
        return total
    def __str__(self):
        s = f"Rectangle(width={self.width}, height={self.height})"
        s = str(s)
        return s


class Square(Rectangle):
    def __init__(self, side):
        self.set_width(side)
        self.set_height(side)

    def set_side(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        s = f"Square(side={self.width})"
        s = str(s)
        return s

rect = Rectangle(10, 3)
print(rect.get_area())
print(rect.get_perimeter())
print(rect.get_picture())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq.get_picture())
print(sq)
