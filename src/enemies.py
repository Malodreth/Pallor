import pylon

class Enemy:
    def __init__(self, name, hp, damage, advantage, perception):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.advantage = advantage
        self.perception = perception

    def is_alive(self):
        return self.hp > 0

class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="GIANT SPIDER", hp=10, damage=2, advantage=0, perception=2)

class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="OGRE", hp=30, damage=15, advantage=0, perception=10)
