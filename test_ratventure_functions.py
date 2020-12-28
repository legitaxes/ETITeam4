import pytest 
from RatVenture_Function import * # update once developer starts 
from tud_test_base import set_keyboard_input, get_display_output

'''''
Sprint 1
'''''

def test_main_menu(): 
    
    """User Story 1.0: Test whether main menu 
    pops out when program opens
    
    Input
    -----------------
    None
    
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
    Enter choice: 1
    Day 1: You are in a town.
    1) View Character
    2) View Map
    3) Move
    4) Rest
    5) Save Game
    6) Exit Game
    Enter choice:
    
    """
    set_keyboard_input("1")
    
    new_game()
    output = get_display_output()
    assert output == ["Enter choice: 1\n Day 1: You are in a town.\n 1) View Character\n 2) View Map\n 3) Move\n 4) Rest\n 5) Save Game\n 6) Exit Game\n Enter choice:"]
                    
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
    
    value = resume_game()
    assert value == "Enter choice: 2 \n The game has been resumed to the previous state."
       
    
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
    value = exit_game()
    assert value == "Enter choice: 3 \n The program will close since there are no unsaved changes." 
    assert value == exit 
 
def test_exit_game_prompt():
    """User Story 1.3.1: Warning Message
    
    Input
    -----------------
    3
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    
    """
    
    value = exit_game()
    assert value == "You have unsaved changes. Do you want to continue?" 

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
    
    value = open(town_menu)
    assert value == "Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:"
                    
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
    value = open (view_map)
    assert value == "Enter choice: 1 \n The hero \n Damage: 2-4 \n Defence: 1 \n HP: 20" 
    
def test_view_map():
    """User Story 2.2: Display the world map
    
    Input
    -----------------
    2
    
    Output
    -----------------
    Enter choice: 2
    /displayWorldMap 
    
    """
    value = open (view_map)
    assert value == "Enter choice: 2"
    assert value == worldMap
    
def test_rest():
    """User Story 2.4: Rest the character 
    
    Input
    -----------------
    4
    
    Output
    -----------------
    Enter choice: 4
    You are fully healed. 
    
    """
    value = open (rest)
    assert value == "Enter choice: 4 \n You are fully healed." 
    
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
    value = open (save_game)
    assert value == "Enter choice: 5 \n Game saved." 
    
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
    value = open (exit_game)
    assert value == "Enter choice: 6 \n The program will close since there are no unsaved changes." 
    assert value == exit 
    
def test_exit_game_prompt():
    """User Story 2.6.1: Warning Message
    
    Input
    -----------------
    6
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue? 
    
    """
    
    value = open (exit_game)
    assert value == "You have unsaved changes. Do you want to continue?" 
    
# need to know how to link one function to another and then have the yes or no input
# for workflow testing
# for testing purposes
    



