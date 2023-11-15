from question1 import *

def test_make_word_tuples_empty():
    # setup
    word_list = []
    expected = []

    # invoke
    actual = make_word_tuples(word_list)

    # analyze
    assert expected == actual

def test_make_word_tuples_1_word():
    # setup
    word_list = ["rabbit"]
    expected = [("r","a","b","b","i","t")]

    # invoke
    actual = make_word_tuples(word_list)

    # analyze
    assert expected == actual

def test_make_word_tuples_many_element():
    # setup
    word_list = ["dog","car","it","cake","house","a","shark","bus","crocodile"]
    expected = [('d', 'o', 'g'), ('c', 'a', 'r'), ('i', 't'),
                ('c', 'a', 'k', 'e'), ('h', 'o', 'u', 's', 'e'), ('a',),
                ('s', 'h', 'a', 'r', 'k'), ('b', 'u', 's'),
                ('c', 'r', 'o', 'c', 'o', 'd', 'i', 'l', 'e')]

    # invoke
    actual = make_word_tuples(word_list)

    # analyze
    assert expected == actual