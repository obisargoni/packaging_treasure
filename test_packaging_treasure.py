# Unit tests for packaging_treasure.py
import copy
from packaging_treasure import outcome, update_dungeon, dungeon1
##
#print(dungeon1)
def test_outcome():
    #print (dungeon1)
    assert outcome(dungeon1)==-1


def test_update_dungeon():
    initial_dungeon=copy.deepcopy(dungeon1)
    assert update_dungeon(dungeon1)!=initial_dungeon





#def update_dungeon(dungeon):
#    dungeon['adventurer']=random_move(dungeon['network'], dungeon['adventurer'])
#    dungeon['troll']=random_move(dungeon['network'], dungeon['troll'])
