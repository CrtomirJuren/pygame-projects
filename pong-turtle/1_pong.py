"""
Simple pong in python 3 for begginers

tutorial series: https://www.youtube.com/playlist?list=PLlEgNdBJEO-kXk2PyBxhSmo84hsO3HAz2
"""

import turtle

wn = turtle.Screen()
wn.title("Pong by @TokyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# main game loop
while True:
	wn.update() #updates screen