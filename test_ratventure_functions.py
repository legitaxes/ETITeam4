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

@pytest.fixture
def get_orb() -> generate_orb(): 
    orb = generate_orb()
    return orb

@pytest.fixture
def get_RatKing() -> theRatKing(): 
    RatKing = theRatKing()
    return RatKing

### This code onwards are testing the ones with inputs

def test_mainmenu_zero(): 
    """To test whether an incorrect input in the Main Menu will
    return an error message.
    
    Input
    -----------------
    0
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Please enter a valid choice

    """
    set_keyboard_input([0])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]

def test_mainmenu_negative(): 
    """To test whether an incorrect negative input in the Main Menu will
    return an error message.
    
    Input
    -----------------
    -2
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Please enter a valid choice

    """
    set_keyboard_input([-2])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]

def test_mainmenu_positive(): 
    """To test whether an incorrect positive input in the Main Menu will
    return an error message.
    
    Input
    -----------------
    5
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Please enter a valid choice

    """
    set_keyboard_input([5])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Please enter a valid choice"]

def test_mainmenu_specialcharacter(): 
    """To test whether an incorrect not numerical input in the Main Menu will
    return an error message.
    
    Input
    -----------------
    @
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Please enter a valid option!

    """
    set_keyboard_input(["="])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Please enter a valid option!"]

def test_mainmenu_newgame(): 
    """To test whether the option New Game will be triggered from the Main Menu.
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Starting a new game...

    """
    set_keyboard_input([1])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Starting a new game..."]

def test_mainmenu_resumegame(): 
    """To test whether the option Resume Game will be triggered from the Main Menu.
    
    Input
    -----------------
    2
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Resuming from last save state...

    """
    set_keyboard_input([2])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Resuming from last save state..."]

def test_mainmenu_exitgame(): 
    """To test whether the option Resume Game will be triggered from the Main Menu.
    
    Input
    -----------------
    3
    
    Output
    -----------------
    Welcome to Ratventure!
    ----------------------
    1) New Game
    2) Resume Game
    3) Exit Game
    Enter choice:

    Exiting game...

    """
    set_keyboard_input([3])
    main_menu()
    output = get_display_output()
    assert output == ["Welcome to Ratventure", "----------------------", "1) New Game","2) Resume Game",
                        "3) Exit Game", "Enter Choice: ", "Exiting game..."]

def test_mainmenu_exitgame_Yesprompt(): 
    """To test whether the Exit Game prompted with a Yes will close the program.
    
    Input
    -----------------
    Y
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue?
    Enter choice: [Y/N]
    Bye bye!

    """
    set_keyboard_input(["Y"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", 
                        "Enter choice: [Y/N]","Bye bye!"]

def test_mainmenu_exitgame_Noprompt(): 
    """To test whether the Exit Game prompted with a No will lead the 
    user back to the game to save the changes. 
    
    Input
    -----------------
    N
    
    Output
    -----------------
    You have unsaved changes. Do you want to continue?
    Enter choice: [Y/N]
    Going back to the game...
    
    """
    set_keyboard_input(["N"])
    exit_game_prompt()
    output = get_display_output()
    assert output == ["You have unsaved changes. Do you want to continue?", 
                        "Enter choice: [Y/N]","Going back to the game..."]

# have failing test cases for small and big letters
def test_townmenu_move_w(get_hero, get_w_map, get_orb): 
    """To test whether user can move up in the town.
    
    Input
    -----------------
    w
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    Not able to move out of map (Up/Down)!
    
    """
    set_keyboard_input(["w"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: ",
                        "Not able to move out of map (Up/Down)!"]

def test_townmenu_move_bigletter(get_hero, get_w_map, get_orb): 
    """To test whether user can move up in the town.
    
    Input
    -----------------
    W (upper case)
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    Not able to move out of map (Up/Down)!
    
    """
    set_keyboard_input(["W"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: ",
                        "Not able to move out of map (Up/Down)!"]

def test_townmenu_move_a(get_hero, get_w_map, get_orb): 
    """To test whether user can move left in the town.
    
    Input
    -----------------
    a
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    Not able to move out of map (Left/Right)!
    
    """
    set_keyboard_input(["a"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: ", "Not able to move out of map (Left/Right)!"]

def test_townmenu_move_d(get_hero, get_w_map, get_orb): 
    """To test whether user can move right in the town.
    
    Input
    -----------------
    d
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    
    """
    set_keyboard_input(["d"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: "]

def test_townmenu_move_s(get_hero, get_w_map, get_orb): 
    """To test whether user can move down in the town.
    
    Input
    -----------------
    s
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    
    """
    set_keyboard_input(["s"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: "]

def test_townmenu_move_otherletter(get_hero, get_w_map, get_orb): 
    """To test whether an incorrect input will produce an error message.
    
    Input
    -----------------
    z
    
    Output
    -----------------
    W = up; A = left; S = down; D = right
    Your move:
    Input out of range
    """
    set_keyboard_input(["z"])
    move_hero(get_hero, get_w_map, get_orb, False)
    output = get_display_output()
    assert output == ["W = up; A = left; S = down; D = right", "Your move: ", "Input out of range"]

def test_encounter_attack(get_hero, get_rat):
    """To test whether the hero can attack the Rat.
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You deal {} damage to the Rat. 
    Ouch! The Rat hit you for {} damage.
    You have {} HP left. 
    Encounter! - Rat
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run
    """
    set_keyboard_input([1])
    origin_hp = get_hero["hp"]
    origin_hp_rat = get_rat["hp"]
    #attack(get_hero, get_rat, False)
    encounter(get_hero, get_rat, False)
    output = get_display_output()

    hero_total_damage = origin_hp_rat - get_rat["hp"]
    rat_total_damage = origin_hp - get_hero["hp"]

    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hporiginal = "HP: 10"
    hp = "HP: {}".format(get_rat["hp"])
    hp1 = "You have {} HP left.".format(get_hero["hp"])
    deal = "You deal {} damage to the {}".format(hero_total_damage, get_rat["name"])
    ouch = "Ouch! The {} hit you for {} damage".format(get_rat["name"],rat_total_damage)

    assert output == [encounter1, damage, defence, hporiginal, "1) Attack\n2) Run", "Enter choice: ", 
                        deal, ouch, hp1, encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_encounter_3(get_hero, get_rat):
    """To test whether combat menu will return an error message
    when an incorrect input is inputted.
    
    Input
    -----------------
    3
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    Please enter a valid choice: 
    """
    set_keyboard_input([3])
    #attack(get_hero, get_rat, False)
    encounter(get_hero, get_rat, False)
    output = get_display_output()

    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hporiginal = "HP: 10"

    assert output == [encounter1, damage, defence, hporiginal, "1) Attack\n2) Run", "Enter choice: ", "Please enter a valid option!"]


def test_encounter_run_1(get_hero, get_rat):
    """To test whether the hero can run and hide from the Rat.
    
    Input
    -----------------
    2, 1
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.

    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Encounter! - Rat
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run
    """
    set_keyboard_input([2, 1])
    encounter(get_hero, get_rat, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_encounter_run_2(get_hero, get_rat):
    """To test whether the hero can run and hide from the Rat.
    
    Input
    -----------------
    2, 2
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.

    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Encounter! - Rat
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run
    """
    set_keyboard_input([2, 2])
    encounter(get_hero, get_rat, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_encounter_run_3(get_hero, get_rat):
    """To test whether the hero can run and hide from the Rat and
    move from the Map again.
    
    Input
    -----------------
    2, 3
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.

    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    W = up; A = left; S = down; D = right
    """
    set_keyboard_input([2, 3])
    encounter(get_hero, get_rat, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        "W = up; A = left; S = down; D = right"]

def test_encounter_run_4(get_hero, get_rat):
    """To test whether the hero can run and hide from the Rat.
    
    Input
    -----------------
    2, 4
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.

    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Encounter! - Rat
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run
    """
    set_keyboard_input([2, 4])
    encounter(get_hero, get_rat, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: "]
                        #encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_encounter_run_5(get_hero, get_rat):
    """To test whether the hero can run and hide from the Rat.
    Failing Test Case.
    
    Input
    -----------------
    2, 5
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.

    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Please enter a valid choice

    """
    set_keyboard_input([2, 5])
    encounter(get_hero, get_rat, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_rat["name"])
    damage = "Damage: {}-{}".format(get_rat["min_damage"], get_rat["max_damage"])
    defence = "Defence: {}".format(get_rat["defence"])
    hp = "HP: {}".format(get_rat["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: "]

def test_ratking_encounter_attack_no(get_hero, get_RatKing): 
    """To test whether the ratking can attack the hero and whether 
    hero has the Orb.
    Failing Test Case. 
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 25 

    1) Attack 
    2) Run
    Enter Choice: 

    You do not have the Orb of Power - the Rat King is immune!

    You deal {} damage to the RatKing. 
    Ouch! The RatKing hit you for {} damage.
    You have {} HP left. 

    Encounter! - RatKing
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run

    """
    ## without orb
    set_keyboard_input([1])
    origin_hp = get_hero["hp"]
    origin_hp_ratking = get_RatKing["hp"]
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()

    hero_total_damage = origin_hp_ratking - get_RatKing["hp"]
    ratking_total_damage = origin_hp - get_hero["hp"]

    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hporiginal = "HP: 25"
    hp = "HP: {}".format(get_RatKing["hp"])
    hp1 = "You have {} HP left".format(get_hero["hp"])
    deal = "You deal {} damage to the {}".format(hero_total_damage, get_RatKing["name"])
    ouch = "Ouch! The {} hit you for {} damage".format(get_RatKing["name"],ratking_total_damage)
    nopower = "You do not have the Orb of Power - the Rat King is immune!"

    assert output == [encounter1, damage, defence, hporiginal, "1) Attack\n2) Run", "Enter choice: ", nopower,
                        deal, ouch, hp1, encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_ratking_encounter_attack_yes(get_hero, get_RatKing):
    """To test whether the ratking can attack the hero and whether 
    hero has the Orb. 
    
    Input
    -----------------
    1
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 25 

    1) Attack 
    2) Run
    Enter Choice: 

    You deal {} damage to the RatKing. 
    Ouch! The RatKing hit you for {} damage.
    You have {} HP left. 
    
    Encounter! - RatKing
    Damage: 1-3
    Defence: 1
    HP: {}

    1) Attack
    2) Run

    """
    ## with orb
    set_keyboard_input([1])
    origin_hp = get_hero["hp"]
    origin_hp_ratking = get_RatKing["hp"]
    get_hero["orb"] = True
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()

    hero_total_damage = origin_hp_ratking - get_RatKing["hp"]
    ratking_total_damage = origin_hp - get_hero["hp"]

    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hporiginal = "HP: 25"
    hp = "HP: {}".format(get_RatKing["hp"])
    hp1 = "You have {} HP left".format(get_hero["hp"])
    deal = "You deal {} damage to the {}".format(hero_total_damage, get_RatKing["name"])
    ouch = "Ouch! The {} hit you for {} damage".format(get_RatKing["name"],ratking_total_damage)

    assert output == [encounter1, damage, defence, hporiginal, "1) Attack\n2) Run", "Enter choice: ",
                        deal, ouch, hp1, encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_ratking_encounter_3(get_hero, get_RatKing): 
    """To test whether combat menu will return an error message
    when an incorrect input is inputted.
    Failing Test Case.
    
    Input
    -----------------
    3
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 10 
    1) Attack 
    2) Run
    Enter Choice: 
    Please enter a valid option! 
    """
    set_keyboard_input([3])
    #attack(get_hero, get_rat, False)
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()

    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hporiginal = "HP: 25"
    

    assert output == [encounter1, damage, defence, hporiginal, "1) Attack\n2) Run", "Enter choice: ", "Please enter a valid option!"]


def test_ratking_encounter_run_1(get_hero, get_RatKing):
    """To test whether the hero can run and hide from the RatKing.
    Also, choosing to view Character. 
    This is for RatKing. 
    
    Input
    -----------------
    2, 1
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Encounter! - RatKing
    Damage: 1-3
    Defence: 1
    HP: {}
    1) Attack
    2) Run

    """
    set_keyboard_input([2, 1])
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hp = "HP: {}".format(get_RatKing["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_ratking_encounter_run_2(get_hero, get_RatKing):
    """To test whether the hero can run and hide from the RatKing. Also, 
    choosing View Map in outdoor menu.
    This is for RatKing. 
    
    Input
    -----------------
    2, 2
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Encounter! - RatKing
    Damage: 1-3
    Defence: 1
    HP: {}
    1) Attack
    2) Run
    
    """
    set_keyboard_input([2, 2])
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hp = "HP: {}".format(get_RatKing["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        encounter1, damage, defence, hp, "1) Attack\n2) Run"]

def test_ratking_encounter_run_3(get_hero, get_RatKing):
    """To test whether the hero can run and hide from the RatKing. Also, 
    choosing Move in outdoor menu.
    This is for RatKing. 
    
    Input
    -----------------
    2, 3
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    W = up; A = left; S = down; D = right
    """
    set_keyboard_input([2, 3])
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hp = "HP: {}".format(get_RatKing["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        "W = up; A = left; S = down; D = right"]

def test_ratking_encounter_run_4(get_hero,get_RatKing):
    """To test whether the hero can run and hide from the Rat.
    Also choosing to exit the game.
    
    Input
    -----------------
    2, 4
    
    Output
    -----------------
    Encounter! - RatKing 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:

    Exiting from the game...
    """
    set_keyboard_input([2, 4])
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hp = "HP: {}".format(get_RatKing["hp"])
    #assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        #"You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        #encounter1, damage, defence, hp, "1) Attack\n2) Run"]
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: "]

def test_ratking_encounter_run_5(get_hero, get_RatKing):
    """To test whether the hero can run and hide from the Rat. Inputting a wrong
    value for the outdoor menu.
    Failing Test Case.
    Input
    -----------------
    2, 5
    
    Output
    -----------------
    Encounter! - Rat 
    Damage: 1-3
    Defence: 1
    HP: 10 

    1) Attack 
    2) Run
    Enter Choice: 

    You run and hide.
    1) View Character
    2) View Map
    3) Move
    4) Exit Game
    Enter choice:
    
    Please enter a valid option!
    """
    set_keyboard_input([2, 5])
    ratking_encounter(get_hero, get_RatKing, False)
    output = get_display_output()
    encounter1 = "Encounter! - {}".format(get_RatKing["name"])
    damage = "Damage: {}-{}".format(get_RatKing["min_damage"], get_RatKing["max_damage"])
    defence = "Defence: {}".format(get_RatKing["defence"])
    hp = "HP: {}".format(get_RatKing["hp"])
    assert output == [encounter1, damage, defence, hp, "1) Attack\n2) Run", "Enter choice: ", 
                        "You run and hide.", "1) View Character\n2) View Map\n3) Move\n4) Exit Game", "Enter choice: ",
                        "Please enter a valid option!"]








