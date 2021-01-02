# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 11:44:03 2020

@author: crtom
"""


from vector import Vector

a = Vector(5, 10)
b = Vector(-5, 10)

c = a + b #Vector class using __add__ operator overload

print(a.x, a.y)
print(b.x, b.y)
print(c.x, c.y)

# if we want to do a*b. vector multiplication
# we need to create constructor overload
