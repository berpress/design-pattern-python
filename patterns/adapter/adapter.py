#problem

# American fork
class UsaFork:
    def power_usa(self):
        print('power on. Usa')

# Europe fork
class EuroFork:
    def power_euro(self):
        print('power on. Euro')

# American socket
class UsaSocket:
    def __init__(self, fork):
        self.fork = fork
    def connect(self):
        self.fork.power_usa()

# Use American fork with American socket
uf = UsaFork()
us = UsaSocket(uf)
us.connect()

# Use Europe fork with American socket, get error
ef = EuroFork() 
us = UsaSocket(ef) 
us.connect() 


# solution
class AdapterEuroInUsa:
    def __init__(self):
        self._euro_fork = EuroFork()
    def power_usa(self):
        self._euro_fork.power_euro()

# Use American fork with American socket
uf = UsaFork() 
us = UsaSocket(uf) 
us.connect() 
# >>> power on. Usa
# Use Europe fork with American socket, get error
ad = AdapterEuroInUsa()
us = UsaSocket(ad)
us.connect() 