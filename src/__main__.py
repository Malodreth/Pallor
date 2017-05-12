import pylon, items, os
from player import Player


def play():   
    gameIsRunning = True
    
    while gameIsRunning:
        pylon.load_tiles()
        player = Player()        
        print("""
        You open your eyes. You feel dizzy and your head hurts.
        You're having trouble remembering what happened, but first...
        who are you?
        """)
        
        while player.name == '':
            player.name = input('Enter your name:\n\n>')
            os.system('cls' if os.name == 'nt' else 'clear')
            
        print("\n\tYou're {}! But where are you? And how do you get out of here?".format(player.name))
        print("\tYou look around and find yourself in a cave with a flickering torch on the wall.")
        player.move(2,5)
        
        while player.is_alive() and not player.victory:
            room = pylon.tile_exists(player.location_x, player.location_y)
            room.modify_player(player)            
            #Check player's state again for any changes
            if player.is_alive() and not player.victory:
                print("Choose an action:\n")
                available_actions = room.available_actions()
                
                for action in available_actions:
                    print(action)
                    
                action_input = input('\n>').lower()
                os.system('cls' if os.name == 'nt' else 'clear')
                
                for action in available_actions:
                    if action_input == action.hotkey:
                        player.do_action(action, **action.kwargs)
                        break
                    if action_input == 'exit' or action_input == 'stop':
                        stopPlaying(player, gameIsRunning)
                        break
                    
            if not player.is_alive():
                print("\n\tYou died!\n")
                
        totalValue = 0
        counter = 0
        
        for item in player.inventory:
            totalValue += player.inventory[counter].value
            counter += 1
            
        print("\tScore: {}\n\n".format(totalValue))
        player_input = ''
        
        while player_input != 'n' or player_input != 'y' or player_input != 'exit' or player_input != 'stop':
            print("\tWould you like to play again? y/n\n")
            player_input = input('>').lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if player_input == 'n':
                gameIsRunning = False
                break
            if player_input == 'y':
                break
            if not player.victory and player_input == 'exit' or not player.victory and player_input == 'stop':
                print("\n\tYou're already dead!")
                player_input = ''
            if player.victory and player_input == 'exit' or player.victory and player_input == 'stop':
                print("\n\tWhy would you want to do that?! Play again!\n\n")
                player_input = ''
            else:
                print("\tYou can't perform that action.\n\n")
                player_input = ''


def stopPlaying(player, state):
    print("\n\tUnable to continue any further, you decide to kill yourself.")
    best_weapon = None
    max_dmg = 0
    
    for i in player.inventory:
        if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
                
    best_weapon.damage = 100
    print("\n\tYou used {} against yourself.".format(best_weapon.name))
    print("\tYour {} does {} damage.".format(best_weapon.name, best_weapon.damage))
    player.hp -= best_weapon.damage
    

#Programme begins here
if __name__ == "__main__":
    play()       
