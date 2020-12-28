from random import randint
import json
import sys

# Initialize Hero and Enemy Stats
def hero():
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
    "position": [0, 0],
    #"orb": False,
    #"gold": 0
    }
    print(hero)
    return hero

def rat():
    # TODO: Create a function that initalizes the rat stats
    # The function should initialize the rat's stats such as name, hp, defence, potential damage
    # refer to the unit test function to know what to code
    # 
    # labels: tasks
    # assignees: laukwangwei
    # milestone: 1
    """Initialize the rat with the following:
        Name: Rat
        HP: 10
        Min Damage: 1
        Max Damage: 3
        Defence: 1
    """
    # code goes here
    rat = {
    "name": "Rat",
    "hp": 10,
    "min_damage": 1,
    "max_damage": 3,
    "defence": 1
    }

    return rat

def world_map():
    # TODO: Create a function that initializes the world map using 2D array
    # A world map should be initialized as a 2D array according to how it looks like in the document
    # Refer to the unit testing function to know what to code here
    # labels: tasks
    # assignees: legitaxes
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
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    print(w_map)
    return w_map

def print_map():
    """
    Displays the Map of the game when called
    This function should print the full layout of the map
    """
    # TODO: Create a function that prints the map of the game 
    # The map will be printed upon calling displaying details of the map 
    # Details such as the town position and hero position should be displayed
    # labels: tasks
    # assignees: legitaxes

    return print_w_map

def print_day():
    """
    Display the tile the hero is at and display whether the hero is in town or out in open
    """
    # TODO: Create a function that prints the day of the game
    # This function should also show the location of the hero besides displaying the day
    # labels: tasks
    # assignees: laukwangwei

    return printday

def print_hero_stats():
    """
    Display the hero's stats and his details
    This function should return the hero's Name, Damage, Defence and HP 
    """
    # TODO: Create a function that prints the stats of the hero
    # This function should print the hero's stats as well as return the stats as a dictionary object
    # labels: tasks
    # assignees: laukwangwei

def get_hero_position():
    """
    This function mainly serves as a way for the program to get the position of the hero
    It should return the tile where the hero is on the map
    """
    # TODO: Create a function that gets the hero's position
    # This function should only serve as a way for the program to get the position of the hero
    # labels: tasks
    # assignees: legitaxes
    

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
    print("\n Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:")
    return "\n Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:"

def new_game():
    # TODO: figure out the structure of the program and how it should be ran
    # also figure out how test script should work with @python.mark.parametrize() for each feature in the menu
    # labels: research
    # assignees: legitaxes
    # milestone: 1
    """
    This function should display the Menu of Town since a new instance of the game is created
    Hence, the return value is a function called town_menu()  
    town_menu() function should return:
        Day 1: You are in a town.
        1) View Character
        2) View Map
        3) Move
        4) Rest
        5) Save Game
        6) Exit Game
        Enter choice:
    """
    
    return town_menu()

def resume_game():
    """
    Add comments here, include a todo comment
    """
    return ""


def exit_game():
    """
    Add comments here, include a todo comment
    """
    return ""

def exit_game_prompt():
    """
    Add comments here, include a todo comment
    """
    return ""

