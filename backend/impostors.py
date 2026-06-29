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

    def set_cooldown(self,setcooldown):
        self.__cooldown = setcooldown
