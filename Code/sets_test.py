from sets import *

def test_contains():
    set1 = ['Dog', 'Cat', 'Bird']
    myset = Set(set1)
    assert myset.contains('Dog') == True

def test_add():
    set1 = ['Dog', 'Cat', 'Bird']
    myset = Set(set1)
    myset.add('Chicken')
    newset = ['Dog','Cat','Bird','Chicken']
    newset1 = Set(newset)
    assert myset == newset1

def test_remove():
    set1 = ['Dimitri', 'Byleth', 'Edelgard', 'Claude']
    myset = Set(set1)
    set2 = ['Dimitri', 'Edelgard', 'Claude']
    myset2 = Set(set2)
    myset.remove('Byleth')
    assert myset == myset2

def test_union():
    set1 = ['Nohime', 'Oichi no Kata', 'Koshosho', 'Nene', 'Komatsuhime']
    myset1 = Set(set1)
    set2 = ['Nobunaga Oda', 'Nagamasa Azai', 'Motochika Chosokabe', 'Hideyoshi Toyotomi', 'Nobuyuki Sanada']
    myset2 = Set(set2)
    set3 = ['Nohime', 'Oichi no Kata', 'Koshosho', 'Nene', 'Komatsuhime', 'Nobunaga Oda', 'Nagamasa Azai', 'Motochika Chosokabe', 'Hideyoshi Toyotomi', 'Nobuyuki Sanada']
    myset3 = Set(set3)
    unionset = myset1.union(myset2)
    assert unionset == myset3

def test_intersection():
    set1 = ['Nohime', 'Oichi no Kata', 'Koshosho', 'Gracia', 'Nene', 'Komatsuhime', 'Ginchiyo Tachibana', 'Hayakawa-dono', 'Aya gozen', 'Naotora Ii', 'Kunoichi']
    myset1 = Set(set1)
    set2 = ['Nohime', 'Oichi no Kata', 'Koshosho', 'Gracia', 'Nene', 'Komatsuhime', 'Ginchiyo Tachibana', 'Hayakawa-dono', 'Aya gozen', 'Naotora Ii', 'Kunoichi', 'Nobuyuki Sanada']
    myset2 = Set(set2)
    intersectionset = myset1.intersection(myset2)
    assert intersectionset == myset1
