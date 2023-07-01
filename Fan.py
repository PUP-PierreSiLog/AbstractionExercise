class Fan:
        # ■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
        # ■ A private int data field named speed that specifies the speed of the fan.
        # ■ A private bool data field named on that specifies whether the fan is on (the default is False).
        # ■ A private float data field named radius that specifies the radius of the fan.
        # ■ A private string data field named color that specifies the color of the fan.
    def __init__(self, speed, on, radius, color):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
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
        self.__speed = speed

    def set_on(self, on):
        self.__on = on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def show_fan(self):
        print("The fan's speed is", self.__speed, ".It's current status is",self.__on, ".The fan has a radius of", self.__radius, "and has a color",self.__color)
    # ■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
default_fan = Fan(3, "on", 5, "blue")
    # Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.
#FOR FAN 1
default_fan.set_speed(3)
default_fan.set_radius(10)
default_fan.set_color("yellow")
default_fan.set_on("on")
default_fan.show_fan()
#FOR FAN 2
default_fan.set_speed(2)
default_fan.set_radius(5)
default_fan.set_color("blue")
default_fan.set_on("off")
default_fan.show_fan()
