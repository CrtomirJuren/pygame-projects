# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 15:37:57 2020

@author: crtjur
"""
"""
import turtle

tim = turtle.Turtle() # create turtle module object
tim.color('red') #
tim.pensize(5) #thickness of line
tim.shape('turtle')

"""

#==============================================================================
# Turtle adjustments
#==============================================================================
# This is needed to prevent turtle scripts crashes after multiple runs in the
# same IPython Console instance.
# See Spyder issue #6278
try:
    import turtle
    from turtle import Screen, Terminator

    def spyder_bye():
        try:
            Screen().bye()
            turtle.TurtleScreen._RUNNING = True
        except Terminator:
            pass
    turtle.bye = spyder_bye
except:
    pass
