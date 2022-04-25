class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:
    id = 0

    def create_person(self, name):
      p = Person(PersonFactory.id, name)
      PersonFactory.id += 1
      return p

person = PersonFactory().create_person('Test')
person2 = PersonFactory().create_person('Test2')
