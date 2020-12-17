
print("steamchine example!")


# This variable holds the current state of the machine
stateNum = 0

def advance_state_machine():
    global stateNum
    if stateNum == 0:      # Transition from state 0 to state 1
       print("yellow")
       stateNum = 1
    elif stateNum == 1:    # Transition from state 1 to state 2
       print("red")
       stateNum = 2
    else:                  # Transition from state 2 to state 0
       print("green")
       stateNum = 0

while True:
  user_input = input("press up, pres down")
  print(user_input)
  if user_input == "q":
    break
  elif user_input == "w":
    advance_state_machine()
