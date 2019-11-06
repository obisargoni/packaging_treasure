# Unit tests for packaging_treasure.py
import random
from unittest.mock import patch
from .packaging_treasure import random_move, outcome, update_dungeon, dungeon1

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