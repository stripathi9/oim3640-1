"""
Write a program that reads a word list from a file and prints all the sets of words that are anagrams. Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters.
How to represent the collection of letters in a way that can be used as a key?
Modify the program to prints the longest list of anagrams first, followed by the second longest, and so on.
"""


def is_anagram(word_1, word_2):
    return sorted(word_1) == sorted(word_2)


def file_to_wordlist():
    """
    convert words.txt to a list of words, and return the list
    Return:
    """
    words = []
    f = open('data/words.txt')
    for line in f:
        word = line.strip()
        words.append(word)
    return words


def get_anagrams():
    result = []
    visited = set()
    words = file_to_wordlist()
    for i, word in enumerate(words):
        if word in visited:
            continue
        anagrams = [word]
        visited.add(word)
        for word2 in words[i + 1 :]:
            if is_anagram(word, word2):
                anagrams.append(word2)
                visited.add(word2)
        if len(anagrams) > 1:
            result.append(anagrams)
            print('Found anagrams!')
            print(anagrams)
    return result


def main():
    anagrams_list = get_anagrams()
    print(anagrams_list)


if __name__ == "__main__":
    main()
