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
    output = town_menu()
    assert output == "Day 1: You are in a town.\n1) View Character\n2) View Map\n3) Move\n4) Rest\n5) Save Game\n6) Exit Game"    

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
    Enter choice: 2
    /displayWorldMap 
    
    """
    value = open (view_map)
    assert value == "Enter choice: 2"
    #assert value == worldMap
    
def test_rest(get_hero):
    """User Story 2.4: Rest the character 
    
    Input
    -----------------
    4
    
    Output
    -----------------
    Enter choice: 4
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
    



