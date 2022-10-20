"""
Write a program that reads a word list from a file and prints all the sets of words that are anagrams. Here is an example of what the output might look like:
['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
['generating', 'greatening']
['resmelts', 'smelters', 'termless']

Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters.
How to represent the collection of letters in a way that can be used as a key?
Modify the program to prints the longest list of anagrams first, followed by the second longest, and so on.
"""

"""
Psuedo-code


Intuitive solution:

Loop over the word list:
   one word -> compare this word with all the other words

O(n * n)


file -> word list (after cleaning the data) -> dict {key: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'] } -> list of lists of words

1. read the file, store all the words into a list ['a', 'aa', 'abc']

- helper: word -> sorted tuple/string

2. create a dict, key is sorted tuple or string, value is a list of words that are in common which can built from the key
   1. loop over the entire list of words
        1. get the tuple - we could use the helper function
        2. store the word into dict
        3. ...
3. dict -> list of lists of anagrams, we only want those lists that have more than 1 word inside.

('a', 'd', 'e', 'l', 's', 't')/'adelst':   ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']

"""

def file_to_wordlist():
    """
    convert words.txt to a list of words, and return the list
    Return: 
    """

def sort_word(word):
    """
    The helper function.
    word -> sorted string
    """


print(sort_word('deltas'))

def list_to_dict(word_list):
    """
    word_list: a list of all the English words
    Return a dict, key is sorted string, value is a list of words that are in common which can be built from the key
    """

list_for_test = ['deltas', 'abc', 'desalt', 'bca', 'lasted', 'salted', 'slated', 'staled', 'a']

result = list_to_dict(list_for_test)

# expected result {'a': ['a'], 'abc':['abc', 'bca'], 'adelts': ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'] }


def dict_to_list(anagram_dict):
    """
    Return the list of lists of anagram words, only those that have more than 1 word
    """
