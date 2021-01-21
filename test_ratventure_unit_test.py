import pytest 
from RatVenture_Function import * # update once developer starts 
from RatVenture_Main import main
from tud_test_base import set_keyboard_input, get_display_output


@pytest.fixture
def get_hero() -> theHero():
    hero = theHero()
    return hero

@pytest.fixture
def get_rat() -> theRat():
    rat = theRat()
    return rat

@pytest.fixture
def get_current_day() -> ini_current_day():
    current_day = ini_current_day() 
    return current_day

@pytest.fixture
def get_w_map() -> world_map():
    w_map = world_map()
    return w_map

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

def test_main_menu_input_1():
    set_keyboard_input([1])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", 
                        "----------------------", 
                        "1) New Game", 
                        "2) Resume Game", 
                        "3) Exit Game", 
                        "Enter Choice: ", 
                        "Starting a new game..."]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_main_menu_input_2():
    set_keyboard_input([2])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", 
                        "----------------------", 
                        "1) New Game", 
                        "2) Resume Game", 
                        "3) Exit Game", 
                        "Enter Choice: ", 
                        "Resuming from last save state..."]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_main_menu_input_3():
    set_keyboard_input([3])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", 
                        "----------------------", 
                        "1) New Game", 
                        "2) Resume Game", 
                        "3) Exit Game", 
                        "Enter Choice: ", 
                        "Exiting game..."]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_town_menu():
    value = town_menu()
    assert value == "1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"


def test_print_map(get_hero, get_w_map):
    """
    Test function of print_map Function:
        Displays the Map of the game when called
        This function should print the full layout of the map
    """

    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    location, current_day, printresult = print_day(get_hero, get_current_day)
    assert printresult == "Day " + f'{current_day}' + ": " + location
    # if actual_tile == "T":
    #     assert actual_location == "You are in a town."
    # elif actual_tile == " ":
    #     assert actual_location == "You are out in the open."
    #printresult = "Day {}: {}".format(current_day, value)
    

def test_print_hero_stats(get_hero):
    """
    Test function of print_hero_stats Function:
        Display the hero's stats and his details
        This function print the following:
        The Hero
        Damage: min damage - max damage
        Defence: defence
        HP: hp
    """

    #set keyboard input function is necessary to test the print statements
    set_keyboard_input([])
    print_hero_stats(get_hero)
    output = get_display_output()
    damage = "Damage: {}-{}".format(get_hero["min_damage"], get_hero["max_damage"])
    defence = "Defence: {}".format(get_hero["defence"])
    hp = "HP: {}".format(get_hero["hp"])
    assert output == [get_hero["name"], damage, defence, hp] 


def test_get_hero_position(get_hero, get_w_map):
    """
    Test function of get_hero_position Function:
        This function mainly serves as a way for the program to get the position of the hero
        It should return the tile where the hero is on the map
    """
    tile = get_hero_position(get_hero)   
    position = get_hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    assert tile == get_w_map[x_coor][y_coor]
    
def test_rest(get_hero):
    """
    Test function of rest function:
        This function resets the current hp of hero to the maximum hp
        It should print the following statement: "You are fully healed"
    """
    hp, print_result = rest(get_hero)
    assert hp == get_hero["hp"]
    assert print_result == "You are fully healed."

def test_new_game(get_hero, get_current_day):
    """
    This test function will test whether new_game() function is working
    It will assert the following
        > current_day
        > hero
    """
    current_day, hero, w_map = new_game()
    assert current_day == get_current_day
    assert hero["name"] == get_hero["name"]
    assert hero["min_damage"] == get_hero["min_damage"]
    assert hero["max_damage"] == get_hero["max_damage"]
    assert hero["hp"] == get_hero["hp"]
    assert hero["max_hp"] == get_hero["max_hp"]
    assert hero["defence"] == get_hero["defence"]
    assert hero["position"] == get_hero["position"]
	
def test_resume_game():
    """
    This test function will test whether resume_game() function is working
    It will assert the following:
        If there is a file from before:
            Load the file and return The game has been resumed to the previous save state.
        else: 
            return "existing file does not exist"
    """
    error, value, hero, w_map, current_day = resume_game()
    if(error == ""):
        assert value == "The game has been resumed to the previous save state." 
    else:
        assert error == FileNotFoundError
        assert value == "Existing file does not exist.\n"

def test_save_game(get_hero, get_current_day, get_w_map):
    """
    This test function will test whether the save_game() function works
    The save game function will write to the json file to store its global variable objects
    At the end of the operation, it will print "Game Saved."
    """
    set_keyboard_input([])
    save_game(get_hero, get_w_map, get_current_day)
    output = get_display_output()
    assert output == ["Game saved."]

def test_exit_game():
    """
    This test function will test whether exit_game() works
    The exit game function will only print the message and return an indicator whether it will exit
    At the end of the operation, it will print "The program will close since there are no unsaved changes" 
    """
    set_keyboard_input([])
    exit_game()
    output = get_display_output()
    assert output == ["The program will close since there are no unsaved changes."]

def test_exit_game_prompt_yes():
    """
    The test function will test whether exit_game_prompt() works
    The exit game function will only print the message and ask for a user input
    At the end of the operation, it will return an indicator to the program whether the user wants to exit the game
    """
    set_keyboard_input(["Y"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", "Enter choice: [Y/N]", "Bye bye!"]

def test_exit_game_prompt_no():
    """
    The test function will test the no option for exit game prompt to check whether the display output is correct
    At the end of the operation it should print another line of code saying "Going back to the game..."
    """
    set_keyboard_input(["N"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", "Enter choice: [Y/N]", "Going back to the game..."]

@pytest.mark.parametrize("x,y",[(1,2), (2,4),(3,7),(6,2),(5,5)])
def test_set_hero_position(get_hero, x, y):
    """
    This unit test function should test whether the hero's position is set correctly
    Test should set the correct x coordinates and y coordiantes (there should not be any x or y that is below 0 or above 7) 
    This test should test whether the returned hero_position and condition is correct
    """
    set_keyboard_input([])
    # needs to be run by itself to get output of the program
    set_hero_position(get_hero, x, y)
    condition, hero_position = set_hero_position(get_hero, x, y)
    position = get_hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    output = get_display_output()
    if y!= None:
        y_coor += y
        if y_coor < 0 or y_coor > 7:
            assert output == ["Not able to move out of map (Left/Right)!"]
            assert condition == False
            assert hero_position == get_hero["position"]
            return #test function should stop if its false
    
    if x!= None:
        x_coor += x
        if x_coor < 0 or x_coor > 7:
            assert output == ["Not able to move out of map (Up/Down)!"]
            assert condition == False
            assert hero_position == get_hero["position"]
            return #test function should stop if its false
    
    #save the updated position
    position[0] = x_coor
    position[1] = y_coor
    assert hero_position == position
    assert condition == True

@pytest.mark.parametrize("x,y",[(-1,2), (2,-4), (8,1), (3,8),(-1,0),(0,-1),(7,8)])
def test_set_hero_position_out_of_bounds(get_hero, x, y):
    """
    This unit test function should test whether the hero's position is set correctly
    Test should set the x coordinate to out of bounds and y to be a normal integer
    x out of bounds = any number not between 0 ~ 7
    y out of bounds = any number not between 0 ~ 7
    """
    set_keyboard_input([])
    condition, hero_position = set_hero_position(get_hero, x, y)
    position = get_hero["position"]
    x_coor = position[0]
    y_coor = position[1]
    output = get_display_output()
    if y!= None:
        y_coor += y
        if y_coor < 0 or y_coor > 7:
            assert output == ["Not able to move out of map (Left/Right)!"]
            assert condition == False
            assert hero_position == get_hero["position"]
            return
    
    if x!= None:
        x_coor += x
        if x_coor < 0 or x_coor > 7:
            assert output == ["Not able to move out of map (Up/Down)!"]
            assert condition == False
            assert hero_position == get_hero["position"]
            return
    
    #save the updated position
    position[0] = x_coor
    position[1] = y_coor
    assert hero_position == position
    assert condition == True

@pytest.mark.parametrize("move",[("W"), ("w")])
def test_move_hero_up(get_hero, get_w_map, move):
    """
    Test should cover 'W' part of the movement
    If the movement is an invalid one, it should print: "Not able to move out of map (Up/Down)"
    Tested on the starting point of the map [0,0]. Test should be a failing test case with the error message of Not being able to move up
    """
    # Asserting print_map function 
    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value

    set_keyboard_input([move])
    actual_status = move_hero(get_hero, get_w_map, False)
    #test_status = set_hero_position(get_hero,x=-1)
    output = get_display_output()
    # testing the actual move function
    #if(actual_status == test_status):
    if(actual_status == False):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: ", "Not able to move out of map (Up/Down)!"]
    elif(actual_status == True):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: "]

@pytest.mark.parametrize("move",[("D"), ("d")])
def test_move_hero_down(get_hero, get_w_map, move):
    """
    Test should cover 'S' part of the movement
    If the movement is an invalid one, it should print: "Not able to move out of map (Up/Down)"
    Tested on the starting point of the map [0,0]. Test should be a passing test case without needing an error message
    """
    # Asserting print_map function 
    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value
    
    #test case of move hero down, getting the print output
    set_keyboard_input([move])
    actual_status = move_hero(get_hero, get_w_map, False)
    #test_status = set_hero_position(get_hero,x=1)
    output = get_display_output()
    # Testing the actual move function
    if(actual_status == False):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: ", "Not able to move out of map (Up/Down)!"]
    elif(actual_status == True):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: "]

@pytest.mark.parametrize("move",[("A"), ("a")])
def test_move_hero_left(get_hero, get_w_map, move):
    """
    Test should cover 'A' part of the movement
    If the movement is an invalid one, it should print: "Not able to move out of map (Left/Right)"
    Tested on the starting point of the map [0,0]. Test should be a failing test case with the error message of Not being able to move left
    """
    # Asserting print_map function 
    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value

    #test case of move hero left, getting the print output
    set_keyboard_input([move])
    status = move_hero(get_hero, get_w_map, False)
    output = get_display_output()
    # Testing the actual move function
    if(status == False):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: ", "Not able to move out of map (Left/Right)!"]
    elif(status == True):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: "]

@pytest.mark.parametrize("move",[("D"), ("d")])
def test_move_hero_right(get_hero, get_w_map, move):
    """
    Test should cover 'D' part of the movement
    If the movement is an invalid one, it should print: "Not able to move out of map (Left/Right)"
    Tested on the starting point of the map [0,0]. Test should be a pass with no error message
    """
    # Asserting print_map function 
    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value

    #test case of move hero right, getting the print output
    set_keyboard_input([move])
    status = move_hero(get_hero, get_w_map, False)
    output = get_display_output()
    # Testing the actual move function
    if(status == False):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: ", "Not able to move out of map (Left/Right)!"]
    elif(status == True):
        assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: "]

@pytest.mark.parametrize("oor_input",[("k"), ("z"), ("b"), ("g"),("q"),("y"),("p")])
def test_move_hero_out_of_range(get_hero, get_w_map, oor_input):
    """
    Test should cover anything else typed to the input of the movement
    This test case tests for out of range characters not accepted by the function
    It should print Index out of Range when any input other than W A S D is inputted
    """
    # Asserting print_map function 
    position, x_coor, y_coor, legend, list_map = print_map(get_hero, get_w_map, False)
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
    assert all([a == b for a, b in zip(list_print_map, list_map)]) #this checks python list against the expected value
    
    #test case with wrong user input, getting the print output
    set_keyboard_input([oor_input])
    status = move_hero(get_hero, get_w_map, False)
    output = get_display_output()
    # Test case should always fail since other inputs are not accepted
    assert status == False
    assert output == ["W = up; A = left; S = down; D = right", 
                    "Your move: ", "Input out of range"]


# =====================================================================================================
# +++++++++++++++++++
# ++++++|Main|+++++++
# +++++++++++++++++++
# =====================================================================================================
#@pytest.mark.parametrize("choice_main_menu",[(1), (2)])
#@pytest.mark.parametrize("choice_town_menu",[(1), (2), (4), (5), (6)])
@pytest.mark.parametrize("choice_main_menu",[(1),(2)])
@pytest.mark.parametrize("choice_town_menu",[(1),(2),(4),(5), (6)])
def test_main(choice_main_menu, choice_town_menu, get_hero, get_current_day):
    """
        Testing the Main Function of the program
        This test will cover the choices in the following order:
        | 1, 1 | 1, 2 | 1, 3 | 1, 4 | 1, 5 | 1, 6 |
        | 2, 1 | 2, 2 | 2, 3 | 2, 4 | 2, 5 | 2, 6 |
        The first '1' indicates the start of a new game whereas the first '2' indicates resume game
        The second number in the matrix runs the available options in the town menu from 1 to 6
    """
    #calling print day function to  get printresults to be used under resume game function section
    location, current_day, printresult = print_day(get_hero, get_current_day)
    output = main(choice_main_menu, choice_town_menu)

    # === ========================= ===
    # === New Game Function section ===
    # === ========================= ===
    if choice_main_menu == 1:
        # View Character function
        if choice_town_menu == 1:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Starting a new game...",
                            "Day 1: You are in a town.",
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            get_hero["name"],
                            "Damage: " + f'{get_hero["min_damage"]}' + "-" + f'{get_hero["max_damage"]}',
                            "Defence: " + f'{get_hero["defence"]}',
                            "HP: " + f'{get_hero["hp"]}']
        
        # View Map function
        elif choice_town_menu == 2:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Starting a new game...",
                            "Day 1: You are in a town.",
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: "]
        # Rest function
        elif choice_town_menu == 4:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Starting a new game...",
                            "Day 1: You are in a town.",
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "You are fully healed."]
        
        # Save Game function
        elif choice_town_menu == 5:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Starting a new game...",
                            "Day 1: You are in a town.",
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "Game saved."]
        
        # Exit Game Function
        elif choice_town_menu == 6:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Starting a new game...",
                            "Day 1: You are in a town.",
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "The program will close since there are no unsaved changes."]

    # === ============================ ===
    # === Resume Game Function section ===
    # === ============================ ===
    elif choice_main_menu == 2:
        # View Character function
        if choice_town_menu == 1:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Resuming from last save state...",
                            printresult,
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            get_hero["name"],
                            "Damage: " + f'{get_hero["min_damage"]}' + "-" + f'{get_hero["max_damage"]}',
                            "Defence: " + f'{get_hero["defence"]}',
                            "HP: " + f'{get_hero["hp"]}']
        
        # View Map function
        elif choice_town_menu == 2:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Resuming from last save state...",
                            printresult,
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: "]

        # Rest function
        elif choice_town_menu == 4:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Resuming from last save state...",
                            printresult,
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "You are fully healed."]

        # Save Game function
        elif choice_town_menu == 5:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Resuming from last save state...",
                            printresult,
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "Game saved."]

        # Exit Game function
        elif choice_town_menu == 6:
            assert output == ["Welcome to Ratventure",
                            "----------------------",
                            "1) New Game",
                            "2) Resume Game",
                            "3) Exit Game",
                            "Enter Choice: ",
                            "Resuming from last save state...",
                            printresult,
                            "1) View Character\n"
                            "2) View Map\n"
                            "3) Move\n"
                            "4) Rest\n"
                            "5) Save Game\n"
                            "6) Exit Game",
                            "Enter choice: ",
                            "The program will close since there are no unsaved changes."]

@pytest.mark.parametrize("choice_main_menu",[(1),(2)])
@pytest.mark.parametrize("choice_town_menu",[(3)])
@pytest.mark.parametrize("movement", ("w","a","s","d"))
def test_main_move(choice_main_menu, choice_town_menu, movement, get_hero, get_current_day):
    """
    This main function tests the movement part of the game with various inputs such as W A S D 
    """
    location, current_day, printresult = print_day(get_hero, get_current_day)

    #set_keyboard_input([choice_main_menu, choice_town_menu])
    output, status = main(choice_main_menu, choice_town_menu, movement)
    if choice_main_menu == 1:
        if choice_town_menu == 3:
            if status == False:
                if movement == 'w':
                    assert output == ["Welcome to Ratventure",
                                    "----------------------",
                                    "1) New Game",
                                    "2) Resume Game",
                                    "3) Exit Game",
                                    "Enter Choice: ",
                                    "Starting a new game...",
                                    printresult,
                                    "1) View Character\n"
                                    "2) View Map\n"
                                    "3) Move\n"
                                    "4) Rest\n"
                                    "5) Save Game\n"
                                    "6) Exit Game",
                                    "Enter choice: ",
                                    "W = up; A = left; S = down; D = right",
                                    "Your move: ",
                                    "Not able to move out of map (Up/Down)!"]
                
                elif movement == "a":
                    assert output == ["Welcome to Ratventure",
                                    "----------------------",
                                    "1) New Game",
                                    "2) Resume Game",
                                    "3) Exit Game",
                                    "Enter Choice: ",
                                    "Starting a new game...",
                                    printresult,
                                    "1) View Character\n"
                                    "2) View Map\n"
                                    "3) Move\n"
                                    "4) Rest\n"
                                    "5) Save Game\n"
                                    "6) Exit Game",
                                    "Enter choice: ",
                                    "W = up; A = left; S = down; D = right",
                                    "Your move: ",
                                    "Not able to move out of map (Left/Right)!"]
                
                elif movement == "s":
                    assert output == ["Welcome to Ratventure",
                                    "----------------------",
                                    "1) New Game",
                                    "2) Resume Game",
                                    "3) Exit Game",
                                    "Enter Choice: ",
                                    "Starting a new game...",
                                    printresult,
                                    "1) View Character\n"
                                    "2) View Map\n"
                                    "3) Move\n"
                                    "4) Rest\n"
                                    "5) Save Game\n"
                                    "6) Exit Game",
                                    "Enter choice: ",
                                    "W = up; A = left; S = down; D = right",
                                    "Your move: ",
                                    "Not able to move out of map (Up/Down)!"]
                
                elif movement == "d":
                    assert output == ["Welcome to Ratventure",
                                    "----------------------",
                                    "1) New Game",
                                    "2) Resume Game",
                                    "3) Exit Game",
                                    "Enter Choice: ",
                                    "Starting a new game...",
                                    printresult,
                                    "1) View Character\n"
                                    "2) View Map\n"
                                    "3) Move\n"
                                    "4) Rest\n"
                                    "5) Save Game\n"
                                    "6) Exit Game",
                                    "Enter choice: ",
                                    "W = up; A = left; S = down; D = right",
                                    "Your move: ",
                                    "Not able to move out of map (Left/Right)!"]
            
            elif status == True:
                if movement == "w":
                    assert output == ["Welcome to Ratventure",
                                "----------------------",
                                "1) New Game",
                                "2) Resume Game",
                                "3) Exit Game",
                                "Enter Choice: ",
                                "Starting a new game...",
                                printresult,
                                "1) View Character\n"
                                "2) View Map\n"
                                "3) Move\n"
                                "4) Rest\n"
                                "5) Save Game\n"
                                "6) Exit Game",
                                "Enter choice: ",
                                "W = up; A = left; S = down; D = right",
                                "Your move: "] 

                elif movement == "a":
                    assert output == ["Welcome to Ratventure",
                                "----------------------",
                                "1) New Game",
                                "2) Resume Game",
                                "3) Exit Game",
                                "Enter Choice: ",
                                "Starting a new game...",
                                printresult,
                                "1) View Character\n"
                                "2) View Map\n"
                                "3) Move\n"
                                "4) Rest\n"
                                "5) Save Game\n"
                                "6) Exit Game",
                                "Enter choice: ",
                                "W = up; A = left; S = down; D = right",
                                "Your move: "] 

                elif movement == "s":
                    assert output == ["Welcome to Ratventure",
                                "----------------------",
                                "1) New Game",
                                "2) Resume Game",
                                "3) Exit Game",
                                "Enter Choice: ",
                                "Starting a new game...",
                                printresult,
                                "1) View Character\n"
                                "2) View Map\n"
                                "3) Move\n"
                                "4) Rest\n"
                                "5) Save Game\n"
                                "6) Exit Game",
                                "Enter choice: ",
                                "W = up; A = left; S = down; D = right",
                                "Your move: "]

                elif movement == "d":
                    assert output == ["Welcome to Ratventure",
                                "----------------------",
                                "1) New Game",
                                "2) Resume Game",
                                "3) Exit Game",
                                "Enter Choice: ",
                                "Starting a new game...",
                                printresult,
                                "1) View Character\n"
                                "2) View Map\n"
                                "3) Move\n"
                                "4) Rest\n"
                                "5) Save Game\n"
                                "6) Exit Game",
                                "Enter choice: ",
                                "W = up; A = left; S = down; D = right",
                                "Your move: "] 


# ==============================
# ==========SPRINT 2============
# ==============================

def test_fight_menu():
    """
    This test will test the print statement of the combat menu when fighting the rat
    It should only assert to output statements only and there will be no inputs
            1) Attack
            2) Run
    """
    value = fight_menu()
    assert value == "1) Attack\n2) Run"

def test_outdoor_menu():
    """
    This test will test the print statement of the outdoor menu text once there are no encounter or if the enemy is slained
    It should only assert the output statements as the following:
            1) View Character
            2) View Map
            3) Move
            4) Exit Game
    """
    # TODO Create a unit test function for the outdoor menu
    # This test shall only assert the print statements of the outdoor menu
    # labels: tasks, unit-test
    # milestone: 2
    # assignees: perlechen

def test_print_rat_stats(get_rat):
    """
    This test will only test the print_rat_stats() function for its print statement whether it is correct
    It should only assert the following: 
            Encounter! - Rat
            Damage: [min_damage] - [max_damage]
            Defence: [defence]
            HP: [hp]
    """
    set_keyboard_input([])
    print_rat_stats(get_rat)
    output = get_display_output()
    ratdamage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    ratdefence = "Defence: {}".format(get_rat["defence"])
    rathp = "HP: {}".format(get_rat["hp"])
    assert output == [get_rat["name"], ratdamage, ratdefence, rathp]


def test_attack(get_hero, get_rat):
    """
    This test will test the logic of the attacking system in the game
    Both the hero and the rat's damage will be rolled between their minimum attack to their maximum attack
    Then the damage will be reduced by the number of defence the enemy or the hero have
    The test will only test the damage calculation and the print output within the test function 
    After the calculation of damage, the HP of the hero and the enemy must be reduced 
        and if the hero's hp hit 0, its game over.
        and if the rat's hp hit 0, it will asser the print statement of you are victorious
    """
    # save original hp to a variable
    origin_hp = get_hero["hp"]
    origin_hp_rat = get_rat["hp"]

    set_keyboard_input([])
    attack(get_hero, get_rat, False)
    output = get_display_output()

    # do a short calculation to get the remaining HP
    hero_total_damage_test = origin_hp_rat - get_rat["hp"] 
    enemy_total_damage_test = origin_hp - get_hero["hp"] 
    # hero_hp = get_hero["hp"] - enemy_total_damage_test
    # enemy_hp = get_rat["hp"] - hero_total_damage_test

    if get_hero["hp"]  <=0:
        assert output == ["You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You ran out of HP! Game Over."]
    
    elif get_rat["hp"] <=0:
        assert output == ["You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You have " + f'{get_hero["hp"]}' + " HP left.",
                        "The " + get_rat["name"] + " is dead! You are victorious!"]
    
    else:
        assert output == ["You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You have " + f'{get_hero["hp"]}' + " HP left."]
    

# @pytest.mark.parametrize("choice", ("1","2"))
def test_encounter_1(get_rat, get_current_day, get_hero):
    """
    This test will assert the print statements that are supposed to be there such as 
        print_rat_stats(), combat menu
    It will also test for the choices made and what functions it should run after the selected choice
    IF the player move or run away from the combat, the HP of the enemy will be resetted along with printing the outdoor menu text
    If the player does anything besides moving away from the same spot, the encounter function will be ran again
    Or if the player does decide to move, he will be able to move normally without any events occuring if the tile he is standing on next is not empty
    """

    origin_hp = get_hero["hp"]
    origin_hp_rat = get_rat["hp"]

    set_keyboard_input(["1"])
    status = encounter(get_hero, get_rat)
    output = get_display_output()

    hero_total_damage_test = origin_hp_rat - get_rat["hp"] 
    enemy_total_damage_test = origin_hp - get_hero["hp"] 

    if get_rat["hp"] <= 0:
        assert status == False
        if get_hero["hp"]  <=0:
            assert output == ["Encounter! - " + get_rat["name"],
                        "Damage: " + f'{get_rat["min_damage"]}' + "-" + f'{get_rat["max_damage"]}',
                        "Defence: " + f'{get_rat["defence"]}',
                        "HP: " + f'{get_rat["hp"]}',
                        "1) Attack",
                        "2) Run",
                        "You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You ran out of HP! Game Over."]
    
        elif get_rat["hp"] <=0:
            assert output == ["Encounter! - " + get_rat["name"],
                        "Damage: " + f'{get_rat["min_damage"]}' + "-" + f'{get_rat["max_damage"]}',
                        "Defence: " + f'{get_rat["defence"]}',
                        "HP: " + f'{get_rat["hp"]}',
                        "1) Attack",
                        "2) Run",
                        "You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You have " + f'{get_hero["hp"]}' + " HP left.",
                        "The " + get_rat["name"] + " is dead! You are victorious!"]
    
        else:
            assert output == ["Encounter! - " + get_rat["name"],
                        "Damage: " + f'{get_rat["min_damage"]}' + "-" + f'{get_rat["max_damage"]}',
                        "Defence: " + f'{get_rat["defence"]}',
                        "HP: " + f'{get_rat["hp"]}',
                        "1) Attack",
                        "2) Run",
                        "You deal " + f'{hero_total_damage_test}' + " damage to the " + get_rat["name"],
                        "Ouch! The " + get_rat["name"] + " hit you for " + f'{enemy_total_damage_test}' + " damage",
                        "You have " + f'{get_hero["hp"]}' + " HP left."]

    else:
        with patch('encounter') as mock:
            assert mock.called, 'Encounter function should be called'
            #mock.assert_called_with(encounter, [get_hero, get_rat])
            #mock.assert_called_with(42)
    
@pytest.mark.parametrize("open_choice", [("1","2","3","4")])
def test_encounter_2(get_rat, get_current_day, open_choice, get_hero):
    """
    This test will assert the print statements that are supposed to be there such as 
        print_rat_stats(), combat menu
    It will also test for the choices made and what functions it should run after the selected choice
    IF the player move or run away from the combat, the HP of the enemy will be resetted along with printing the outdoor menu text
    If the player does anything besides moving away from the same spot, the encounter function will be ran again
    Or if the player does decide to move, he will be able to move normally without any events occuring if the tile he is standing on next is not empty
    This test function will focus on the running part of the encounter
    """
    
    set_keyboard_input(["2", open_choice])
    status = encounter(get_hero, get_rat)
    output = get_display_output()
    assert get_rat["hp"] == 10

    if open_choice == 1 or open_choice == 2 or open_choice == 4:
        with patch('encounter') as mock:
            assert mock.called, 'Encounter function should be called'
            #mock.assert_called_with(encounter, [get_hero, get_rat])
            #mock.assert_called_with(42)
    
    elif open_choice == 3:
        with patch('move_hero') as mock:
            #encounter(get_hero, get_rat)
            assert mock.called, 'Move Hero function should be called'
            #mock.assert_called_with(move_hero, get_hero)

        # assert output == ["Encounter! - " + get_rat["name"],
        #         "Damage: " + f'{get_rat["min_damage"]}' + "-" + f'{get_rat["max_damage"]}',
        #         "Defence: " + f'{get_rat["defence"]}',
        #         "HP: " + f'{get_rat["hp"]}',
        #         "1) Attack",
        #         "2) Run",
        #         "You run and hide",
        #         "1) View Character",
        #         "2) View Map",
        #         "3) Move",
        #         "4) Exit Game"]