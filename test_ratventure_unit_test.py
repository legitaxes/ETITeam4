import pytest 
from RatVenture_Function import * # update once developer starts 

@pytest.fixture
def get_hero() -> theHero():
    hero = theHero()
    return hero

@pytest.fixture
def get_current_day() -> ini_current_day():
    current_day = ini_current_day() 
    return current_day

def test_theHero(get_hero):
    """This test function initializes hero's stats
        OUTPUT:"name": "The Hero",
                "min_damage": 2,
                "max_damage": 4,
                "hp": 20,
                "max_hp": 20,
                "defence": 1,
                "position": [0, 0]
            In a DICTIONARY
    """
    value = theHero()
    assert value['name'] == get_hero["name"]
    assert value['min_damage'] == get_hero["min_damage"]
    assert value['max_damage'] == get_hero["max_damage"]
    assert value['hp'] == get_hero["hp"]
    assert value['max_hp'] == get_hero["max_hp"]
    assert value['defence'] == get_hero["defence"]
    assert value['position'] == get_hero["position"]

def test_theRat():
    """
    This test function initializes rat's stats
        OUTPUT:"name": "Rat",
                "min_damage": 1,
                "max_damage": 3,
                "hp": 10,
                "defence": 1
            In a DICTIONARY
    """
    value = theRat()
    assert value['name'] == "Rat"
    assert value['min_damage'] == 1
    assert value['max_damage'] == 3
    assert value['defence'] == 1
    assert value['hp'] == 10


def test_world_map():
    """
    Test function of initializing world_map():
        The map will be initialized upon running this function
    """
    value = world_map()
    expected = [['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
                [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
                
    assert len(value) == len(expected)
    assert all([a == b for a, b in zip(value, expected)]) #this checks python list against the expected value

def test_main_menu():
    value = main_menu()
    assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_town_menu():
    value = town_menu()
    assert value == "1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"


def test_print_map(get_hero):
    """
    Test function of print_map Function:
        Displays the Map of the game when called
        This function should print the full layout of the map
    """

    position, x_coor, y_coor, legend, list_map = print_map(get_hero)
    #theHero = print_hero_stats()
    w_map = world_map()
    pos = get_hero["position"]
    assert position == pos
    assert x_coor == pos[0]
    assert y_coor == pos[1]
    list_print_map = []
    for x in range(8):
        list_print_map.append("+---"*8 + "+")
        for y in range(8):
            legend = "   "
            if w_map[x][y] == "T":
                if x == x_coor and y == y_coor:
                    legend = "H/T"
                    #assert legend == "H/T"
                else:
                    legend = " T "
                    #assert legend == " T "
            elif w_map[x][y] == "K":
                if x == x_coor and y == y_coor:
                    legend = "H/K"
                    #assert legend == "H/K"
                else:
                    legend = " K " 
                    #assert legend == " K "
            else:
                if x == x_coor and y == y_coor:
                    legend = " H "
                    #assert legend == " H "
            list_print_map.append("|" + legend)
        list_print_map.append("|")
    list_print_map.append("+---"*8 + "+")
    # assert both lists
    print(list_map)
    print(list_print_map)
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value

def test_print_day(get_hero, get_current_day):
    """
    Test function of print_day Function:
        Display the tile the hero is at and display whether the hero is in town or out in open
    """
    actual_tile, actual_location, printresult, current_day = print_day(get_hero, get_current_day)

    if actual_tile == "T":
        assert actual_location == "You are in a town."
    elif actual_tile == " ":
        assert actual_location == "You are out in the open."
    #printresult = "Day {}: {}".format(current_day, value)
    assert printresult == "Day " + str(current_day) + ": " + actual_location

def test_print_hero_stats(get_hero):
    """
    Test function of print_hero_stats Function:
        Display the hero's stats and his details
        This function should return the hero's Name, Damage, Defence and HP 
    """
    
    assert print_hero_stats(theHero()) == str(get_hero["name"]) + "Damage:" + str(get_hero["min_damage"]) + "-" + str(get_hero["max_damage"]) + str(get_hero["defence"]) + str(get_hero["hp"])

def test_get_hero_position(get_hero):
    """
    Test function of get_hero_position Function:
        This function mainly serves as a way for the program to get the position of the hero
        It should return the tile where the hero is on the map
    """
    tile, theHero, w_map = get_hero_position(get_hero)   
    position = theHero["position"]
    assert theHero["position"] == get_hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    assert tile == w_map[x_coor][y_coor]
    
def test_rest(get_hero):
    """
    Test function of rest function:
        This function resets the current hp of hero to the maximum hp
        It should print the following statement: "You are fully healed"
    """
    hp, print_result = rest(get_hero)
    assert hp == get_hero["hp"]
    assert print_result == "You are fully healed."

def test_new_game():
    """
    This test function will test whether new_game() function is working
    It will assert the following
        > current_day
        > hero
    """
    # TODO Create a unit test for new game function
    # This unit test function shall initialize a new game and will assert two variables
    # > current_day
    # > hero
    # labels: tasks
    # milestone: 1
    

def test_resume_game():
    """
    This test function will test whether resume_game() function is working
    It will assert the following:
        If there is a file from before:
            Load the file and return The game has been resumed to the previous save state.
        else: 
            return "existing file does not exist"
    """
    # TODO Create a unit test for resume game function
    # This unit test function shall resume a previous save state game and will assert the return values of resume_game()
    # labels: tasks
    # milestone: 1

def test_save_game():
    """
    This test function will test whether the save_game() function works
    The save game function will write to the json file to store its global variable objects
    At the end of the operation, it will print "Game Saved."
    """
    # TODO Create a unit test for save game function
    # This unit test function will save the game onto a json file object
    # The json file shall store global variables as a json string
    # labels: tasks
    # milestone: 1

def test_exit_game():
    """
    This test function will test whether exit_game() works
    The exit game function will only print the message and return an indicator whether it will exit
    At the end of the operation, it will print "The program will close since there are no unsaved changes" 
    """
    # TODO Create a unit test for exit game function
    # This unit test function will exit the game on demand
    # labels: tasks
    # milestone: 1

def test_exit_game_prompt():
    """
    The test function will test whether exit_game_prompt() works
    The exit game function will only print the message and ask for a user input
    At the end of the operation, it will return an indicator to the program whether the user wants to exit the game
    """
    # TODO Create a unit test for prompting the user when exiting the game
    # This unit test will assert a print statement upon running
    # labels: tasks
    # milestone: 1
