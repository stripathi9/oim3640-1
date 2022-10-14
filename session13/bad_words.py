def get_bad_words():
    """return a list of bad words"""
    f = open('data/random_words.txt')

    bad_words = []  # for return

    for line in f:
        word = line.strip()
        # check if the word meets all the three requirements, if so, append the word the into bad_words
        if (
            has_covid(word) and has_twice(word) and same_first_last(word)
        ):  # fake it till make it
            bad_words.append(word)

    return bad_words


def has_covid(word):
    """return True if the word contains at least 3 letters from covid"""
    


def has_twice(word):
    """return True if ..."""


def same_first_last(word):
    """return True if ..."""
    return word[0] == word[-1]


def main():
    result = get_bad_words()
    print(len(result))
