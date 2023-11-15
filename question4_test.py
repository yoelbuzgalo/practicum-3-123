from question4 import *

def read_word_list(filename):
    with open(filename) as words_file:
        word_list = []
        for line in words_file:
            word = line.strip().lower()
            if len(word) > 0: # account for blank lines
                word_list.append(word)
        return word_list

def test_longest_small():
    # setup
    word_list = ["a", "cry", "be", "aardvark", "crooked", "alpha", "bonnet", 
        "bee", "crook"] 

    # invoke
    longest = longest_words(word_list)

    # analyze
    assert "aardvark" == longest["a"]
    assert "bonnet" == longest["b"]
    assert "crooked" == longest["c"]

def test_longest_large():
    # setup
    word_list = read_word_list("data/words.txt")

    # invoke
    longest = longest_words(word_list)

    # analyze
    assert "antidisestablishmentarianism" == longest["a"]
    assert "straight-from-the-shoulder" == longest["s"]
    assert "quasi-characteristically" == longest["q"]
