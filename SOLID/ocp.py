# wrong
from abc import ABC, abstractmethod


class Square():
  def __init__(self, radius):
    self.radius = radius

class Circle():
  def __init__(self, side):
    self.side = side

class SquareCalculation():
  def __init__(self, shapes):
    self.shapes = shapes

  def square_shapes(self):
    if isinstance(self.shapes, Square):
      return (3.14 * self.shapes.radius * self.shapes.radius)
    elif isinstance(self.shapes, Circle):
      return (self.shapes.side * self.shapes.side)
    # and more if 

# solution
# Move square_shapes in our class 
# Add metaclass
# Rewrite  SquareCalculation

class Figure(ABC):
    @abstractmethod
    def square_shapes():
      pass

class SquareValid(Figure):
  def __init__(self, radius):
    self.radius = radius
  
  def square_shapes(self):
    return (3.14 * self.radius * self.radius)

class CircleValid(Figure):
  def __init__(self, side):
    self.side = side

  def square_shapes(self):
    return (self.side * self.side)


class SquareCalculationValid():
  def __init__(self, shapes):
    self.shapes = shapes

  def square_shapes(self):
    return self.shapes.square_shapes()
    # and more if 


square = SquareValid(3)
circle = CircleValid(4)

print(SquareCalculationValid(square).square_shapes())
print(SquareCalculationValid(circle).square_shapes())