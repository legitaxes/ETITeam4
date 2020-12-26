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
    assert value == "Welcome to Ratventure!\n"
                     "----------------------"
                     "1) New Game /n"
                     "2) Resume Game /n"
                     "3) Exit Game /n"
                     "Enter choice: "
                
                     
    
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
    assert value = "Enter choice: 1 /n"
                   "Day 1: You are in a town. /n" 
                   "1) View Character /n"
                   "2) View Map /n"
                   "3) Move /n"
                   "4) Rest /n"
                   "5) Save Game /n"
                   "6) Exit Game /n"
                   "Enter choice: /n"
                    
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
    assert value = "Enter choice: 2 /n" 
                   "The game has been resumed to the previous state."
       
    
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
    assert value = "Enter choice: 3" 
                  "The program will close since there are no unsaved changes." 
    assert value = close(RatVenture) 
 

def test_exit_game_prompt():
    """User Story 1.3.1: Warning Message
    
    Input
    -----------------
    3
    
    Output
    -----------------
    You have unsaved changes. Continue or Cancel? 
    
    """
    
    value = open (exit_game)
    assert value = "You have unsaved changes. Continue or Cancel?" 
    



