import re
import itertools

def solvePuzzle(puzzle):
    # get all the words
    words = re.findall('[A-Z]+' , puzzle.upper())

    # get all the unique characters
    unique_characters = set("".join(words))

    print (unique_characters)

    # Assert that length of the set is less than number 10
    assert len(unique_characters)<=10 , "Too many characters"

    # get the first letters
    first_letters = {word[0] for word in words}

    n = len(first_letters)

    sorted_characters = ''.join(first_letters) + ''.join(unique_characters - first_letters)

    print (sorted_characters)

    characters = tuple(ord(c) for c in sorted_characters)
    digits = tuple(ord(c) for c in '0123456789')

    zero = digits[0]

    # itertools.permutations takes a sequence and r and generates nPr for that
    # sequence. It returns an iterator

    for guess in itertools.permutations(digits , len(characters)):
        if zero not in guess[:n]:

            # String translate uses a translation table/dictionary to
            # translate the string according to the dictionary
            # eg. {'A' : '1' , 'B' : '2'} if used as translation table then
            # AB would translate to 12

            # zip returns a list of tuples, where the i-th tuple contains the i-th
            # element from each of the argument sequences or iterables

            equation = puzzle.translate(dict(zip(characters,guess)))
            if eval(equation):
                return equation


if __name__ == "__main__":
    import sys
    for puzzle in sys.argv[1:]:
        print (puzzle)
        solution = solvePuzzle(puzzle)
        if solution:
            print (solution)
