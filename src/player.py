import pylon, items

class Player():
    global _max_x
    global _max_y
    
    def __init__(self):
        self.name = ''
        self.inventory = [items.Gold(15), items.Mushroom(), items.Mushroom(), items.Rock()]
        self.hp = 100
        self.stealth = 12
        self.location_x, self.location_y = (0, 0)
        self.victory = False
        self.has_attacked = False
        self.has_read = False
        self.map = [["?"*15 for i in range(pylon._max_x)] for j in range(pylon._max_y)]

    def is_alive(self):
        return self.hp > 0

    def check_status(self):
        counter = 0
        for item in self.inventory:
            counter += 1
        print("\n\t\t---=( Player Status ) =---\n")
        print("\tName: {}\n\tHP: {}/100\n\n\tCarrying {} items\n\n\tSKILLS\n\t=====\n\tStealth: {}\n".format(self.name, self.hp, counter, self.stealth))

    def print_inventory(self):
        print("\n\t\t---=( Inventory )=---\n")
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
        print("\n\t\t---=( Dungeon Map )=---\n")
        for j in range(pylon._max_y):
            for i in range(pylon._max_x):
                if self.location_x == i and self.location_y == j:
                    print('\t\t  [', self.map[j][i].center(15), ']')
                else:
                    print('\t\t ', self.map[j][i].center(20))
            print("")

    def look(self):
        print(pylon.tile_exists(self.location_x, self.location_y).intro_text())

    def use_consumable(self):
        best_food = None
        max_heal = 0
        modifier = 0
        heal_amt = 0
        for i in self.inventory:
            if isinstance(i, items.Consumable):
                if i.healing > max_heal:
                    max_heal = i.healing
        for i in self.inventory:
            if isinstance(i, items.Consumable):
                if i.healing == max_heal:
                    best_food = i
                    self.inventory.remove(i)
                    break

        if best_food == None:
            print("\n\tYou have nothing to eat.\n")
        else:
            print("\n\tYou ate a {}.".format(best_food.name))
            if self.hp == 100:
                print("\tYou don't feel any different...\n")
            if self.hp < 100:
                self.hp += best_food.healing
                heal_amt = best_food.healing
                if self.hp > 100:
                    modifier = self.hp - 100
                    self.hp -= modifier
                    heal_amt = best_food.healing - modifier
                print("\tYou've been healed for {} points! You have {} HP.\n".format(heal_amt, self.hp))
        

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        self.has_attacked = True
        print("\n\tYou used {} against {}.".format(best_weapon.name, enemy.name))
        print("\tYour {} does {} damage!".format(best_weapon.name, best_weapon.damage))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("\tYou killed {}!\n".format(enemy.name))
            self.has_read = False
            self.has_attacked = False
        else:
            print("\n\t{}'s HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile, enemy):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = pylon.run(len(available_moves))
        stealth_check = (pylon.d6() + self.stealth) - (enemy.advantage * 2)
        if enemy.perception < stealth_check and not self.has_attacked:
            enemy.advantage += 4
            self.has_read = False
            print("\n\tYou ran away!")
            self.do_action(available_moves[r])
        else:
            enemy_roll = pylon.d20() + enemy.advantage
            player_roll = pylon.d20()
            while enemy_roll == player_roll:
                enemy_roll = pylon.d20()
                player_roll = pylon.d20()
            if player_roll > enemy_roll:
                enemy.advantage += 2
                self.has_read = False
                self.has_attacked = False
                print("\n\tYou ran away!")
                self.do_action(available_moves[r])
            else:
                enemy.advantage += 2
                print("\n\t{} blocked your escape!".format(tile.id))
