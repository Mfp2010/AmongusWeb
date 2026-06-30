class Impostor():
    def __init__(self,player,cooldown):
        self.__player = player
        self.__cooldown = cooldown

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
            "player": self.__player.to_dict(),
            "cooldown": self.__cooldown
        }
