import pylon, items

class Player():
    global _max_x
    global _max_y
    
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]
        self.hp = 100
        self.location_x, self.location_y = (0, 0)
        self.victory = False
        self.map = [["?"*15 for i in range(pylon._max_x)] for j in range(pylon._max_y)]

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("-=( Inventory )=-\n")
        for item in self.inventory:
            print(item, '\n')

    def add_gold(self, amt):
        for i, j in enumerate(self.inventory):
            if isinstance(j, items.Gold):
                self.inventory[i].add(amt)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        self.map[self.location_y][self.location_x] = getattr(pylon._world[(self.location_x, self.location_y)], 'id')
        print(pylon.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def view_map(self):
        print("-=( Dungeon Map )=-")
        for j in range(pylon._max_y):
            for i in range(pylon._max_x):
                if self.location_x == i and self.location_y == j:
                    print('[',self.map[j][i].center(15),']')
                else:
                    print(self.map[j][i].center(20))
            print("")

    def look(self):
        print(pylon.tile_exists(self.location_x, self.location_y).intro_text())

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("\n\tYou used {} against {}.".format(best_weapon.name, enemy.name))
        print("\tYour {} does {} damage to {}!".format(best_weapon.name, best_weapon.damage, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("\tYou killed {}!\n".format(enemy.name))
        else:
            print("\n\t{}'s HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = pylon.run(len(available_moves))
        enemy = pylon.d20()
        player = pylon.d20()
        while enemy == player:
            enemy = pylon.d20()
            player = pylon.d20()
        if player > enemy:
            print("\n\tYou ran away!")
            self.do_action(available_moves[r])
        else:
            print("\n\t{} blocked your escape!".format(tile.id))
