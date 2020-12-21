# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 10:54:58 2020

@author: crtom
"""

import numpy as np

def var1():
    # build a list of touples from two numpy arrays
    x = np.linspace(0, 500, 6)
    y = np.linspace(0, 500, 6)
    
    z = zip(x,y)
    print(list(z))

def var2():
    # create a list of touple positions
    lst = []
    for x in range(0, 600, 100):
        for y in range(0, 600, 100):
            lst.append((x,y))
    
    print(lst)
    print('first item:',lst[0])
    print('last item:',lst[35])
   
# create a dictionary of grid    
def var3():
    
    thisdict = {
      "position_vertice": (0,0),
      "position_card": (10,10),
      "surface": 1964
    }           
    
    print(thisdict["position_vertice"])
    print(thisdict["position_vertice"])
    print(thisdict["surface"])

def var4():
    pass

    
#var3()
