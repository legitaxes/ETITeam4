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
    print("Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game\nEnter choice: ")
    
    #choice = int(input("Enter Choice: "))
    return "Welcome to Ratventure\n1) New Game\n2) Resume Game\n3) Exit Game\nEnter choice: "

def town_menu():
    print("\n Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:")
    return "\n Day 1: You are in a town. \n 1) View Character \n 2) View Map \n 3) Move \n 4) Rest \n 5) Save Game \n 6) Exit Game \n Enter choice:"

def new_game(choice):
    # TODO figure out the structure of the program and how it should be ran
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
    choice = 1

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

