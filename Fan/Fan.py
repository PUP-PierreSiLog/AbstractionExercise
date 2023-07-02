class Fan:
        # ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
        # ■ A private int data field named speed that specifies the speed of the fan.
        # ■ A private bool data field named on that specifies whether the fan is on (the default is False).
        # ■ A private float data field named radius that specifies the radius of the fan.
        # ■ A private string data field named color that specifies the color of the fan.
    def __init__(self, speed, on, radius, color):
        self.__speed = int(speed)
        self.__on = bool(on)
        self.__radius = float(radius)
        self.__color = str(color)
    # ■ The accessor(getters)
    def get_speed(self):
        return self.__speed
    
    def get_on(self):
        return self.__on
    
    def get_radius(self):
        return self.__radius
    
    def get_color(self):
        return self.__color
    
    #and mutator(setters) methods for all four data fields.
    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_on(self, on):
        self.__on = bool(on)
        if on == True:
            self.__on = "On"
        else:
            self.__on = "Off"
    
    def set_radius(self, radius):
        self.__radius = float(radius)

    def set_color(self, color):
        self.__color = str(color)

    def show_fan(self):
        print("The fan's speed is", self.__speed, ".It's current status is",self.__on, ".The fan has a radius of", self.__radius, "and has a color",self.__color)
    # ■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
