# Unit tests for packaging_treasure.py
import copy
from packaging_treasure import outcome, update_dungeon, dungeon1, dungeon2, run_to_result, success_chance
##
#print(dungeon1)
def test_outcome():
    #print (dungeon1)
    assert outcome(dungeon1)==-1


def test_update_dungeon():
    initial_dungeon=copy.deepcopy(dungeon1)
    assert update_dungeon(dungeon1)!=initial_dungeon


def test_success_change_dungeon1_zero():
    assert success_chance(dungeon1)==0

def test_success_change_dungeon2_one():
    assert success_chance(dungeon2)!=1

def test_success_change_dungeon2_zero():
    assert success_chance(dungeon2)!=0
