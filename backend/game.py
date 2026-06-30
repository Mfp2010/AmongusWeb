class Game():
    def __init__(self,state):
        self.__state = state

    def get_state(self):
        return self.__state
        
    def set_state(self,newstate):
        self.__state = newstate