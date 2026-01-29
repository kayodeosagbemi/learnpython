# Creating a Dog class
class Dog:
    def __init__(self, name, breed):
        self.name =name
        self.breed=breed

    def bark(self):
        print(f"{self.name} says Woof!")



dog = Dog("Aja", "German Shephard")
dog.bark()

