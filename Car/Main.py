class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self, speed):
        self.__speed = speed + 5
        return self.__speed
    
    def brake(self, speed):
        self.__speed = speed - 5
        return self.__speed
    
    def get_speed (self, speed):
        return self.__speed
    