# import the turtle module so we can use all the neat code it contains
from turtle import Turtle, Screen

KEY_REPEAT_RATE = 20  # in milliseconds

# Create a variable `tina` that is a Turtle() object. Set shape to 'turtle'
tina = Turtle('turtle')

# Create a variable `screen`, a Screen() object, that will handle keys
screen = Screen()

# Define functions for each arrow key
def go_left():
    tina.left(7)
    if repeating:
        screen.ontimer(go_left, KEY_REPEAT_RATE)

def go_right():
    tina.right(7)
    if repeating:
        screen.ontimer(go_right, KEY_REPEAT_RATE)

def go_forward():
    tina.forward(10)
    if repeating:
        screen.ontimer(go_forward, KEY_REPEAT_RATE)

def go_backward():
    tina.backward(10)
    if repeating:
        screen.ontimer(go_backward, KEY_REPEAT_RATE)

def start_repeat(func):
    global repeating

    repeating = True

    func()

def stop_repeat():
    global repeating

    repeating = False

repeating = False

# Tell the program which functions go with which keys
screen.onkeypress(lambda: start_repeat(go_left), 'Left')
screen.onkeyrelease(stop_repeat, 'Left')

screen.onkeypress(lambda: start_repeat(go_right), 'Right')
screen.onkeyrelease(stop_repeat, 'Right')

screen.onkeypress(lambda: start_repeat(go_forward), 'Up')
screen.onkeyrelease(stop_repeat, 'Up')

screen.onkeypress(lambda: start_repeat(go_backward), 'Down')
screen.onkeyrelease(stop_repeat, 'Down')

# Tell the screen to listen for key presses
screen.listen()

screen.mainloop()