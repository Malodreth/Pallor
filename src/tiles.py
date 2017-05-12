import pylon, items, enemies


MapTile = pylon.MapTile
LootRoom = pylon.LootRoom
EnemyRoom = pylon.EnemyRoom
LockedRoom = pylon.LockedRoom


##### STANDARD ROOMS #####

class StartingRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = "START"
        
    def intro_text(self):
        return """
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        pass


class VictoryRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows as you get closer! It's sunlight!


        Victory is yours!
        """

    def modify_player(self, player):
        player.victory = True

        
class EmptyCavePath(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = "EMPTY HALLWAY"
        
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        pass


class SnakePitRoom(MapTile):
    def intro_text(self):
        return "\n\tYou fell into a pit of deadly snakes!"

    def modify_player(self, player):
        player.hp = 0

##########################
##### STANDARD LOOT ROOMS #####

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())
        self.id = "TREASURE: DAGGER"

    def intro_text(self):
        if self.item:
            return """
        You notice something in the corner.
        It's a dagger! You pick it up.
            """
        else:
            return """
        This is the room that your dagger was found in.
        Nothing else is remarkable about this room now.
            """


class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))
        self.id = "TREASURE: GOLD"

    def intro_text(self):
        if self.item:
            return """
        Someone dropped a 5 gold piece. You pick it up.
            """
        else:
            return """
        You discovered gold in this room.
        It is now empty and unremarkable.
            """


class FindBananaRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Banana())
        self.id = "TREASURE: FOOD"

    def intro_text(self):
        if self.item:
            return """
        You find a wooden table with a broken chair. Upon the table a
        clay plate with a tasty ripe banana rests beside a dirty fork.

        Who's dinner was this? You put the banana in your inventory.
            """
        else:
            return """
        You see a wooden table with an empty plate and a broken chair.
        Nothing else looks interesting.
            """

###############################
##### LOCKED LOOT ROOMS #####

class StorageRoom(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, "storage",
                         items.Longsword(),
                         """
        The door unlocks and you find a closet with a longsword inside
        a display case! You pick up the longsword.""")
        self.id = "LOCKED DOOR"

    def intro_text(self):
        if not self.opened and self.locked:
            return """
        You stumble upon a locked door. The keyhole makes an odd crossed shape.
            """
        else:
            return """
        You previously unlocked this room and found a longsword.
        It is now empty. You must press on.
            """


class FindChestRoom(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, "deusex",
                         items.BoneKey(),
                         """
        The chest opens and inside you find... another key? The key
        seems to be made of bone. You notice that its teeth end in four
        points from the centre.""")
        self.id = "LOCKED CHEST"

    def intro_text(self):
        if not self.opened and self.locked:
            return """
        You see a golden trunk with the words 'Machina' engraved on the front.
        It needs a key to open it.
            """
        else:
            return """
        You previously unlocked this chest and found another key.
            """

#############################
##### ENEMY ROOMS #####

class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())
        self.id = "GIANT SPIDER"

    def intro_text(self):
        if self.enemy.is_alive():
            return "\n\tA giant spider jumps down from its web in front of you!"
        else:
            return """
        The corpse of a dead spider rots on the ground.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())
        self.id = "OGRE"

    def intro_text(self):
        if self.enemy.is_alive():
            return "\n\tAn ogre is blocking your path!"
        else:
            return """
        A dead ogre reminds you of your triumph.
            """

#######################
