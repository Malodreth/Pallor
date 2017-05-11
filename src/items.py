class Item:
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {}\n".format(self.name, self.description, self.value)


    
class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="GOLD",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

    def add(self, amt):
        self.amt += amt
        self.description = "{} shimmering gold coins.".format(str(self.amt))
        self.value = self.amt



class Weapon(Item):
    """The subclass for all weapons"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {}\n\tDamage: {}\n".format(self.name, self.description, self.value, self.damage)



class Consumable(Item):
    """The subclass for all consumables"""
    def __init__(self, name, description, value, healing):
        self.healing = healing
        super().__init__(name, description, value)

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {}\n\tHealing: {}\n".format(self.name, self.description, self.value, self.healing)



class Mushroom(Consumable):
    def __init__(self):
        super().__init__(name="MUSHROOM",
                         description="A simple brown mushroom. Looks edible.",
                         value=5,
                         healing=15)



class Banana(Consumable):
    def __init__(self):
        super().__init__(name="BANANA",
                         description="A large yellow banana with bruises. Looks edible.",
                         value=5,
                         healing=30)


        
class Rock(Weapon):
    def __init__(self):
        super().__init__(name="ROCK",
                         description="A fist-sized rock, suitable for bludgeoning.",
                         value=0,
                         damage=5)

class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="DAGGER",
                         description="A small blade with a dull point. Still more dangerous than a rock.",
                         value=10,
                         damage=10)
