from hashtable import *

#Dictionary Version
class DictionaryWordJumble:
    def __init__(self, jumbledwords):
        self.jumbledwords = jumbledwords
        self.word_map = self.build_word_hash("/usr/share/dict/words")

    def build_word_hash(self, filename):
        word_map = {}
        word_file = open(filename, "r")
        lines = [word.rstrip().lower() for word in word_file.readlines()]

        for word in lines:
            key = "".join(sorted(word))
            value = word
            word_map[key] = value

        return word_map

    def unscramble(self):
        solutions = {}
        for scrambled in self.jumbledwords:
            sorted_word = "".join(sorted(scrambled))
            solutions[scrambled] = self.word_map.get(sorted_word)
            print("The solution for " + scrambled + " is " + self.word_map[sorted_word])

        return solutions

# Hashtable version
class HashTableWordJumble:
    def __init__(self, jumbledwords):
        self.jumbledwords = jumbledwords
        self.word_map = self.build_word_hash("/usr/share/dict/words")

    def build_word_hash(self, filename):
        word_map = HashTable()
        word_file = open(filename, "r")
        lines = [word.rstrip().lower() for word in word_file.readlines()]

        for word in lines:
            key = "".join(sorted(word))
            value = word
            word_map.set(key, value)

        return word_map

    def unscramble(self):
        solutions = {}
        for scrambled in self.jumbledwords:
            sorted_word = "".join(sorted(scrambled))
            solutions[scrambled] = self.word_map.get(sorted_word)
            print("The solution for " + scrambled + " is " + self.word_map.get(sorted_word))

        return solutions


def test_dictionary_unscramble():
    wj = DictionaryWordJumble(['tac', 'sokik', 'dirb'])
    solutions = wj.unscramble()
    assert solutions == {'tac':'cat', 'sokik':'kiosk', 'dirb':'drib'}

def test_hashtable_unscramble():
    wj = HashTableWordJumble(['tac', 'sokik', 'dirb'])
    solutions = wj.unscramble()
    assert solutions == {'tac':'cat', 'sokik':'kiosk', 'dirb':'drib'}


if __name__ == '__main__':
    wj = DictionaryWordJumble(['tefon', 'sokik', 'niumem', 'siconu'])
    wj.unscramble()
