class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        print(f"{self.name.title()} rolls over!")

my_dog = Dog("willie", "6")
your_dog = Dog("bob", "12")

print(f"My dog's name is {my_dog.name.title()}, and it is {my_dog.age} years old.")
print(f"Your dog's name is {your_dog.name.title()}, and it is {your_dog.age} years old.")

# Accessing the methods of individual Dog class instances.
my_dog.sit()
your_dog.roll_over()