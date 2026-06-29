class Player():
    def __init__(self,name,tasks,state):
        self.__name = name
        self.__tasks = tasks
        self.__state = state

    def get_name(self):
        return self.__name
    
    def get_task(self):
        return self.__tasks
    
    def get_state(self):
        return self.__state
    
    def set_name(self,newname):
        self.__name = newname

    def set_task(self,newtask):
        self.__tasks = newtask

    def set_state(self,state):
        self.__state = state

    def to_dict(self):
        return {
            "name": self.__name,
            # Aqui mapeamos cada objeto Task da lista para o seu próprio dicionário
            "tasks": [task.to_dict() for task in self.__tasks],
            "state": self.__state
        }