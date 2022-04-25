# problem 

from cmath import cos, sin
from enum import Enum


class CoordinateSystem(Enum):
  CARTESIAN = 1
  POLAR = 2

class PointProblem:
  def __init__(self, a, b, system = CoordinateSystem.CARTESIAN):
    if system == CoordinateSystem.CARTESIAN:
      self.x = a
      self.y = b
    elif system == CoordinateSystem.POLAR:
      self.x = a * cos(b)
      self.y = a * sin(b)

# solution

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return f'x: {self.x}, y: {self.y}'

  @staticmethod
  def new_catesian_point(x, y):
    return Point(x, y)
  
  @staticmethod
  def new_polar_point(rho, theta):
    return Point(rho * cos(theta), rho * sin(theta))

  class Factory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

p = Point(1, 2)
p2 = Point.new_polar_point(1, 2)
print(p2)


# take out factory methods to a separate class
class PointFactory:
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), rho * cos(theta))

p3 = PointFactory.new_polar_point(1, 2)
p4 = Point.Factory.new_polar_point(1, 2)