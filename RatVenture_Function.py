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
    """
    hero = {
    "name": "The Hero",
    "min_damage": 2,
    "max_damage": 4,
    "hp": 20,
    "max_hp": 20,
    "defence": 1,
    "position": [0, 0]
    #"orb": False,
    #"gold": 0
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
    #code goes here
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

def print_map(hero, w_map, flag=True):
    """
    Displays the Map of the game when called
    This function should print the full layout of the map
    """
    position = hero["position"]
    x_coor = position[0]
    y_coor = position[1]
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
    # TODO Create a function that prints the day of the game
    # This function should also show the location of the hero besides displaying the day
    # labels: tasks
    # assignees: laukwangwei
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
    
def new_game():
    """
    This function should display the Menu of Town since a new instance of the game is created
    Hence, the return value is a function called town_menu()  
    town_menu() function should return:
        -> Current_day as 1
        -> Initialize Hero using getHero() function
    """
    global current_day, hero
    current_day = ini_current_day()
    hero = theHero()
    w_map = world_map()
    return current_day, hero, w_map

def resume_game():
    """
    This function loads the previous game data using a json file in the same directory. 
    The previous save state should have stored variables as a json object
    This function will set the global variables in the program from the json object  
    """
    try:
        global hero, w_map, current_day
        file = open("./save.json", mode = "r")
        load_data = json.load(file)
        hero = load_data["hero"]
        w_map = load_data["w_map"]
        current_day = load_data["current_day"]
        file.close()
    except FileNotFoundError:
        print("Existing file does not exist.\n")
        return FileNotFoundError,"Existing file does not exist.\n"
        #main()
    #print("The game has been resumed to the previous save state.")
    return "","The game has been resumed to the previous save state.", hero, w_map, current_day


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
    # TODO Create a function that prints a confirmation message and prompts the user to select "Yes" or "No"
    # This function will act as a confirmation message to the user if he wants to really exit the game without saving
    # 
    # labels: tasks
    print("You have unsaved changes. Do you want to continue?")
    choice = input("Enter choice: [Y/N]")
    if(choice == "Y"):
        print("Bye bye!")
    elif(choice == "N"):
        print("Going back to the game...")
    return choice

def save_game(hero, w_map, current_day):
    """
    This function saves the current progress of the game onto an external json file named: 'save.json'
    """
    file = open("./save.json", mode = "w+")
    file.write(json.dumps({"hero": hero, "w_map": w_map, "current_day": current_day}))
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


def move_hero(hero, w_map, flag=True):
    """
    This function moves the hero based on the hero's input
    Input being: W, A, S, D | Up, Left, Down, Right
    Program should show the map of the game and prompt for user input 
    Any Flag that is False is used for Unit Test Cases ONLY
    """
    if(flag == True):
        print_map(hero, w_map)
    print("W = up; A = left; S = down; D = right")

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
        print_map(hero, w_map)


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