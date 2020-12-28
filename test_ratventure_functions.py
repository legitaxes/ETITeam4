import pytest 
# from RatVenture_Function import * # update once developer starts 

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
    value = open(main_menu)
    assert value == "Welcome to Ratventure \n 1) New Game \n 2) Resume Game \n 3) Exit Game \n Enter choice: "
                     
                
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
    
    value = open(new_game)
    assert value == "Enter choice: 1 \n Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:"
                    
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
    
    value = open(resume_game)
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
    value = open (exit_game)
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
    
    value = open (exit_game)
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
    set_keyboard_input("1") 
    view_character() 
    output = get_display_output()
    assert output == "Enter choice: 1\nThe hero\nDamage: 2-4\nDefence: 1\nHP: 20"


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
    #assert value == worldMap
    
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
    set_keyboard_input("4") 
    rest() 
    output = get_display_output()
    assert output == "Enter choice: 4\nYou are fully healed."

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
    



