from random import randint
import json
import sys
from RatVenture_Function import * 

def main():
    global current_day, hero, w_map
    #hero = theHero()
    choice = main_menu()
    if choice == 1:
        current_day, hero, w_map = new_game()
    elif choice == 2:
        useless1, useless2, hero, w_map, current_day = resume_game()
    elif choice == 3:
        sys.exit(0)
    
    while True:
        print_day(hero, current_day)
        position = get_hero_position(hero)
        # if the hero is in town
        if position == "T":
            town_menu()
            choice = int(input("Enter choice: "))

            if choice == 1:
                print_hero_stats(hero)
            elif choice == 2:
                print_map(hero, w_map)
            elif choice == 3:
                move_hero(hero, w_map)
                current_day += 1
            elif choice == 4:
                rest(hero)
                current_day += 1
            elif choice == 5:
                save_game(hero, w_map, current_day)
            elif choice == 6:
                exit_game()
                sys.exit(0)

        # if the hero is not in town 
        # feature for combat not done yet
        # elif position == " ":

if __name__ == "__main__":
    main()