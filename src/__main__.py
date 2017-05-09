import pylon, items, os
from player import Player

def play():
    pylon.load_tiles()
    player = Player()
    #These lines load the starting room and display the text
    print("\n\tYou find yourself in a cave with a flickering torch on the wall.")
    player.move(2,5)
    while player.is_alive() and not player.victory:
        room = pylon.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        #Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            os.system('cls' if os.name == 'nt' else 'clear')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
        if not player.is_alive():
            print("\n\tYou died!\n")
    totalValue = 0
    counter = 0
    for item in player.inventory:
        totalValue += player.inventory[counter].value
        counter += 1
    print("\tScore: {}\n".format(totalValue))

if __name__ == "__main__":
    play()
        
