from abc import ABC, abstractmethod
class Creature(ABC):
    @abstractmethod
    def feed(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def make_noise(self):
        pass
    
class Animal(Creature):
    def feed(self):
        print("I eat grass")
        
    def move(self):
        print("I walk forward")
    
    def make_noise(self):
        print("WOOO!")

# Abstrcat decorator
class AbstractDecorator(Creature):
    def __init__(self, obj):
        self.obj = obj
        
    def feed(self):
        self.obj.feed()
    
    def move(self):
        self.obj.move()
    
    def make_noise(self):
        self.obj.make_noise()
        
class Swimming(AbstractDecorator):
    def move(self):
        print("I swim")
    
    def make_noise(self):
        print("...")
        
class Flying(AbstractDecorator):
    def move(self):
        print("I fly")
    
    def make_noise(self):
        print("QUAAA!")
        
class Predator(AbstractDecorator):
    def feed(self):
        print("I eat other animals")
        
class Fast(AbstractDecorator):
    def move(self):
        self.obj.move()
        print("Fast!")

animal = Animal()
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Swimming(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Predator(animal)
animal.feed()
animal.move()
animal.make_noise()
print()

animal = Fast(animal)
animal.feed()
animal.move()
animal.make_noise()

print()
animal = Fast(animal)
animal.feed()
animal.move()
animal.make_noise()
print()