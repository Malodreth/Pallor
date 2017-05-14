import items, actions, random
from re import match


_world = {}
_max_x = 0
_max_y = 0


##### TILING ENGINE #####

def load_tiles(map_id):
    """Parses a .txt file that feeds the map into the _world dictionary"""
    global _max_x, _max_y
    with open('map_{}.txt'.format(map_id)) as f:
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

#########################
##### RANDOM NUMBER GENERATORS #####

def run(r):
    return random.randint(0, r - 1)

def map_select(r):
    return random.randint(1, r)

def d6():
    return random.randint(1, 6)

def d12():
    return random.randint(1, 12)

def d20():
    return random.randint(1, 20)

def d100():
    return random.randint(1, 100)

####################################
##### TILE TEMPLATES #####

class MapTile:
    """Class template for all rooms"""
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
        moves.append(actions.CheckStatus())
        moves.append(actions.UseConsumable())
        moves.append(actions.ViewInventory())
        moves.append(actions.ViewMap())
        return moves


class LootRoom(MapTile):
    """Class template for all standard loot rooms"""
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
            

class LockedRoom(MapTile):
    """Class template for all locked loot rooms"""
    def __init__(self, x, y, key, item, description):
        self.key = key
        self.item = item
        self.description = description
        self.opened = False
        self.locked = True
        super().__init__(x, y)

    def add_loot(self, player):
        if isinstance(self.item, items.Gold):
            player.add_gold(self.item.amt)
        else:
            player.inventory.append(self.item)
        self.item = None
    
    def modify_player(self, player):
        if not self.locked and not self.opened:
            self.opened = True
            self.add_loot(player)
            print("\t{}\n".format(self.description))
        if self.opened:
            pass

    def available_actions(self):
        if self.locked:
            moves = self.adjacent_moves()
            moves.append(actions.Look())
            moves.append(actions.CheckStatus())
            moves.append(actions.UseKey(tile=self))
            moves.append(actions.UseConsumable())
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewMap())
            return moves
        else:
            moves = self.adjacent_moves()
            moves.append(actions.Look())
            moves.append(actions.CheckStatus())
            moves.append(actions.UseConsumable())
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewMap())
            return moves
        

class EnemyRoom(MapTile):
    """Class template for all enemy rooms"""
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, player):
        stealth_check = (d6() + player.stealth) - (self.enemy.advantage * 2)
        if self.enemy.is_alive():
            if self.enemy.perception < stealth_check and not player.has_attacked and not player.has_read:
                print("\n\t{} doesn't seem to notice you.\n".format(self.enemy.name))
                player.has_read = True
            if self.enemy.perception < stealth_check and not player.has_attacked and player.has_read:
                pass
            else:
                player.has_attacked = True
                dmg = self.enemy.damage + d6()
                player.hp = player.hp - dmg
                if not player.hp <= 0: 
                    print("\n\t{} does {} damage. You have {} HP remaining.\n".format(self.enemy.name, dmg, player.hp))

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self, enemy=self.enemy), actions.Attack(enemy=self.enemy), actions.CheckStatus()]
        else:
            moves = self.adjacent_moves()
            moves.append(actions.Look())
            moves.append(actions.CheckStatus())
            moves.append(actions.UseConsumable())
            moves.append(actions.ViewInventory())
            moves.append(actions.ViewMap())
            return moves

##########################
##### ENEMY TEMPLATES #####

class Enemy:
    """Class template for all enemies"""
    def __init__(self, name, hp, damage, advantage, perception):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.advantage = advantage
        self.perception = perception

    def is_alive(self):
        return self.hp > 0

###########################
##### MISC #####

notAllowed = ['lady gaga',
              'johnathan',
              'johnathan boatman',
              'mikerowave',
              'bunbun',
              'larry',
              'lawrence',
              'mike',
              'michael']

################
