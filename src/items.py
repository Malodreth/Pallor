class Item:
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


    
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
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)



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
