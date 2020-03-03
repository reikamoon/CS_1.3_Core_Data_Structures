
class WordJumble:
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
        print("The solutions are: ")
        for scrambled in self.jumbledwords:
            sorted_word = "".join(sorted(scrambled))


if __name__ == '__main__':
    wj = WordJumble(['tefon', 'sokik', 'niumem', 'siconu'])
    wj.unscramble()
