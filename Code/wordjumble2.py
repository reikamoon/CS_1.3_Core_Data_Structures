from hashtable import *
# Hashtable version
class WordJumble:
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
        for scrambled in self.jumbledwords:
            sorted_word = "".join(sorted(scrambled))
            print("The solution for " + scrambled + " is " + self.word_map.get(sorted_word))

    #Time Complexity: O(n)



if __name__ == '__main__':
    wj = WordJumble(['tefon', 'sokik', 'niumem', 'siconu'])
    wj.unscramble()
