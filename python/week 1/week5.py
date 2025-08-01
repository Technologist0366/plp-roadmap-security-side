# Base class
class Superhero:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # Protected attribute

    def show_power(self):
        print(f"{self.name} has power level {self._power_level} 💥")

# Subclass with extra features and method overriding (polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power_level, altitude):
        super().__init__(name, power_level)
        self.altitude = altitude

    def show_power(self):  # Polymorphism in action
        print(f"{self.name} is flying at {self.altitude} meters with power {self._power_level} ✈️")

# Subclass with encapsulated behavior
class InvisibleHero(Superhero):
    def __init__(self, name, power_level):
        super().__init__(name, power_level)
        self.__invisible = False  # Private attribute

    def go_invisible(self):
        self.__invisible = True
        print(f"{self.name} is now invisible 🕵️‍♂️")

# Creating objects
hero1 = Superhero("Bolt", 80)
hero2 = FlyingHero("SkyWing", 95, 1000)
hero3 = InvisibleHero("Ghost", 70)

# Interacting with objects
hero1.show_power()
hero2.show_power()        # Polymorphism
hero3.show_power()
hero3.go_invisible()      # 
Encapsulation


Activity 2: Polymorphism


class Car:
    def move(self):
        print("The car is driving 🚗")

class Bike:
    def move(self):
        print("The bike is cycling 🚴‍♂️")

class Plane:
    def move(self):
        print("The plane is flying ✈️")

# Polymorphism in action
vehicles = [Car(), Bike(), Plane()]

for vehicle in vehicles:
    vehicle.move()

