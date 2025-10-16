import math

# Begin by establishing a base class from which the rest shall inherit.

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

# Now we go into the specific shapes, with the knowledge that they will need both area and perimeter methods.

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# For the triangle, we will need to use Herons Formula.
  
class Triangle(Shape):
    def __init__(self,):
        a = side_one
        b = side_two
        c = side_three

        def area(self):
            return math.sqrt(s * (s - a) * (s - b) * (s - c))

       math.sqrt(s * (s - a) * (s - b) * (s - c))
        

# Below are examples of using these classes and then printing the output.

c = Circle(10)
print(f"The area of your specified Circle is: {round(c.area())}, and the perimeter is: {round(c.perimeter())}")

r = Rectangle(5)
print (f"The area of your specified Retangle is: {round(r.area())}, and the perimeter is: {round(r.perimeter())}")
