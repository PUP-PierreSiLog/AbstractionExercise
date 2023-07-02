class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = int(age)
    
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name (self):
        print("The name of the pet is ", self.__name)

    def get_age(self):
        print("The age of the pet is ", self.__age)
    
    def get_type(self):
        print("The type of pet is ", self.__animal_type)