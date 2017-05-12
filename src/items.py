##### ITEM TEMPLATES #####

class Item:
    """Class template for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {} gold\n".format(self.name, self.description, self.value)

    
class Gold(Item):
    """Class template for gold coins"""
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="COIN PURSE",
                         description="A burlap pouch tied to your belt, meant for carrying gold coins. Currently empty.",
                         value=self.amt)

    def add(self, amt):
        self.amt += amt
        self.description = "A burlap pouch tied to your belt containing several shimmering gold coins."
        self.value = self.amt


class Weapon(Item):
    """Class template for all weapons"""
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {} gold\n\tDamage: -{} HP\n".format(self.name, self.description, self.value, self.damage)


class Key(Item):
    """Class template for all keys"""
    def __init__(self, name, description, value, unique):
        self.unique = unique
        super().__init__(name, description, value)


class Consumable(Item):
    """Class template for all consumables"""
    def __init__(self, name, description, value, healing):
        self.healing = healing
        super().__init__(name, description, value)

    def __str__(self):
        return "\t{}\n\t=====\n\t{}\n\tValue: {} gold\n\tHealing: +{} HP\n".format(self.name, self.description, self.value, self.healing)

##########################
##### KEYS #####

class BoneKey(Key):
    def __init__(self):
        super().__init__(name="BONE KEY",
                         description="An ornate key carved from bone. What does it open?",
                         value=5,
                         unique="storage")


class GoldenKey(Key):
    def __init__(self):
        super().__init__(name="GOLDEN KEY",
                         description="A key made of gold with 'Deus Ex' written on a ribbon tied to its end.",
                         value=0,
                         unique="deusex")

################
##### WEAPONS #####

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


class Longsword(Weapon):
    def __init__(self):
        super().__init__(name="LONGSWORD",
                         description="A long, simple blade made of steel with a very sharp edge.",
                         value=25,
                         damage=25)        

###################
##### CONSUMABLES #####
        
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
                         value=10,
                         healing=30)

#######################
