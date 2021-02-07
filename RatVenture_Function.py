from random import randint
import json
import sys


# Initialize Hero and Enemy Stats
def theHero():
    """
    Initialize the Hero with the following:
        Name: The Hero
        HP: 20
        Min Damage: 2
        Max Damage: 4
        HP: 20
        MAX HP: 20
        Defence: 1
        Position: [0, 0]
        Orb: False
    """
    hero = {
    "name": "The Hero",
    "min_damage": 2,
    "max_damage": 4,
    "hp": 20,
    "max_hp": 20,
    "defence": 1,
    "position": [0, 0],
    "orb": False,
    "save": True
    }
    #print(hero)
    return hero

#initialize current day as 1 
def ini_current_day():
    global current_day
    current_day = 1
    return current_day

def theRat():
    """Initialize the rat with the following:
        Name: Rat
        HP: 10
        Min Damage: 1
        Max Damage: 3
        Defence: 1
    """
    rat = {
    "name": "Rat",
    "hp": 10,
    "min_damage": 1,
    "max_damage": 3,
    "defence": 1
    }

    return rat

def world_map():
    """
    Initialize the World Map to be like this:
            ['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']
    """
    global w_map
    #code goes here, town [1,3], [2,5], [3,1], [6,4]
    w_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    #print(w_map)
    return w_map

def print_map(hero, w_map, orb, flag=True):
    """
    Displays the Map of the game when called
    This function should print the full layout of the map
    """
    # TODO Add the new requirement of showing the orb in the town
    # assignees: legitaxes
    # labels: tasks
    position = hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    orb_x_coor = orb[0]
    orb_y_coor = orb[1]

    list_map = []
    w_map = world_map()
    for x in range(8):
        if flag == False:
            list_map.append("+---"*8 + "+")
        else:
            print("+---"*8 + "+")
        for y in range(8):
            legend = "   "
            if w_map[x][y] == "T":
                legend = " T "
                if x == x_coor and y == y_coor:
                    legend = "H/T"
                    if orb_x_coor == x_coor and orb_y_coor == y_coor:
                        legend = "H/O"
                # elif orb_x_coor == x_coor and orb_y_coor == y_coor:
                #     legend = "H/O"
                elif x == orb_x_coor and y == orb_y_coor:
                    legend = "T/O"
            elif w_map[x][y] == "K":
                legend = " K "
                if x == x_coor and y == y_coor:
                    legend = "H/K"
            else:
                if x == x_coor and y == y_coor:
                    legend = " H "
            if flag == True:
                print("|{}".format(legend), end="")
                #print("|" + legend, sep="")
            else:
                 list_map.append("|" + legend)
        if flag == False: 
            list_map.append("|")
        else:
            print("|")
    if flag == False:
        list_map.append("+---"*8 + "+")
    else:
        print("+---"*8 + "+")
    # list of items returned below are mainly used for unit test
    # they do not serve any other extra purpose
    return position, x_coor, y_coor, legend, list_map

def print_day(hero, current_day):
    """
    Display the details of the location the hero is at and display the current day of the game
    """
    tile = get_hero_position(hero)
    location = ""
    if tile == "T":
        location = "You are in a town."
    elif tile == " ":
        location = "You are out in the open."
    print("Day {}: {}".format(current_day, location))
    printresult = "Day " + f'{current_day}' + ": " +  location
    return location, current_day, printresult

def rest(hero):
    """
    Hero's HP will be resetted to its max HP
    """
    hero["hp"] = hero["max_hp"]
    print("You are fully healed.")
    print_result = "You are fully healed."
    return hero["hp"], print_result

def print_hero_stats(hero):
    """
    Display the hero's stats and his details
    This function should return the hero's Name, Damage, Defence and HP 
    """

    print(hero["name"])
    print("Damage: {}-{}".format(hero["min_damage"], hero["max_damage"]))
    print("Defence: {}".format(hero["defence"]))
    print("HP: {}".format(hero["hp"]))
    #return hero


def get_hero_position(hero):
    """
    This function mainly serves as a way for the program to get the position of the hero
    It should return the tile where the hero is on the map
    """
    position = hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    #w_map = world_map()
    tile = w_map[x_coor][y_coor]
    return tile


def main_menu():
    """
    Displays the Main Menu of the game
    The menu should show: 
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:
    """
    print("Welcome to Ratventure")
    print("----------------------")
    print("1) New Game")
    print("2) Resume Game")
    print("3) Exit Game")
    choice = int(input("Enter Choice: "))
    if(choice < 1 or choice > 3):
        print("Please enter a valid choice")
    else:
        if(choice == 1):
            print("Starting a new game...")
        elif(choice == 2):
            print("Resuming from last save state...")
        elif(choice == 3):
            print("Exiting game...")
    return choice

def town_menu():
    """
    This function should display the menu of Town
    Hence, the following values should be returned:
        1) View Character
        2) View Map
        3) Move
        4) Rest
        5) Save Game
        6) Exit Game
    """
    print("1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game")
    return "1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"
    
def orb_town_menu():
    """
    This function should display the menu of Town when there is an orb in the town
    Hence, the following values should be returned:
        1) View Character
        2) View Map
        3) Move
        4) Rest
        5) Pick Up Orb
        6) Save Game
        7) Exit Game
    """
    print("1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Pick up Orb of Power\n6) Save Game\n7) Exit Game")
    return "1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Pick up Orb of Power\n6) Save Game\n7) Exit Game"

def new_game():
    """
    This function should display the Menu of Town since a new instance of the game is created
    Hence, the return value is a function called town_menu()  
    town_menu() function should return:
        -> Current_day as 1
        -> Initialize Hero using getHero() function
    """
    global current_day, hero, orb
    current_day = ini_current_day()
    hero = theHero()
    w_map = world_map()
    orb = generate_orb()
    return current_day, hero, w_map, orb

def resume_game():
    """
    This function loads the previous game data using a json file in the same directory. 
    The previous save state should have stored variables as a json object
    This function will set the global variables in the program from the json object  
    """
    # TODO Adjust Resume game to load orb data
    # assignees: legitaxes
    # labels: tasks
    try:
        global hero, w_map, current_day, orb
        file = open("./save.json", mode = "r")
        load_data = json.load(file)
        hero = load_data["hero"]
        w_map = load_data["w_map"]
        current_day = load_data["current_day"]
        orb = load_data["orb"]
        file.close()
    except FileNotFoundError:
        print("Existing file does not exist.\n")
        return FileNotFoundError,"Existing file does not exist.\n"
        #main()
    #print("The game has been resumed to the previous save state.")
    return "","The game has been resumed to the previous save state.", hero, w_map, current_day, orb


def exit_game():
    """
    This function exits the game and prints a notification message saying it will now close
    """
    print("The program will close since there are no unsaved changes.")
    return "The program will close since there are no unsaved changes."

def exit_game_prompt():
    """
    This function acts as a confirmation message to the user if he is in the game
    If the user typed Y
    The program will exit and print a bye bye! message
    or N: will go back to the previous menu
    """
    print("You have unsaved changes. Do you want to continue?")
    choice = input("Enter choice: [Y/N]")
    if(choice == "Y"):
        print("Bye bye!")
    elif(choice == "N"):
        print("Going back to the game...")
    return choice

def save_game(hero, w_map, current_day, orb):
    """
    This function saves the current progress of the game onto an external json file named: 'save.json'
    """
    # TODO Adjust Save game to save orb data
    # assignees: legitaxes
    # labels: tasks
    file = open("./save.json", mode = "w+")
    file.write(json.dumps({"hero": hero, "w_map": w_map, "current_day": current_day, "orb": orb}))
    file.close()
    print("Game saved.")
    return "Game saved."

def set_hero_position(hero, x=None, y=None):
    """
    This function should set the hero's position and return true if it is a valid movement
    Else it should return false if the hero is out of bounds in the map
    Both scenarios should return the hero's position to check against the test cases
    """
    position = hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    if y != None:
        y_coor += y
        if y_coor < 0 or y_coor > 7:
            print("Not able to move out of map (Left/Right)!")
            return False, hero["position"]
    if x != None:
        x_coor += x
        if x_coor < 0 or x_coor > 7:
            print("Not able to move out of map (Up/Down)!")
            return False, hero["position"]
    #save the updated hero position
    position[0] = x_coor
    position[1] = y_coor
    hero["position"] = position
    return True, hero["position"]


def move_hero(hero, w_map, orb, flag=True):
    """
    This function moves the hero based on the hero's input
    Input being: W, A, S, D | Up, Left, Down, Right
    Program should show the map of the game and prompt for user input 
    Any Flag that is False is used for Unit Test Cases ONLY
    """
    if(flag == True):
        print_map(hero, w_map, orb)
    print("W = up; A = left; S = down; D = right")
    if(flag == None): #ensure the function have ran
        return
    while True:
        move = input("Your move: ").lower()
        if move == "w":
            status, pos = set_hero_position(hero, x=-1)
            if status == False:
                if flag == False:
                    return False
                continue
            elif status == True:
                if flag == False:
                    return True
                break
        elif move == "a":
            status, pos = set_hero_position(hero, y=-1)
            if status == False:
                if flag == False:
                    return False
                continue
            elif status == True:
                if flag == False:
                    return True
                break
        elif move == "s":
            status, pos = set_hero_position(hero, x=1)
            if status == False:
                if flag == False:
                    return False
                continue
            elif status == True:
                if flag == False:
                    return True
                break
        elif move == "d":
            status, pos = set_hero_position(hero, y=1)
            if status == False:
                if flag == False:
                    return False
                continue
            elif status == True:
                if flag == False:
                    return True
                break
        elif(flag == False):
            print("Input out of range")
            return False
        else:
            print("Input out of range")
    if(flag == False):
        return True
    else:
        print_map(hero, w_map, orb)


# ==============================
# ==========SPRINT 2============
# ==============================

"""
Sprint 2 of the development will add the combat system to the game as well as making the game functional and completely playable
"""

def attack(hero, rat, flag=True):
    hero_damage = randint(hero["min_damage"], hero["max_damage"])
    enemy_damage = randint(rat["min_damage"], rat["max_damage"])

    hero_total_damage = hero_damage - rat["defence"]
    rat_total_damage = enemy_damage - hero["defence"]

    if rat_total_damage <= 0:
        rat_total_damage = 0
    # calculate the hp after damage
    rat["hp"] = rat["hp"] - hero_total_damage
    hero["hp"] = hero["hp"] - rat_total_damage
    print("You deal {} damage to the {}".format(hero_total_damage, rat["name"]))
    print("Ouch! The {} hit you for {} damage".format(rat["name"],rat_total_damage))

    if hero["hp"] <= 0:
        print("You ran out of HP! Game over.")
        if flag == True:
            sys.exit(0)
    print("You have {} HP left.".format(hero["hp"]))
    if rat["hp"] <= 0:
        print("The {} is dead! You are victorious!".format(rat["name"]))
        

def fight_menu():
    """
    This function should display the Combat Menu when fighting a rat
    Hence, the following values should be return:
        1) Attack
        2) Run
    """
    print("1) Attack\n2) Run")

def print_rat_stats(rat):
    """
    Display the rat's Stats and his details
    This function should return the rat's Name, Damage, Defence and HP
    """
    print("Encounter! - {}".format(rat["name"]))
    print("Damage: {}-{}".format(rat["min_damage"], rat["max_damage"]))
    print("Defence: {}".format(rat["defence"]))
    print("HP: {}".format(rat["hp"]))

def encounter(hero, rat, flag=True):
    print_rat_stats(rat)
    fight_menu()
    if flag == None: #check if function is called
        return
    #encounter_choice = int(input("Enter choice: "))
    try:
        encounter_choice = int(input("Enter choice: "))
    except ValueError:
        print("Please input a number!")
        return

    global current_day, world_map

    if encounter_choice == 1:
        attack(hero, rat)
        if rat["hp"] <= 0:
            #position = hero["position"]
            return
        if flag == False: #if its running as unit test function, print rat stats and menu again
            # print_rat_stats(rat)
            # fight_menu()
            encounter(hero, rat, None)
        else:
            encounter(hero, rat)
    
    if encounter_choice == 2:
        print("You run and hide.")
        rat["hp"] = 10
        outdoor_menu()
        outdoor_choice = int(input("Enter choice: "))

        if outdoor_choice == 1 or outdoor_choice == 2:
            if flag == False:
                encounter(hero, rat, None)
            else:
                encounter(hero, rat)
        
        elif outdoor_choice == 3:
            if flag == False:
                move_hero(hero, w_map, orb, None)
                rat["hp"] = 10
                current_day += 1
            else:
                move_hero(hero, w_map, orb)
                rat["hp"] = 10
                current_day += 1

        elif outdoor_choice == 4:
            if flag == False:
                return
            if hero["save"] == True:
                exit_game()
                sys.exit(0)
            else:
                saving = input("There are unsaved changes, do you want to continue? [Y/N] ")
                if saving.upper() == "Y":
                    exit_game()
                    sys.exit(0)
    else:
        print("Please enter a valid option!")
        return

def outdoor_menu():
    """
    This function should display the menu of Outdoor
    Hence, the following values should be returned:
        1) View Character
        2) View Map
        3) Move
        4) Exit Game
    """
    print("1) View Character\n2) View Map\n3) Move\n4) Exit Game")
    #return "1) View Character\n2) View Map\n3) Move\n4) Exit Game"


# ==============================
# ==========SPRINT 3============
# ==============================
# Requirement changes / New functions 

def generate_orb(i=randint(1,4)):
    """
    generate_orb() generates an orb in any of the town location randomly
    Function should return the random orb location
    """
    global orb
    #town locations [1,3], [2,5], [3,1], [6,4]
    orblocation = []
    switch = {
        1: [1,3],
        2: [2,5],
        3: [3,1],
        4: [6,4]
    }
    orblocation = switch.get(i, "Invalid input of number")
    orb = orblocation
    return orblocation

def pickup_orb(hero, orb):
    """
    Print Orb Function will print the following lines when the orb is picked up
    This function should also set the hero's Orb to be True
        "You found the Orb of Power!"
        "Your attack rose by 5!"
        "Your defence rose by 5!"
    """
    hero_pos = hero["position"]
    orb_pos = orb
    if hero_pos == orb_pos:
        hero["min_damage"] += 5
        hero["max_damage"] += 5
        hero["defence"] += 5
        hero["orb"] = True
        print("You found the Orb of Power!\n" "Your attack rose by 5!\n" "Your defence rose by 5!")
    else:
        print("You are not allowed to pick up the Orb!")

def theRatKing():
    """
    This function initializes the rat king stats and the dictionary for rat king
    """
    ratking = {
    "name": "Rat King",
    "min_damage": 8,
    "max_damage": 12,
    "hp": 25,
    "defence": 5
    }
    return ratking

def print_ratking_stats(ratking):
    """
    The function prints the Rat King Stats as the following:
        "Encounter! - Rat King"
        "Damage: MinDamage - MaxDamage"
        "Defence: DefenceLevel"
        "HP: HP"
    """
    print("Encounter! - {}".format(ratking["name"]))
    print("Damage: {}-{}".format(ratking["min_damage"], ratking["max_damage"]))
    print("Defence: {}".format(ratking["defence"]))
    print("HP: {}".format(ratking["hp"]))

def win_game():
    """
    The function should print the following:
        "The Rat King is Dead! You are Victorious!"
        "Congratulations, you have defeated the Rat King"
        "The world is saved! You win!"
    """
    print("The Rat King is dead! You are victorious!\nCongratulations, you have defeated the Rat King\nThe world is saved! You win!")

def ratking_attack(hero, ratking, flag=True):
    """
    Essentially another attack() function but for RatKing
    This function will check whether the player is holding the orb as well
    """
    if hero["orb"] == True:
        hero_damage = randint(hero["min_damage"], hero["max_damage"])
        hero_total_damage = hero_damage - ratking["defence"]
        if hero_total_damage < 0:
            hero_total_damage = 0
        ratking["hp"] = ratking["hp"] - hero_total_damage
        print("You deal {} damage to the {}".format(hero_total_damage, ratking["name"]))
    else: 
        print("You do not have the Orb of Power - the {} is immune!".format(ratking["name"]))
        print("You deal 0 damage to the {}".format(ratking["name"]))
    
    ratking_damage = randint(ratking["min_damage"], ratking["max_damage"])
    ratking_total_damage = ratking_damage - hero["defence"]
    hero["hp"] = hero["hp"] - ratking_total_damage
    print("Ouch! The {} hit you for {} damage".format(ratking["name"], ratking_total_damage))
    
    if hero["hp"] <= 0:
        print("You ran out of HP! Game over.")
        if flag == False:
            return
        sys.exit(0)
    
    print("You have {} HP left".format(hero["hp"]))

    if ratking["hp"] <= 0:
        win_game()


def ratking_encounter(hero, ratking, flag=True):
    """
    Essentially the same as encounter() from before but this is for RatKing
    """
    print_ratking_stats(ratking)
    fight_menu()
    if flag == None:
        return
    encounter_choice = int(input("Enter choice: "))
    global current_day, w_map

    if encounter_choice == 1:
        if flag == False:
            ratking_attack(hero, ratking, False)
            ratking_encounter(hero, ratking, None)
        else:
            ratking_attack(hero, ratking)
            ratking_encounter(hero, ratking)

    elif encounter_choice == 2:
        print("You run and hide.")
        ratking["hp"] = 25
        outdoor_menu()
        outdoor_choice = int(input("Enter choice: "))

        if outdoor_choice == 1 or outdoor_choice == 2:
            if flag == False:
                ratking_encounter(hero, ratking, None)
            else:
                ratking_encounter(hero, ratking)
        elif outdoor_choice == 3:
            if flag == False:
                move_hero(hero, w_map, orb, None)
                current_day += 1
            else:
                move_hero(hero, w_map, orb)
                current_day += 1

        elif outdoor_choice == 4:
            if flag == False:
                return
            if hero["save"] == True:
                exit_game()
                sys.exit(0)
            else:
                saving = input("There are unsaved changes, do you want to continue? [Y/N] ")
                if saving.upper() == "Y":
                    exit_game()
                    sys.exit(0)


