class Impostor():
    def __init__(self,player,cooldown):
        self.__player = player
        self.cooldown = cooldown

    def get_player(self):
        return self.__player
    
    def get_cooldown(self):
        return self.__cooldown
    
    def set_player(self,newplayer):
        self.__player = newplayer

    def set_cooldown(self,newcooldown):
        self.__cooldown = newcooldown
    
    def to_dict(self):
        return {
            "imposters": self.__player,
            "cooldown": self.__cooldown
        }
