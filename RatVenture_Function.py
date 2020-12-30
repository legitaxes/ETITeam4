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
    print(hero)
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
    #code goes here
    w_map = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
             [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    print(w_map)
    return w_map

def print_map(hero):
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
        print("+---"*8 + "+")
        list_map.append("+---"*8 + "+")
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
            print("|{}".format(legend), end="")
            list_map.append("|" + legend)
        print("|")
        list_map.append("|")
    print("+---"*8 + "+")
    list_map.append("+---"*8 + "+")
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
    printresult = "Day " + str(current_day) + ": " +  location
    return tile, location, printresult, current_day

def rest(hero):
    """
    Hero's HP will be resetted to its max HP
    """
    hero["hp"] = hero["max_hp"]
    print("You are fully healed.")
    print_result = "You are fully healed."
    return hero["hp"], print_result

def print_hero_stats():
    """
    Display the hero's stats and his details
    This function should return the hero's Name, Damage, Defence and HP 
    """
    # TODO Create a function that prints the stats of the hero
    # This function should print the hero's stats as well as return the stats as a dictionary object
    # labels: tasks
    # assignees: laukwangwei


def get_hero_position(hero):
    """
    This function mainly serves as a way for the program to get the position of the hero
    It should return the tile where the hero is on the map
    """
    position = hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    w_map = world_map()
    tile = w_map[x_coor][y_coor]
    return tile, hero, w_map


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
    print("Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game")
    
    #choice = int(input("Enter Choice: "))
    return "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

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
    return current_day, hero

def resume_game():
    """
    This function loads the previous game data using a json file in the same directory. 
    The previous save state should have stored variables as a json object
    This function will set the global variables in the program from the json object  
    """
    try:
        global hero, world_map, current_day
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
    print("The game has been resumed to the previous save state.")
    return "","The game has been resumed to the previous save state."


def exit_game():
    """
    This function exits the game and prints a "Bye Bye!"
    """
    # TODO Create a function that prints a message that says byebye and exit the game
    # This function should exit the python program using sys.exit()
    # labels: tasks
    return ""

def exit_game_prompt():
    """
    This function acts as a confirmation message to the user if he is in the game
    """
    # TODO Create a function that prints a confirmation message and prompts the user to select "Yes" or "No"
    # This function will act as a confirmation message to the user if he wants to really exit the game without saving
    # labels: tasks
    return ""

