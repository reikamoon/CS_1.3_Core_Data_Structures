#!python
import string
import random
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
input = 'palindrome'

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    if text == "":
        return True
    text = text.lower()
    i, j = 0, len(text) - 1
    while i < j:
        while not text[i].isalnum():
            i += 1
        while not text[j].isalnum():
            j -= 1
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if text == "":
        return True
    if left is None:
        left = 0
        right = len(text) - 1

    while not text[left].isalnum():
        left += 1
    while not text[right].isalnum():
        right -= 1

    if text[left].lower() != text[right].lower():
        return False
    elif left >= right:
        return True
    else:
        return is_palindrome_recursive(text, left + 1, right - 1)

def anagram(input):
    anagram = ""
    for i in range(len(input)):
        pos = random.randint(0, len(input)-1)
        anagram += input[pos]
        input = input[:pos] + input[pos+1:]
    print(anagram)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    anagram(input)
