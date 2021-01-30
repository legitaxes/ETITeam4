import pytest 
from RatVenture_Function import * # update once developer starts 
from RatVenture_Main import *
from tud_test_base import *

@pytest.fixture
def get_hero() -> theHero():
    hero = theHero()
    return hero

@pytest.fixture
def get_current_day() -> ini_current_day():
    current_day = ini_current_day() 
    return current_day

@pytest.fixture
def get_w_map() -> world_map():
    w_map = world_map()
    return w_map

@pytest.fixture
def get_rat() -> theRat(): 
    rat = theRat()
    return rat

'''''
Sprint 1
'''''                                 
                     
def test_mainmenu_input_1():
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

def test_mainmenu_input_2():
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

def test_mainmenu_input_3():
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

def test_mainmenu_input_4():
    set_keyboard_input([4])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game", "2) Resume Game", "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainmenu_input_0():
    set_keyboard_input([0])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game", "2) Resume Game", "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"


def test_mainmenu_input_negative():
    set_keyboard_input([-1])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game", "2) Resume Game", "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"

def test_mainmenu_input_specialcharacter():
    set_keyboard_input(['@'])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game", "2) Resume Game", "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]
    #assert value == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"                    
                
def test_mainmenu_newgame(): 
    """ User Story 1.1: Create New Game
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Return Day & Hero 
    
    """
    
    current_day, hero, w_map = new_game()
    assert current_day == 1
    assert hero["name"] == "The Hero"
    assert hero["min_damage"] == 2
    assert hero["max_damage"] == 4
    assert hero["hp"] == 20
    assert hero["max_hp"] == 20
    assert hero["defence"] == 1
    assert hero["position"] == [0, 0]
                    
def test_mainmenu_resumegame(): 
    """User Story: 1.2: Resume the previous game
    
     Input
    -----------------
    2
    
    Output
    -----------------
    Enter Choice: 2
    The game has been resumed to the previous state.
    
    """
    errormessage, output, hero, w_map, current_day = resume_game()
    if(errormessage == ""):
        assert output == "The game has been resumed to the previous save state."
    else:
        assert output == "Existing file does not exist.\n"
        assert errormessage == FileNotFoundError

def test_mainmenu_exitgame(): 
    """User Story 1.3: Exit the game
    
     Input
    -----------------
    3
    
    Output
    -----------------
    Enter choice: 3
    The program will close since there are no unsaved changes. 
    
    """
    output = exit_game()
    assert output == "The program will close since there are no unsaved changes."
    
 
def test_mainmenu_exitgame_prompt_yes():
    """User Story 1.3.1: Warning Message
    
    Input
    -----------------
    Y
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    Enter Choice: [Y/N]
    Bye bye!
    
    """
    set_keyboard_input(["Y"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", 
                    "Enter choice: [Y/N]", 
                    "Bye bye!"]
    #choice = unsaved_changes() #create a function
    # if(choice == "Yes"):
    #     exit_game_prompt()
    #     output = get_display_output()
    #     assert output == "You have unsaved changes. Do you want to continue?"
    # else:
    #     exit_game()
    #     output = get_display_output()
    #     assert output == "Enter choice: 3\nThe program will close since there are no unsaved changes."

# def test_unsaved_changes(): 
#     """A function to see if there is unsaved changes. 

#     Input
#     -----------------
#     Yes 
    
#     Output
#     -----------------
#     You have unsaved changes. Do you want to continue?

#     """

#     set_keyboard_input("Yes")
#     unsaved_changes()
#     output = get_display_output()
#     assert output == "You have unsaved changes. Do you want to continue?"

def test_mainmenu_exitgame_prompt_no():
    """User Story 1.3.2: Warning Message
    
    Input
    -----------------
    N
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    Enter Choice: [Y/N]
    Going back to the game...

    """
    
    set_keyboard_input(["N"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?","Enter choice: [Y/N]", "Going back to the game..."]

# User Story 2

def test_townmenu_input_1():
    set_keyboard_input([1])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Viewing the Character's statistics..."]

def test_townmenu_input_2():
    set_keyboard_input([2])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Viewing the Town Map..."]

def test_townmenu_input_3():
    set_keyboard_input([3])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Moving the Hero..."]

def test_townmenu_input_4():
    set_keyboard_input([4])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Resting the Hero..."]

def test_townmenu_input_5():
    set_keyboard_input([5])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Saving the game..."]

def test_townmenu_input_6():
    set_keyboard_input([6])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Exiting game..."]

def test_townMenu_input_0():
    set_keyboard_input([0])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Please enter a valid choice."]
    
def test_townmenu_input_negative():
    set_keyboard_input([-3])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Please enter a valid choice."]

def test_townmenu_input_positive():
    set_keyboard_input([9])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Please enter a valid choice."]

def test_townmenu_input_specialcharacter():
    set_keyboard_input(['='])
    town_menu()
    output = get_display_output()
    assert output == ["1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Rest", 
                        "5) Save Game", 
                        "6) Exit Game", 
                        "Please enter a valid numerical choice."]


def test_townmenu():
    """User Story 2.0: Display town menu
    
    Input
    -----------------
    Start new game or in a town
    
    Output
    -----------------
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game
    
    """
    output = town_menu()
    assert output == "1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"     

       

def test_townmenu_viewcharacter(get_hero):
    """User Story 2.1: Display player's statistics 
    
    
    Output
    -----------------
    
    The hero
    Damage: 2-4
    Defence: 1
    HP: 20
    
    """
    #print_hero_stats() 
    set_keyboard_input([])
    print_hero_stats(get_hero)
    output =get_display_output()
    damage = "Damage: {}-{}".format(get_hero["min_damage"], get_hero["max_damage"])
    defence = "Defence: {}".format(get_hero["defence"])
    hp = "HP: {}".format(get_hero["hp"])
    assert output == [get_hero["name"], damage, defence, hp]

    
   

def test_townmenu_viewmap(get_hero, get_w_map):
    """User Story 2.2: Display the world map
    
    
    Output
    -----------------
        
        ['T', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
        [' ', ' ', ' ', 'T', ' ', ' ', ' ', ' '],\
        [' ', ' ', ' ', ' ', ' ', 'T', ' ', ' '],\
        [' ', 'T', ' ', ' ', ' ', ' ', ' ', ' '],\
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
        [' ', ' ', ' ', ' ', 'T', ' ', ' ', ' '],\
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']
    
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

def test_townmenu_move(): 
    """ Incomplete function."""

    print("Move.")

def test_townmenu_rest(get_hero):
    """User Story 2.4: Rest the character 
    
    
    Output
    -----------------
    
    You are fully healed. 
    
    """
    #set_keyboard_input("4") 
    hp, print_result = rest(get_hero) 
    #output = get_display_output()
    assert hp == get_hero["max_hp"]
    assert print_result == "You are fully healed."

def test_townmenu_savegame(get_hero, get_current_day, get_w_map):
    """User Story 2.5: Save the game
    
    
    Output
    -----------------
    Enter choice: 5
    Game saved. 
    
    """  
    output = save_game(get_hero, get_w_map, get_current_day)
    assert output == "Game saved."

def test_townmenu_exitgame(): 
    """User Story 2.6: Exit the game
    
    
    Output
    -----------------
    Enter choice: 6
    The program will close since there are no unsaved changes. 
    /closeRatVenture 
    
    """
    
    output = exit_game() 
    assert output == "The program will close since there are no unsaved changes."



# User Story 3

# def test_combatmenu(get_rat): 
#     set_keyboard_input([])
#     print_rat_stats(get_rat)
#     output = get_display_output()

#     # tile = get_hero_position(get_hero)
#     # location = ""
#     # if tile == "T":
#     #     location = "You are in a town."
#     # elif tile == " ":
#     #     location = "You are out in the open."
        
#     #day = "Day {}: {}".format(get_current_day, location)

#     encounter = "Encounter! - {}".format(get_rat["name"])
#     damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
#     defence = "Defence: {}".format(get_rat["defence"])
#     hp = "HP: {}".format(get_rat["hp"])
#     assert output == [encounter, damage, defence, hp]

def test_combatmenu(): 
    set_keyboard_input([])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run"]

def test_combatmenu_input_1():
    set_keyboard_input([1])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Attacking the Rat..."]

def test_combatmenu_input_2():
    set_keyboard_input([2])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Running and hiding..."]      

def test_combatmenu_input_2():
    set_keyboard_input([2])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Running and hiding..."]

def test_combatmenu_input_0():
    set_keyboard_input([0])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Please enter a valid choice."]

def test_combatmenu_input_negative():
    set_keyboard_input([-2])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Please enter a valid choice."]    

def test_combatmenu_input_positive():
    set_keyboard_input([9])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Please enter a valid choice."]  

def test_combatmenu_input_specialcharacter():
    set_keyboard_input(["="])
    fight_menu()
    output = get_display_output()
    assert output == ["1) Attack\n2) Run", 
                        "Please enter a valid numerical choice."]               

def test_combatmenu_view_ratstats(get_rat):
    set_keyboard_input([])
    print_rat_stats(get_rat)
    output = get_display_output()
    encounter = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter, damage, defence, hp]


def test_combatmenu_viewmap(get_hero, get_w_map):
    
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

# def test_combatmenu_attackRat(get_hero, get_rat, flag=True): 
#         set_keyboard_input([])
#         attack(get_hero, get_rat, flag=True)
#         output = get_display_output()

#         hero_damage = randint(get_hero["min_damage"], get_hero["max_damage"])
#         enemy_damage = randint(get_rat["min_damage"], get_rat["max_damage"])

#         hero_total_damage = hero_damage - get_rat["defence"]
#         rat_total_damage = enemy_damage - get_hero["defence"]
#         if rat_total_damage <= 0:
#            rat_total_damage = 0

#         offenseHero = "You deal {} damage to the {}".format(hero_total_damage, get_rat["name"])
#         offenseRat = "Ouch! The {} hit you for {} damage".format(get_rat["name"],rat_total_damage)
#         hp = "You have {} HP left.".format(get_hero["hp"])
#         assert output == [offenseHero, offenseRat, hp]

#         if hero["hp"] <= 0:
#             print("You ran out of HP! Game over.")
#                 if flag == True:
#                 sys.exit(0)

#         print("You have {} HP left.".format(hero["hp"]))
#         if rat["hp"] <= 0:
#             print("The {} is dead! You are victorious!".format(rat["name"]))

#         # need to reverse engineer, incomplete  

def test_combatmenu_Orb(): 
    """ User Story 3.1.1 """
    set_keyboard_input([])
    # the function for Orb power
    output = get_display_output()
    assert output == ["You have successfuly obtained the Orb power."]

def test_combatmenu_run(): 
    set_keyboard_input([])
    hero_run()
    output == get_display_output()
    assert output == ["Enter choice: ", 
                        "You run and hide.", 
                        "1) View Character", 
                        "2) View Map", 
                        "3) Move", 
                        "4) Exit Game",
                        "Enter Choice:"]









