# Classes allow us to create multiple instances of specific objects.
# What objects mean is similar to an individual student of a real world school class.
# Each Object can have Properties and Methods (similar to functions)

class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """We initialize the attributes of a class inside an initialization method.
        Initialization method runs anytime a new instance of an object is created automatically.
        It has a very specific syntax rule, and we must use __init__(self) syntax as a bare minimum."""

        self.name = name # Any property with the "self" prefix can be accessed by any method inside the class. It also allows setting properties of the object.
        self.age = age  # Any property with the "self" prefix can be accessed by any method inside the class. It also allows setting properties of the object.

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.") # "self" keyword allows us to access to the object's specific instance parameters, which are passed in during initialization.

    def roll_over(self):
        print(f"{self.name.title()} rolls over!") # "self" keyword allows us to access to the object's specific instance parameters, which are passed in during initialization.

# Creating an individual instance of dogs using the Dog class.
# Runs the __init__(self, name, age) method of Dog class automatically during initiation.
# "self" is a special class keyword, which is used for self-reference inside the object's methods.
# We only need to pass the custom arguments we set inside the __init__(name, age) method of the Dog class.
my_dog = Dog("willie", "6")
your_dog = Dog("bob", "12")