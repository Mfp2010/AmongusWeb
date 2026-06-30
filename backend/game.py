class Game():
    def __init__(self,state,players,imposters):
        self.__state = state
        self.__players = players
        self.__imposters = imposters

    def get_state(self):
        return self.__state
        
    def get_players(self):
        return self.__players

    def get_imposters(self):
        return self.__imposters

    def set_state(self,newstate):
        self.__state = newstate

    def set_players(self,newplayers):
        self.__players = newplayers
    
    def set_imposters(self,newimposters):
        self.__imposters = newimposters
    
    def to_dict(self):
        return {
            "state": self.__state,
            "players": [p.to_dict() for p in self.__players],
            "imposters": [i.to_dict() for i in self.__imposters]
        }