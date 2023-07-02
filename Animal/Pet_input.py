from Pet import Pet
pet=Pet

default_pet=pet("", "", 0)
default_pet.set_name(name = input("Put name here:"))
default_pet.set_age(age = int(input("Input age here:")))
default_pet.set_animal_type(animal_type=input("Please input pet type here:"))
default_pet.get_name()
default_pet.get_age()
default_pet.get_type()