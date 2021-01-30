from random import randint
import json
import sys
from RatVenture_Function import * 
from tud_test_base import set_keyboard_input, get_display_output

def main(choice1=None, choice2=None, movement=None):
    # TODO Complete the main function after the combat system is done
    # This is the remaining 50% of the main function which handles the instance when hero moves to an empty tile
    # labels: tasks
    # milestone: 2
    
    global current_day, hero, w_map, rat
    rat = theRat()
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
                if choice1 != None: # if running in test environment
                    output = get_display_output()
                    return output
            
            elif choice == 2:
                if choice1 != None: # if running in test environment
                    pos, x, y, legend, list_map = print_map(hero, w_map, False)
                    output = get_display_output()
                    return output
                else:
                    print_map(hero, w_map)
                
            elif choice == 3:
                if movement != None: # if running in test environment
                    status = move_hero(hero, w_map, False)
                    current_day += 1
                    output = get_display_output()
                    return output, status
                else:
                    move_hero(hero, w_map)
                    current_day += 1

            elif choice == 4:
                if choice1 != None: # if running in test environment
                    rest(hero)
                    current_day += 1
                    output = get_display_output()
                    return output
                else:
                    rest(hero)
                    current_day += 1

            elif choice == 5:
                if choice1 != None: # if running in test environment
                    save_game(hero, w_map, current_day)
                    output = get_display_output()
                    return output
                else:
                    save_game(hero, w_map, current_day)

            elif choice == 6:
                if choice1 != None: # if running in test environment
                    exit_game()
                    output = get_display_output()
                    return output
                else:
                    exit_game()
                    sys.exit(0)

        # if the hero is not in town 
        # feature for combat not done yet
        elif position == " ":
            if rat["hp"] <= 0:
                outdoor_menu()
                choice = int(input("Enter choice: "))

                if choice == 1:
                    print_hero_stats(hero)
                elif choice == 2:
                    print_map(hero, w_map)
                elif choice == 3:
                    move_hero(hero, w_map)
                    rat["hp"] = 10
                elif choice == 4:
                    sys.exit(0)
            else:
                if rat["hp"] > 0:
                    encounter(hero, rat)

if __name__ == "__main__":
    main()