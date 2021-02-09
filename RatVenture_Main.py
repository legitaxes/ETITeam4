from random import randint
import json
import sys
from RatVenture_Function import * 
from tud_test_base import set_keyboard_input, get_display_output

def main(choice1=None, choice2=None, movement=None):
    # TODO Adjust the menu for Town if the town has Orb as well as for rat king
    # assignees: legitaxes
    # labels: tasks
    global current_day, hero, w_map, rat, ratking, orb
    rat = theRat()
    ratking = theRatKing()
    if choice1 != None and movement == None: # if its running as a test function
        set_keyboard_input([choice1, choice2])
        choice = main_menu()
    elif movement != None: # if its running as a test function movement
        set_keyboard_input([choice1, choice2, movement])
        choice = main_menu()
    else:
        choice = main_menu()

    if choice == 1:
        current_day, hero, w_map, orb = new_game()
    elif choice == 2:
        useless1, useless2, hero, w_map, current_day, orb = resume_game()
    elif choice == 3:
        sys.exit(0)
    else:
        main();
    
    while True:
        print_day(hero, current_day)
        position = get_hero_position(hero)
        # if the hero is in town
        if position == "T":
            if hero["position"] == orb:
                orb_town_menu()
            else:
                town_menu()

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Please enter numbers only!")
                continue

            if choice == 1:
                print_hero_stats(hero)
                if choice1 != None: # if running in test environment
                    output = get_display_output()
                    return output
            
            elif choice == 2:
                if choice1 != None: # if running in test environment
                    pos, x, y, legend, list_map = print_map(hero, w_map, orb, False)
                    output = get_display_output()
                    return output
                else:
                    print_map(hero, w_map, orb)
                
            elif choice == 3:
                hero["save"] = False
                if movement != None: # if running in test environment
                    status = move_hero(hero, w_map, orb, False)
                    current_day += 1
                    output = get_display_output()
                    return output, status
                else:
                    move_hero(hero, w_map, orb)
                    current_day += 1

            elif choice == 4:
                hero["save"] = False
                if choice1 != None: # if running in test environment
                    rest(hero)
                    current_day += 1
                    output = get_display_output()
                    return output
                else:
                    rest(hero)
                    current_day += 1

            elif choice == 5:
                if hero["position"] == orb:
                    hero["save"] = False
                    pickup_orb(hero, orb)
                    orb = [1337,1337]
                else:
                    if choice1 != None: # if running in test environment
                        save_game(hero, w_map, current_day, orb)
                        output = get_display_output()
                        return output
                    else:
                        save_game(hero, w_map, current_day, orb)
                    hero["save"] = True

            elif choice == 6:
                if hero["position"] == orb:
                    if choice1 != None: # if running in test environment
                        save_game(hero, w_map, current_day, orb)
                        output = get_display_output()
                        return output
                    else:
                        save_game(hero, w_map, current_day, orb)
                    hero["save"] = True
                else:
                    if choice1 != None: # if running in test environment
                        exit_game()
                        output = get_display_output()
                        return output
                    else:
                        if hero["save"] == True:
                            exit_game()
                            sys.exit(0)
                        else:
                            saving = input("There are unsaved changes, do you want to continue? [Y/N] ")
                            if saving.upper() == "Y":
                                exit_game()
                                sys.exit(0)
            
            elif choice == 7:
                if hero["position"] == orb:
                    if choice1 != None: # if running in test environment
                        exit_game()
                        output = get_display_output()
                        return output
                    else:
                        exit_game()
                        sys.exit(0)

            elif choice == 1337: # for debugging on teleporting to orb location 
                hero["position"] = orb

            else:
                print("Please enter a valid option!")

        # if the hero is not in town 
        # feature for combat not done yet
        elif position == " ":
            if rat["hp"] <= 0:
                outdoor_menu()
                choice = int(input("Enter choice: "))

                if choice == 1:
                    print_hero_stats(hero)
                elif choice == 2:
                    print_map(hero, w_map, orb)
                elif choice == 3:
                    hero["save"] = False
                    move_hero(hero, w_map, orb)
                    rat["hp"] = 10
                elif choice == 4:
                    if hero["save"] == True:
                        exit_game()
                        sys.exit(0)
                    else:
                        saving = input("There are unsaved changes, do you want to continue? [Y/N] ")
                        if saving.upper() == "Y":
                            exit_game()
                            sys.exit(0)
                else:
                    print("Please enter a valid option")
            else:
                if rat["hp"] > 0:
                    hero["save"] = False
                    encounter(hero, rat)

        elif position == "K":
            ratking_encounter(hero, ratking)

if __name__ == "__main__":
    main()