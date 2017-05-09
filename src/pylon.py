import items, enemies, actions, pkg_resources, random
from re import match



_world = {}
_max_x = 0
_max_y = 0



def run(r):
    return random.randint(0, r - 1)

def d6():
    return random.randint(1, 6)

def d12():
    return random.randint(1, 12)

def d20():
    return random.randint(1, 20)

def d100():
    return random.randint(1, 100)



def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    global _max_x, _max_y
    with open(pkg_resources.resource_filename(__name__, 'resources/map.txt'), 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split())
    _max_x = x_max
    _max_y = len(rows)
    for y in range(len(rows)):
        cols = rows[y].split()
        for x in range(x_max):
            tile_name = cols[x].rstrip()
            _world[(x, y)] = None if match(r'^x+$', tile_name) else getattr(__import__('tiles'), tile_name)(x, y)



def tile_exists(x, y):
    return _world.get((x, y))



class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = "??????????"

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.Look())
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewMap())
        return moves



class LootRoom(MapTile):
    """The subclass for all loot rooms"""
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        if isinstance(self.item, items.Gold):
            player.add_gold(self.item.amt)
        else:
            player.inventory.append(self.item)
        self.item = None

    def modify_player(self, player):
        if self.item:
            self.add_loot(player)



class EnemyRoom(MapTile):
    """The subclass for all enemy rooms"""
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            dmg = self.enemy.damage + d6()
            the_player.hp = the_player.hp - dmg
            if not the_player.hp < 0: 
                print("\n\t{} does {} damage. You have {} HP remaining.\n".format(self.enemy.name, dmg, the_player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.Look())
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewMap())
            return moves
