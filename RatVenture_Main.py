from random import randint
import json
import sys
from RatVenture_Function import * 
from tud_test_base import set_keyboard_input, get_display_output

def main(choice1=None, choice2=None, movement=None):
    global current_day, hero, w_map
    #hero = theHero()
    if choice1 != None and movement == None: # if its running as a test function
        set_keyboard_input([choice1, choice2])
        choice = main_menu()
    elif movement != None: # if its running as a test function movement
        set_keyboard_input([choice1, choice2, movement])
        choice = main_menu()
    else:
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
                if choice1 != None: # if its running as pytest function
                    output = get_display_output()
                    return output
            
            elif choice == 2:
                if choice1 != None:
                    pos, x, y, legend, list_map = print_map(hero, w_map, False)
                    output = get_display_output()
                    return output
                else:
                    print_map(hero, w_map)
                
            elif choice == 3:
                if movement != None:
                    status = move_hero(hero, w_map, False)
                    current_day += 1
                    output = get_display_output()
                    return output, status
                else:
                    move_hero(hero, w_map)
                    current_day += 1

            elif choice == 4:
                if choice1 != None:
                    rest(hero)
                    current_day += 1
                    output = get_display_output()
                    return output
                else:
                    rest(hero)
                    current_day += 1

            elif choice == 5:
                if choice1 != None:
                    save_game(hero, w_map, current_day)
                    output = get_display_output()
                    return output
                else:
                    save_game(hero, w_map, current_day)

            elif choice == 6:
                exit_game()
                sys.exit(0)

        # if the hero is not in town 
        # feature for combat not done yet
        # elif position == " ":

if __name__ == "__main__":
    main()