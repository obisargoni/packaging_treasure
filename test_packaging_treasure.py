# Unit tests for packaging_treasure.py

from packaging_treasure import outcome, update_dungeon, dungeon1
##
#print(dungeon1)
def test_outcome():
    #print (dungeon1)
    assert outcome(dungeon1)==-1
