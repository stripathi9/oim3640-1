# https://www.nytimes.com/puzzles/spelling-bee

from word_sol import uses_only

# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the string available.
#     """
#     for letter in word:
#         if letter not in available:
#             return False
#     return True


# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     # for letter in required:
#     #     if letter not in word:
#     #         return False
#     # return True
#     return uses_only(required, word)


def spell_bee(required, available):
    f = open('data/words.txt')
    for line in f:
        word = line.strip()

        if (
            len(word) >= 4
            and uses_only(word, available)
            and required in word
        ):
            # print(word)

            if len(set(word)) == len(available):
                print(f' We found a pangram: {word}')
            else:
                print(word)

def main():
    spell_bee(required='l', available='lygifvn')


if __name__ == "__main__":
    main()
