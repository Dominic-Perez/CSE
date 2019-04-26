class Item(object):
   def __init__(self, name):
       self.name = name


class Weapon(Item):
   def __init__ (self):
    super(Weapon, self).__init__("Pipe")

class Armor(Item):
    def __init__(self):
        super(Armor, self).__init__("Helmet")



class Pipe(Weapon):
   def __init__(self):




class Knife(Weapon):
   def __init__(self):

