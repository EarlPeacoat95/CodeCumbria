# Import the math library so we can use Pi etc...

import math

# Start by establishing a basic base class from which the child classes shall inherit.

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
    def __init__(self, a, b, c):
      self.a = a
      self.b = b
      self.c = c
         
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
       
        

# Below are examples of using these classes and then printing the output.

c = Circle(10)
print(f"The area of your specified Circle is: {round(c.area())}, and the perimeter is: {round(c.perimeter())}")

r = Rectangle(5,10)
print (f"The area of your specified Rectangle is: {round(r.area())}, and the perimeter is: {round(r.perimeter())}")

t = Triangle(20, 15, 30)
print(f"The area of your specified Triangle is: {round(t.area())}, and the perimeter is: {round(t.perimeter())}")