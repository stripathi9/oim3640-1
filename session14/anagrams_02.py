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


File 
-> 
list of all English words ['a', 'aa', 'b',...] 

-> 
dict { key: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'], another_key:  ['resmelts', 'smelters', 'termless']} 

-> 

final list of lists of words: 
[ 
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']
]

1. read the file, store words into a list

- helper: given a word, return its signature. Example: 'deltas' -> 'adelts'

2. Create a ditionary: key is common characteristics among the angrams, value is a list of anagram words  key: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']  
('a', 'd', 'e', 'l', 't', 's')/'adelts' : ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']  
call ('a', 'd', 'e', 'l', 't', 's')/'adelts' as the signature of the word
   1. loop over the word list
        1. find the signature of the word
        2. if signature in the dictionary,
3. convert dict to list of lists of words
"""

def file_to_wordlist():
    """
    convert words.txt to a list of words, and return the list
    """

wordlist = file_to_wordlist()
print(len(wordlist), type(wordlist))

def list_to_dict(word_list):
    """
    Create a ditionary: key is common characteristics among the angrams, value is a list of anagram words  key: ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']  
    ('a', 'd', 'e', 'l', 't', 's')/'adelts' : ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']  
    call ('a', 'd', 'e', 'l', 't', 's')/'adelts' as the signature of the word
    1. loop over the word list
            1. find the signature of the word
            2. if signature in the dictionary,

    Return a dict
    """

list_for_test = ['deltas', 'abc', 'desalt', 'lasted', 'bca', 'salted', 'slated', 'aaa', 'staled']
print(list_to_dict(list_for_test))

# expected output: {'aaa': ['aaa'], 'abc': ['abc', 'bca'], 'adelts': ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']}


def get_signature(word):
    """
    given a word, return its signature. Example: 'deltas' -> 'adelts'
    """

print(get_signature("deltas"))


def dict_to_list(anagram_dict):
    """
    convert anagram_dict to a list of lists of anagram words
    """


def main():
    word_list = file_to_wordlist()
    anagrams_dict = list_to_dict(word_list)
    anagrams_list = dict_to_list(anagrams_dict) # result for Q1
    
