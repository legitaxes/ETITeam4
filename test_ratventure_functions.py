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
def test_main(): 
    """User Story 1.0: Test the inputs for Main Menu

    Input
    -----------------
    4
    
    Output
    -----------------
    Please input an appropriate option. 
    Welcome to Ratventure!
    1) New Game
    2) Resume Game
    3) Exit Game

    """
    output = main_menu()
    assert output == "Error! Please input an appropriate option.\nWelcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"
    
def test_main_menu(): 
    
    """User Story 1.0: Test whether main menu 
    pops out when program opens
    
    Input
    -----------------
    Open the RatVenture application.
    
    Output
    -----------------
    Welcome to Ratventure!
    1) New Game
    2) Resume Game
    3) Exit Game
    
    """
    output = main_menu()
    assert output == "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game"
                    
                
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
    output = resume_game()
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
    
    """
    output = exit_game()
    assert output == "Enter choice: 3\nThe program will close since there are no unsaved changes."
    
 
def test_exit_game_prompt():
    """User Story 1.3.1: Warning Message
    
    Input
    -----------------
    3
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    Enter Choice: (Yes)
    Bye bye!
    -----------------
    You have unsaved changes. Do you want to continue? 
    Enter Choice: (No)
    Welcome to Ratventure!
    1) New Game
    2) Resume Game
    3) Exit Game
    """
    set_keyboard_input("Yes")
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", "Enter choice: ", "Bye bye!"]

    set_keyboard_input("No")
    exit_game_prompt()
    output = get_display_output()
    assert output == "You have unsaved changes. Do you want to continue?","Enter choice:",""
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
def test_main():
    """User Story 2.0: Test input for town menu
    
    Input
    -----------------
    7
    
    Output
    -----------------

    Error! Please input an appropiate option.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game
    
    
    """
    output = town_menu()
    assert output == "Error! Please input an appropiate option.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"    

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
    
    
    """
    output = town_menu()
    assert output == "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"    

def test_view_character():
    """User Story 2.1: Display player's statistics 
    
    
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
    assert output == "The hero\nDamage: 2-4\nDefence: 1\nHP: 20"


def test_view_map():
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
    
    
    Output
    -----------------
    Enter choice: 5
    Game saved. 
    
    """  
    output = save_game()
    assert output == "Game saved."

def test_exit_game(): 
    """User Story 2.6: Exit the game
    
    
    Output
    -----------------
    Enter choice: 6
    The program will close since there are no unsaved changes. 
    /closeRatVenture 
    
    """
    
    output = exit_game() 
    assert output == "The program will close since there are no unsaved changes."

# need to know how to link one function to another and then have the yes or no input
# for workflow testing
# for testing purposes

#just to push
    



