from Fan import Fan
fan=Fan

default_fan = fan(3, "on", 5, "blue")
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