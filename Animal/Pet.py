class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    
    def set_name(self, name):
        name = input("Please input name here")
        self.__name = name

    def get_name (self):
        print("The name of the pet is ", self.__name)