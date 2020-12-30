import pytest 
from RatVenture_Function import * # update once developer starts 
from tud_test_base import *

@pytest.fixture
def get_hero() -> theHero():
    hero = theHero()
    return hero

'''''
Sprint 1
'''''

def test_main_menu(): 
    
    """User Story 1.0: Test whether main menu 
    pops out when program opens
    
    Input
    -----------------
    Open the RatVenture application.
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:
    
    """
    main_menu()
    output = get_display_output()
    assert output == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game\nEnter choice: "
                     
                
def test_new_game(): 
    """ User Story 1.1: Create New Game
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Return Day & Hero 
    
    """
    
    current_day, hero = new_game()
    assert current_day == 1
    assert hero["name"] == "The Hero"
    assert hero["min_damage"] == 2
    assert hero["max_damage"] == 4
    assert hero["hp"] == 20
    assert hero["max_hp"] == 20
    assert hero["defence"] == 1
    assert hero["position"] == [0, 0]
                    
def test_resume_game(): 
    """User Story: 1.2: Resume the previous game
    
     Input
    -----------------
    2
    
    Output
    -----------------
    Enter Choice: 2
    The game has been resumed to the previous state.
    
    """
    set_keyboard_input("2")
    
    resume_game()
    output = get_display_output()
    assert output == "Enter choice: 2\nThe game has been resumed to the previous state."
       
    
def test_exit_game(): 
    """User Story 1.3: Exit the game
    
     Input
    -----------------
    3
    
    Output
    -----------------
    Enter choice: 3
    The program will close since there are no unsaved changes. 
    /closeRatVenture 
    
    """
    set_keyboard_input("3")
    exit_game()
    output = get_display_output()
    assert output == "Enter choice: 3\nThe program will close since there are no unsaved changes."
    
 
def test_exit_game_prompt():
    """User Story 1.3.1: Warning Message
    
    Input
    -----------------
    3
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    
    """
    set_keyboard_input("3")
    exit_game_prompt()
    output = get_display_output()
    assert output == "You have unsaved changes. Do you want to continue?"
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

def test_town_menu():
    """User Story 2.0: Display town menu
    
    Input
    -----------------
    Start new game or in a town
    
    Output
    -----------------
    Day 1: You are in a town.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game
    Enter choice:
    
    """
    
    set_keyboard_input("1"/"2")
    menu()
    output = get_display_output()
    assert output == "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game\nEnter choice:"    

def test_view_character():
    """User Story 2.1: Display player's statistics 
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Enter choice: 1
    The hero
    Damage: 2-4
    Defence: 1
    HP: 20
    
    """
    print_hero_stats() 
    output = get_display_output()
    assert output == "Enter choice: 1\nThe hero\nDamage: 2-4\nDefence: 1\nHP: 20"


def test_view_map():
    """User Story 2.2: Display the world map
    
    Input
    -----------------
    2
    
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
    
def test_rest(get_hero):
    """User Story 2.4: Rest the character 
    
    Input
    -----------------
    4
    
    Output
    -----------------
    
    You are fully healed. 
    
    """
    #set_keyboard_input("4") 
    hp = rest(get_hero) 
    #output = get_display_output()
    assert hp == get_hero["max_hp"]

def test_save_game():
    """User Story 2.5: Save the game
    
    Input
    -----------------
    5
    
    Output
    -----------------
    Enter choice: 5
    Game saved. 
    
    """
    set_keyboard_input("5")  
    save_game() 
    output = get_display_output()
    assert output == "Enter choice: 5\nGame saved."

def test_exit_game(): 
    """User Story 2.6: Exit the game
    
    Input
    -----------------
    6
    
    Output
    -----------------
    Enter choice: 6
    The program will close since there are no unsaved changes. 
    /closeRatVenture 
    
    """
    set_keyboard_input("6") 
    exit_game() 
    output = get_display_output()
    assert output == "Enter choice: 6\nThe program will close since there are no unsaved changes."

# need to know how to link one function to another and then have the yes or no input
# for workflow testing
# for testing purposes

#just to push
    



