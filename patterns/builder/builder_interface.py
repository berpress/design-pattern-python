class Person:
  def __init__(self):
    self.name = None
    self.position = None
    self.date_of_birth = None

  def __str__(self):
    return f'{self.name} born on {self.date_of_birth} works as a {self.position}'

  @staticmethod
  def new():
    return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
      self.person.name = name
      return self

class PersonWorkBuilder(PersonInfoBuilder):
    def position(self, position):
      self.person.position = position
      return self

class PersonDateBuilder(PersonWorkBuilder):
    def date_of_birth(self, date_of_birth):
      self.person.date_of_birth = date_of_birth
      return self

pb = PersonDateBuilder()
person = pb.called('Dmitri').position('Doctor').date_of_birth('1/1/1990').build()
print(person)
