# Activity 1: The Superhero Class

class Superhero:
    """
    A class to represent a superhero.

    It demonstrates the use of attributes, a constructor, and methods.
    """
    def __init__(self, name, power, alias):
        """
        The constructor for the Superhero class.

        Args:
            name (str): The superhero's name.
            power (str): The superhero's special power.
            alias (str): The superhero's secret identity (encapsulated).
        """
        # Attributes are initialized here.
        self.name = name
        self.power = power
        # This is an example of encapsulation. The secret identity
        # is a "private" attribute, indicated by the leading underscore.
        self._alias = alias

    def fight_crime(self):
        """A method to represent the superhero fighting crime."""
        return f"{self.name} is using their {self.power} to fight crime!"

    def reveal_identity(self):
        """A public method to access the private alias attribute."""
        return f"{self.name}'s secret identity is {self._alias}."

class FlyingSuperhero(Superhero):
    """
    A subclass that inherits from Superhero.

    This demonstrates inheritance by adding a new attribute and method,
    while also inheriting the attributes and methods of the parent class.
    """
    def __init__(self, name, power, alias, flight_speed):
        """
        The constructor for the FlyingSuperhero subclass.

        It calls the parent class's constructor using `super()`
        and adds a new attribute specific to flying superheroes.
        """
        super().__init__(name, power, alias)
        self.flight_speed = flight_speed

    def fly(self):
        """A method to represent the superhero flying."""
        return f"{self.name} is flying at an incredible speed of {self.flight_speed} mph!"


# Create superhero objects
# Creating a regular superhero object.
superman = Superhero("Superman", "Super Strength", "Clark Kent")
print(superman.fight_crime())
print(superman.reveal_identity())
print("-" * 20)
# Creating a flying superhero object.
supergirl = FlyingSuperhero("Supergirl", "Heat Vision", "Kara Zor-El", 1200)
print(supergirl.fight_crime())
print(supergirl.reveal_identity())
print(supergirl.fly())


# ---
# Activity 2: Polymorphism Challenge!

class Vehicle:
    """A base class for vehicles with a common 'move' method."""
    def move(self):
        """A generic move action."""
        # This method is designed to be overridden by subclasses.
        pass

class Car(Vehicle):
    """A subclass representing a car."""
    def move(self):
        """The car's specific move action."""
        return "Driving 🚗"

class Plane(Vehicle):
    """A subclass representing a plane."""
    def move(self):
        """The plane's specific move action."""
        return "Flying ✈️"

class Boat(Vehicle):
    """A subclass representing a boat."""
    def move(self):
        """The boat's specific move action."""
        return "Sailing ⛵"

def travel(vehicle):
    """A function that demonstrates polymorphism."""
    # This function can accept any object that has a 'move' method.
    print(vehicle.move())

# Create vehicle objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Call the polymorphic function with different objects.
print("\nPolymorphism in action:")
travel(my_car)
travel(my_plane)
travel(my_boat)
