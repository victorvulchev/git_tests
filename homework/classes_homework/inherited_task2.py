class Shape():
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
class Rectangle(Shape):
    def area(self, width, height) -> None:
        product = super().__init__(width, height)
        return product
class Triangle(Shape):
    def area(self, width, height) -> None:
        product = super().__init__(width, height)
        return product / 2
class Circle():
    def __init__(self, diameter) -> None:
        self.diameter = diameter
    def area(self):
        import math
        radius = self.diameter / 2
        return math.pi * radius**2

numb_of_shapes = int(input("Enter number of shapes"))
list_of_shapes = dict()
for i in range(numb_of_shapes):
    current_shape = input("Enter shape:")
    #„Circle“, „Triangle“ и“Rectangle”
    if current_shape == "Circle":
        diameter = float(input("Enter diameter:"))
        current_obj = Circle(diameter)
        list_of_shapes[current_shape] = current_obj.area()
    elif current_shape == "Triangle":
        width = float(input("Enter width:"))
        height = float(input("Enter height:"))
        current_obj = Triangle(width, height)
        list_of_shapes[current_shape] = current_obj.area()
    else:
        width = float(input("Enter width:"))
        height = float(input("Enter height:"))
        current_obj = Rectangle(width, height)
        list_of_shapes[current_shape] = current_obj.area()
        
for key, value in list_of_shapes.items():
    print(f"{key}:{value}")
    