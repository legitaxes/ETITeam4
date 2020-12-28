import pytest 
from RatVenture_Function import * # update once developer starts 

def test_hero():
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
    value = hero()
    assert value['name'] == "The Hero"
    assert value['min_damage'] == 2
    assert value['max_damage'] == 4
    assert value['hp'] == 20
    assert value['max_hp'] == 20
    assert value['defence'] == 1
    assert value['position'] == [0, 0]

def test_rat():
    """
    This test function initializes rat's stats
        OUTPUT:"name": "Rat",
                "min_damage": 1,
                "max_damage": 3,
                "hp": 10,
                "defence": 1
            In a DICTIONARY
    """
    value = rat()
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
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],\
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'K']]
    assert len(value) == len(expected)
    assert all([a == b for a, b in zip(value, expected)]) #this checks python list against the expected value


def test_print_map():
    """
    Test function of print_map Function:
        Displays the Map of the game when called
        This function should print the full layout of the map
    """
    # TODO: Create a test case that prints the map of the game 
    # Test case should assert the following:
    #  > The map 
    #  > Formatting of the "borders" 
    #  > Displaying the "legends"
    # labels: tasks, unit-test
    # assignees: legitaxes


def test_print_day():
    """
    Test function of print_day Function:
        Display the tile the hero is at and display whether the hero is in town or out in open
    """
    # TODO: Create a test case that prints the day of the game
    # Test case should  assert the following values:
    #  > Location of the hero 
    #  > Displaying the day
    # labels: tasks, unit-test
    # assignees: laukwangwei


def test_print_hero_stats():
    """
    Test function of print_hero_stats Function:
        Display the hero's stats and his details
        This function should return the hero's Name, Damage, Defence and HP 
    """
    # TODO: Create a test case that prints the stats of the hero
    # Test case should assert the following values:
    #  > All of the hero's stats
    # labels: tasks, unit-test
    # assignees: laukwangwei

def test_get_hero_position():
    """
    Test function of get_hero_position Function:
        This function mainly serves as a way for the program to get the position of the hero
        It should return the tile where the hero is on the map
    """
    # TODO: Create a test case that gets the hero's position
    # Test case should assert the following values:
    #   > The position of the hero
    # labels: tasks, unit-test
    # assignees: legitaxes
    
