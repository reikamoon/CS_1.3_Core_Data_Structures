from sets import *

def test_contains():
    set1 = ['Dog', 'Cat', 'Bird']
    myset = Set(set1)
    assert myset.contains('Dog') == True

def test_add():
    set1 = ['Dog', 'Cat', 'Bird']
    myset = Set(set1)
    myset.add('Chicken')
    assert myset == ['Dog','Cat','Bird','Chicken']
