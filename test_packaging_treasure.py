# Unit tests for packaging_treasure.py
import random
from unittest.mock import patch, Mock
from .packaging_treasure import random_move, outcome, update_dungeon, dungeon1,run_to_result

def test_random_move():
    """Test the random move function    

    def random_move(network, current_loc):
    targets=network[current_loc]
    return random.choice(targets)
    """
    # Use mock random number generator
    with patch.object(random, "choice") as mock_choice:
        network = [[1],
                   [0,2],
                   [1]]
        current_loc = 0
        next_loc = random_move(network, current_loc)
        mock_choice.assert_called_with(network[current_loc])
        

##
#print(dungeon1)
def test_outcome():
    #print (dungeon1)
    assert outcome(dungeon1)==-1

def test_run_to_result():
    """Test that for a know outcome the function proceeds as expected
    """
    
    with patch('packaging_treasure.packaging_treasure.outcome') as mock_outcome:
        mock_outcome.return_value = 0
        assert run_to_result(dungeon1) == 0
    
    