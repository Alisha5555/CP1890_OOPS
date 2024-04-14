from dataclasses import dataclass


# The Animal class with attributes name and class, method speak
@dataclass
class Animal:
    name: str
    species: str

    def speak(self):
        pass


# The Dog(Animal) class adding breed and overriding speak
@dataclass
class Dog(Animal):
    breed: str

    def speak(self):
        print("Woof!")


# The Cat(Animal) class adding color and overriding speak
@dataclass
class Cat(Animal):
    color: str

    def speak(self):
        print("Meow!")


# The main function to run the program
def main():
    dog = Dog("Max", "Dog", "Golden Retriever")
    cat = Cat("Whiskers", "Cat", "Orange")

    print("Dog:")
    print("Name:", dog.name)
    print("Species:", dog.species)
    print("Breed:", dog.breed)
    print("Sound:", end=" ")
    dog.speak()
    print("\n")
    print("Cat:")
    print("Name:", cat.name)
    print("Species:", cat.species)
    print("Color:", cat.color)
    print("Sound:", end=" ")
    cat.speak()


if __name__ == "__main__":
    main()
