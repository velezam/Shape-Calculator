class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        string = ""
        for i in range(self.height):
            string += "*" * self.width + "\n"

        return string

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, length):
        self.height = length
        self.width = length

    def set_side(self, length):
        self.height = length
        self.width = length

    def set_width(self, length):
        self.height = length
        self.width = length

    def set_height(self, length):
        self.height = length
        self.width = length

    def __str__(self):
        return f"Square(side={self.height})"
