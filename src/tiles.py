import pylon, items, enemies, actions



MapTile = pylon.MapTile
LootRoom = pylon.LootRoom
EnemyRoom = pylon.EnemyRoom



#Starting and ending rooms

class StartingRoom(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = "START"
        
    def intro_text(self):
        return """
        You can make out four paths, each equally as dark and foreboding.
        """

    def modify_player(self, player):
        #Room has no action on player
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



#Misc rooms
        
class EmptyCavePath(MapTile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.id = "EMPTY HALLWAY"
        
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class SnakePitRoom(MapTile):
    def intro_text(self):
        return "\n\tYou fell into a pit of deadly snakes!"

    def modify_player(self, player):
        player.hp = 0



#Loot rooms

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



#Enemy rooms

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
