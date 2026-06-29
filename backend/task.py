class Task():
    def __init__(self, name, completed, place, objective):
        self.__name = name
        self.__completed = completed
        self.__place = place
        self.__objective = objective

    def get_name(self):
        return self.__name

    def get_completed(self):
        return self.__completed
    
    def get_place(self):
        return self.__place

    def get_objective(self):
        return self.__objective
    
    def set_name(self, newname):
        self.__name = newname

    def set_completed(self, setcompleted):
        self.__completed = setcompleted

    def set_place(self, setplace):
        self.__place = setplace

    def set_place(self, setobjective):
        self.__objective = setobjective

    def to_dict(self):
        return {
            "name": self.__name,
            "completed": self.__completed
        }