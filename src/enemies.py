import pylon



Enemy = pylon.Enemy

###########################
##### ENEMIES #####
    
class GiantSpider(Enemy):
    def __init__(self):
        super().__init__(name="GIANT SPIDER", hp=15, damage=3, advantage=0, perception=2)


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="OGRE", hp=60, damage=15, advantage=0, perception=10)

###################
