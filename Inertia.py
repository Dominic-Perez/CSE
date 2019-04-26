class Room(object):
   def __init__(self, name, north=None, south=None, east=None, west=None, northeast=None, northwest=None,
                description=""):
       self.name = name
       self.north = north
       self.south = south
       self.east = east
       self.west = west
       self.northeast = northeast
       self.northwest = northwest
       self.description = description


class Item(object):
   def __init__(self, name):
       self.name = name


class Character(object):
   def __init__(self, name, health, weapon, armor):
       self.name = name
       self.health = health
       self. weapon = weapon
       self.armor = armor

   def take_damage(self, damage):
       self.health -= damage
       if self.health < 0:
           self.health = 0

   def attack(self, target):
       print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
       target.take_damage(self.weapon.damage)


class Weapon(Item):
   def __init__(self, name, damage):
       super(Weapon, self).__init__(name)
       self.damage = damage


class Player(object):
   def __init__(self, starting_location):
       self.health = 100
       self.current_location = starting_location
       self.inventory = []
       self.damage = 10

   def move(self, new_location):
       """


       :param new_location: The variable containing a room object
       """
       self.current_location = new_location


R19A = Room("R19A", 'parking_lot')
parking_lot = Room('The Parking Lot', None, "R19A")
tagging = Room("Tagging Scene", None, None, 'Cop', None, None, None,
              "You awoke from your nap, and it just so happened that one of your own ratted you out\n"
              "to the police, whom invaded you at your last tagging scene before subduing you and \n"
              "handcuffing you to a metal pole. They have just now gave you a choice. \n"
              "Give up your life of crime and join"
              " the police force and solve the murder of the mayor of your town, which is known as Shibuya.\n"
              "Welcome to Inertia!!")

Cop = Room("Cop Car", None, None, None, None, "Murder", None,
          "After being shoved into the cop car and landing on a very stiff bolt, you are\n"
          "Chauffeured to the seen of the murder of the mayor.")

Murder = Room("Murder Scene", "StreetMiddle", None, "StreetRight", "StreetLeft", None, None,
             "You are shown into the room after being dragged ( against your will ) from the cop car. \n"
             "The room looked very much like a murder scene, everything was moved out of place and there were signs\n"
             "of obvious struggle from the mayor. The mayor is beaten and broken, obviously having died of\n"
             "Blunt Force Trauma, somebody obviously beat him to death. You begin questioning why the police needed\n"
             "you and you remember... you're a criminal whom evaded their manhunt for 2 years... takes a criminal\n"
             "to catch a criminal, also, you are fairly expendable. Quite the oddity, huh?")


StreetMiddle = Room("Street Middle", None, None, None, "Heather", None, None,
                   "You have arrived at South Shibuya St. walking down the the road, you look around\n"
                   "and spot a familiar house... why did those officers have to hit you so hard? \n"
                   "Now you can't even remember, wait that's Heather's house! You should probably drop by to say hi\n"
                   "but the bar seems like fun, watching the drunks be idiots, but whatever its your choice."
                   )

Heather = Room("Heather's Apartment", "Second", None, None, "StreetMiddle", None, None,
              "As you walk to the door, a familiar female known as Amber, or Heather's sister asnwers the door\n"
              "and welcomes you in, 5 minutes later Heather walks out and talks to you about your estranged brother\n"
              "who is near the pier, but there might be a clue near the North.")

StreetRight = Room("Street Right", None, None, "Pier", None, None, None,
                  "You arrive at the East Shibuya St. and you see the pier, but your brother's house happens\n"
                  "to be towards the Northeast. ")
Pier = Room("Pier", "Oliver", None, None, None, None, None,
           "The smell of salty sea air fills your nostrils. You see your brothers house and you have a strong\n"
           "desire to go there. ")

Oliver = Room("Oliver", "First", None, None, None, None, None,
             "You knock on the door, and your brother Oliver opens the door to the house. You two talk for a while\n"
             "and he shows you to a room where he has a special box he found.")
First = Room("First Clue", None, "Oliver", None, "Cellar", None, None,
            "You walk down a long hallway and you are in a darkly lit room, and your brother hands you a box."
            "It has the letter L inside of it.")
Cellar = Room("Cellar", None, None, "Bar", "First", None, None,
             "You arrive into a very damp cellar, the air is humid to keep the corks in good condition \n"
             "You smile as you trip on yourself, opening a previously closed passage.")
Bar = Room("Bar", None, "StreetMiddle", "Cellar", "Second", None, None,
          "You walk into the bar that is filled with loud drunks. It annoys you heavily but you walk to a room\n"
          "That has a box in it, what is it?")
Second = Room("Second Clue", None, "Heather", "Bar", None, None, None,
             "You walk into a pretty chill room, and you look into the box in it, the letter O is in it.")

Night = Room("Night Club", "StreetLeft", None, "Fourth", "Third", None, None,
            "You walk into the night club, another place filled with drunks, and again you get annoyed.\n"
            "There is a spare spray paint can, and you walk to it, picking it up, and immediately pass out.")
Fourth = Room("Fourth Clue", "Tagging Scene", None, None, "Night", None, None,
             "You wake up in a room with the same boxes as before, and the letter E is in it. You know the code\n"
             "which is LOVE, type it in to win!")
Third = Room("Third Clue", None, None, "Night", None, None, None,
            "You walk into a room, and it has a box with the letter V in it, almost done now!")

StreetLeft = Room("Street Left", None, "Night", "Murder", "Katie", None, None,
                 "Nothing here to see except the church, where your friend Katie is usually at all the time.")





# Items
knife = Weapon("Knife", 5)
knife2 = Weapon("Bowie Knife", 10)

# Players
player = Player(tagging)


# Characters
c1 = Character("Thug 1", 10, knife, None)
c2 = Character("Thug 2", 20, knife2, None)
c1.attack(c2)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down', 'northeast', 'northwest']
short_directions = ['n', 's', 'e', 'w', 'u', 'd', 'ne', 'nw']
# Controller

while playing:
   print(player.current_location.name)
   print(player.current_location.description)
   command = input(">_")

   if command.lower() in short_directions:
       pos = short_directions.index(command.lower())
       command = directions[pos]

   if command.lower() in ['q', 'quit', 'exit']:
       playing = False
   elif command.lower() in directions:
       try:
           # command = 'north'
           room_name = getattr(player.current_location, command)
           room_object = globals()[room_name]

           player.move(room_object)
       except KeyError:
           print("This key does not exist")
       except AttributeError:
           print("I can't go that way.")
   else:
       print("Command Not Recognized")
