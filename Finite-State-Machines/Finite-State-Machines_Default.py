from enum import Enum, auto
import time

class States(Enum):
    IDLE = auto()
    STARTING = auto()
    RUNNING = auto()
    STOPING = auto()
    ERROR = auto()

class StateObject:
    def __init__(self):
        self.__state = States.IDLE

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state

class Entity(StateObject):
    def __init__(self):
        super().__init__()
        self.__counter = 0

    def inc_counter(self):
        self.__counter += 1

    def sub_counter(self):
        self.__counter -= 1

    def get_counter(self):
        return self.__counter

    def set_counter(self, counter):
        self.__counter = counter

SM1 = Entity()
SM1.set_state(States.IDLE)

SM2 = Entity()
SM2.set_state(States.IDLE)

while True:

    #if we are in IDLE state, ask user for statemachine run
    if SM1.get_state() == States.IDLE:
        user_input = input("goto RUNNING=ok, goto ERRROR=nok, quit=q")
        print("-----------------------------------------")

        if user_input == "ok":
            SM1.set_state(States.RUNNING)
            SM1.set_counter(5)
        elif user_input == "nok":
            SM1.set_state(States.ERROR)
            SM1.set_counter(10)
        elif user_input == "q":
            break

    if SM1.get_state() == States.RUNNING:
        SM1.sub_counter()
        print(SM1.get_counter())
        time.sleep(1) #slow running state
        if SM1.get_counter() <= 0:
            SM1.set_state(States.IDLE)

    if SM1.get_state() == States.ERROR:
        SM1.sub_counter()
        print(SM1.get_counter())
        time.sleep(0.1) #slow running state
        if SM1.get_counter() <= 0:
            SM1.set_state(States.IDLE)

print("Statemachine stopped")