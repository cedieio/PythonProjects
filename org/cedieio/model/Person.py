import uuid

class Person:
    pass
    
    __first_name = ""
    __last_name = ""
    def __init__(self):
        self.__person_id = uuid.uuid4()
        pass

    def get_person_id(self):
        return self.__person_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name
