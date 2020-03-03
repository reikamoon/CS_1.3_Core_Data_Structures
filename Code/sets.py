from binarytree import BinarySearchTree
class Set:
    def __init__(self, items):
        self.set = BinarySearchTree()
        self.size = 0
        for item in items:
            self.add(item)

    def contains(self, item):
        '''Check what items are in the set'''
        return self.set.contains(item)

        # Time complexity: O(n)

    def add(self, item):
        '''Add an item to a set'''
        if self.set.contains(item) != True:
            self.set.insert(item)
            self.size += 1

        # Time Complexity: O(n)

    def remove(self, item):
        '''Remove item from a set'''
        return self.set.delete(item)

        # Time Complexity: O(n)

    def union(self, other_set):
        '''Merges sets together, but removes duplicates'''
        unionset = Set(self.set.items_in_order() + other_set.set.items_in_order())
        return unionset

        # Time Complexity: O(n)

    def intersection(self, other_set):
        '''Finds the most common elements in both sets'''
        # if item is present in self.set and other_set:
        #     return item
        intersectionitems = []
        for item in self.set.items_in_order():
            if other_set.contains(item) == True:
                intersectionitems.append(item)
        intersectionset = Set(intersectionitems)
        return intersectionset
            #check if item is in otherset using contains
            #if it is add to intersectionitems
        #create a new set out of intersectionitems and return it

    def difference(self, other_set):
        '''Checks what items are present in one set that are not present in the other'''
        differenceitems = []
        for item in self.set.items_in_order():
            if other_set.contains(item) == False:
                differenceitems.append(item)
        differenceset = Set(differenceitems)
        return differenceset

        # Time Complexity: O(n)

    def is_subset(self, other_set):
        '''Checks if a set is a subset of another set'''
        for item in self.set.items_in_order():
            if other_set.contains(item) == False:
                return False
        return True

        # Time Complexity: O(n)




if __name__ == '__main__':
    items = [1,2,3,4,5,5,6,7,8,9,19]
    items2 = [10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19]
    sub = [1,2,3,4,5]
    myset1 = Set(items)
    myset2 = Set(items2)
    subset1 = Set(sub)
    result = subset1.is_subset(myset1)
    print(result)

    # print('items in-order:    {}'.format(myset1.set.items_in_order()))
    # print(myset1.contains(3))
    # print(myset1.contains(10))
    # print(myset1.remove(7))
    # print('items in-order:    {}'.format(myset1.set.items_in_order()))
    # unionset = myset1.union(myset2)
    # print('items in-order:    {}'.format(unionset.set.items_in_order()))
    # intersectionset = myset1.intersection(myset2)
    # print('items in-order:    {}'.format(intersectionset.set.items_in_order()))
    # differenceset = myset1.difference(myset2)
    # print('items in-order:    {}'.format(differenceset.set.items_in_order()))
    subset1.is_subset(myset1)
