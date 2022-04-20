# problem
class Journal:
  def __init__(self):
    self.entries = []
    self.count = 0
  

  def add_entry(self, text):
    self.count += 1
    self.entries.append(f'{self.count}: {text}')
    
  def remove_entry(self, pos):
    del self.entries[pos]

  def __str__(self):
    return '\n'.join(self.entries)

  # This method violates the Single Responsibility Principle
  def save(self, filename):
    with open(filename, 'w') as f:
      f.write('\n'.join(self.entries))
  
  def load(url):
    pass


j = Journal()
j.add_entry('Join gym')
j.add_entry('Buy car')
print(j)

# solution
# add new class
class JournalManager:
  @staticmethod
  def save(filename, journal):
    with open(filename, 'w') as f:
      f.write(journal)
  
  def load(url):
    pass

j = Journal()
j.add_entry('Join gym')
j.add_entry('Buy car')
j_m = JournalManager()
j_m.save('test.txt', j)