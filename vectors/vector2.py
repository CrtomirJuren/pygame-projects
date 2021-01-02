# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:24:42 2020

@author: crtom

vector class from the book game development with pygame

Vectors describe: magnitude and direction.
"""
import math

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
    
    # create vector from two points
    """These class methods are called from the class
    and not an instance of the class"""
    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0] - P1[0], P2[1] - P1[1] )

    # pitagora for distance calculation
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )
    
    """Unit vectors always have a length of 1,
    are often used to represent a heading. When we move into the third dimension,
    essential for everything from collision detection to lighting.
    """
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude

    # Addition: rhs stands for Right Hand Side
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)

    # Substraction: substracting means going in the opposite direction
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)

    # Negation
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    # Multiplication by scalar
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):
        return self.__mul__(scalar)   # commutative operation
    
    # Division by scalar
    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)
    
    # check for equal
    def __eq__(self, other):
        if isinstance (other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other
    
    # greater or equal
    def __ge__(self, other):
        if isinstance (other, self.__class__):
            return self.x >= other.x and self.y >= other.y
        return self.x >= other and self.y >= other
    
    def get_value(self):
        return (self.x, self.y)
#-----------------------------------------------------------------------------
def test_function_v1():

    # create vectors
    vector_a = Vector2(1, 1)
    vector_b = Vector2(0, 0)
    
    print(vector_a)
    print(vector_a.x, vector_a.y)
    
    # test_create_vector_from_two_points
    A = (10.0, 20.0)
    B = (30.0, 35.0)
    
    AB = Vector2.from_points(A, B)
    print('vector AB:',AB)    
    
    # get vector length, magnitude
    print('magnitude: ', AB.get_magnitude())
    
    AB.normalize()
    print('normalized:', AB)
 
 
def test_function_v2():

    A = (10.0, 20.0)
    B = (30.0, 35.0)
    C = (15.0, 45.0)
    
    AB = Vector2.from_points(A, B)
    BC = Vector2.from_points(B, C)
    print("Vector AB is", AB)
    print("Vector BC is", BC)
    
    AC = Vector2.from_points(A, C)
    print("Vector AC is", AC)
    
    AC = AB + BC
    print("Addition: AB + BC is", AC)
    
    AC = AB - BC
    print("Subtraction: AB - BC is", AC)

    AC = -AB
    print("Negation: -AB is", AC)        
    
    AC = 10*AB
    print("Multiplication: 10*AB is", AC) 
    
    AC = AB/2
    print("Division: AB/2 is", AC)

def calculate_position():
    #point A
    A = (10.0, 20.0)
    #point B
    B = (30.0, 35.0)
    
    # vector of distance between points AB
    AB = Vector2.from_points(A, B)
    
    # step vector, length of 1/10 AB
    step = AB * .1
    
    #start position vector at point A
    position = Vector2(A[0], A[1])
    
    for n in range(10):
        position += step
        print(position)
     
if __name__ == '__main__':
    #test_function_v2()
    calculate_position()