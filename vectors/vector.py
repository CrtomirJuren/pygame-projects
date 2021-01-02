# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:31:56 2020

@author: crtom
"""

import math
import random

class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # Vector operator overload
    # theory: when called a + b, python calls a.__add__(b)
    # we now overrdide this methods
    
    def __add__(self, other):
        if isinstance (other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y )
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance (other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y )
        return Vector(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance (other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y )
        return Vector(self.x * other, self.y * other)

    # # reverse multiply override
    # def __rmul__(self, other):
    #     return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)   # commutative operation
    
    def __truediv__(self, other):
        if isinstance (other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y )
        return Vector(self.x / other, self.y / other)
    
    # check for equal
    def __eq__(self, other):
        if isinstance (other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other
    
    def make_int_tuple(self):
        return int(self.x), int(self.y)

    def set(self, vec):
        self.x = vec.x
        self.y = vec.y

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
        
# additional vector calculations
# Skalarni produkt (Dot product)
#Rezultat se izračuna kot produkt dolžin obeh vektorjev in kosinusa vmesnega kota. 
def dot(vec1, vec2):
    return vec1.x * vec2.x + vec1.y * vec2.y    

# calculate vector angle
# angle = arccos[(xa * xb + ya * yb) / (√(xa2 + ya2) * √(xb2 + yb2))]

def angle_between(vec1, vec2):
    return math.acos(dot(vec1, vec2))


#-----------------------------------------------------------------------------
#----------------------DISTANCE AND LENGTH FUNCTIONS--------------------------
#-----------------------------------------------------------------------------



# vector lengt squared, faster
# pitagora a^2+b^2 = c^2
def length_sqr(vec):
    return vec.x**2 + vec.y**2

# vector length
def length(vec):
    return math.sqrt(length_sqr(vec))

# distance between vector squared, faster
def dist_sqr(vec1, vec2):
    return length_sqr(vec1 - vec2)

# distance between vector squared, faster
def dist(vec1, vec2):
    return length(vec1 - vec2)

# create a unit vector
def normalize(vec):
    vec_length = length(vec)
    
    # check if null size
    if vec_length < 0.00001:
        return Vector(0, 1)
    # return unit vector
    return Vector(vec.x / vec_length, vec.y / vec_length)

# reflections
def reflect(incident, normal):
    return incident - dot(normal, incident) * 2.0 * normal

def negate(vec):
    return Vector(-vec.x, -vec.y)

# rotation 90deg clockwise, perpendicual
def right(vec):
    return Vector(-vec.y, vec.x)

def left(vec):
    return negate(right(vec)) 

# create a random vector
def random_vector():
    return Vector(random.random()*2.0 - 1.0, random.random()*2.0-1.0)

def random_direction():
    return normalize(random_vector())

# so we dont have any issues with references
def copy(vec):
    return Vector(vec.x, vec.y)


# ---------- testing code    
def test_operator_overloads():
    a = Vector(5, 10)
    b = Vector(-5, 10)
    
    print(a.x, a.y)
    print(b.x, b.y)
    
    c = a + b #Vector class using __add__ operator overload
    print('__add__:', c.x, c.y)

    c = a - b #Vector class using __add__ operator overload
    print('__sub__:', c.x, c.y)

    c = a * b #Vector class using __add__ operator overload
    print('__mul__:', c.x, c.y)
    
    # normal operator overload
    c = a * 10
    print('__mul__:', c.x, c.y)

    # reverse operator overload
    c = 10 * a
    print('__rmul__:', c.x, c.y)
    
    c = a / b #Vector class using __add__ operator overload
    print('__truediv__:', c.x, c.y)


def test_functions():
    a = Vector(1, 1)
    b = Vector(0, 0)
    
    print('a = Vector(1, 1): ', a.x, a.y)
    print('b = Vector(0, 0)', b.x, b.y)

    print('Skalarni produkt (Dot product):', dot(a, b))
    print('angle_between a and b :', angle_between(a, b))   
    print('length of vector a:', length(a))  
    print('length_squared:', length_sqr(a))   
    
if __name__ == '__main__':
    test_functions()