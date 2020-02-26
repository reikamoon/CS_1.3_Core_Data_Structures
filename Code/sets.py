
class Set:
    def __init__(self, items):
        self.set = []
        self.size = 0
        for item in items:
            self.add(item)

    def contains(self, element):
        pass

    def add(self, item):
        if item not in self.set:
            self.set.append(item)
            self.size += 1

    def remove(self, element):
        pass

    def union(self, other_set):
        pass

    def intersection(self, other_set):
        pass

    def difference(self, other_set):
        pass

    def is_subset(self, other_set):
        pass


if __name__ == '__main__':
    items = [1,2,3,4,5,5,6,7,8,9]
    myset = Set(items)
    print(myset.set)
