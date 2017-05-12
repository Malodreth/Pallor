from player import Player



##### ACTION TEMPLATES #####

class Action():
    """Class template for all actions"""
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "[{}] {}".format(self.hotkey, self.name)
    
############################
##### DEFAULT ACTIONS #####
    
class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')


class Look(Action):
    """Reprints the current room description"""
    def __init__(self):
        super().__init__(method=Player.look, name='Look', hotkey='l')


class CheckStatus(Action):
    """Prints the player's stats"""
    def __init__(self):
        super().__init__(method=Player.check_status, name='Check status', hotkey='h')


class UseConsumable(Action):
    def __init__(self):
        super().__init__(method=Player.use_consumable, name='Use consumable', hotkey='c')


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, name='View inventory', hotkey='i')


class ViewMap(Action):
    """Prints a vertical layout of the game map"""
    def __init__(self):
        super().__init__(method=Player.view_map, name='View map', hotkey='m')
        
###########################
##### COMBAT ACTIONS #####
        
class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, name='Attack', hotkey='a', enemy=enemy)


class Flee(Action):
    def __init__(self, tile, enemy):
        super().__init__(method=Player.flee, name='Flee', hotkey='f', tile=tile, enemy=enemy)
        
##########################
##### CIRCUMSTANTIAL ACTIONS #####
        
class UseKey(Action):
    def __init__(self, tile):
        super().__init__(method=Player.use_key, name='Use key', hotkey='k', tile=tile)
        
##################################
