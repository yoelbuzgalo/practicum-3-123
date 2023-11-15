import random

from question2 import fish_sort

def test_fish_sort_empty ():
    # Setup
    pond = []
    expected = []

    # Invoke
    barrel = fish_sort (pond)

    # Analysis
    assert barrel == expected

def test_fish_sort ():
    # Setup
    random.seed (1)
    pond = random.sample (range (1000), 10)
    expected = sorted (pond)

    # Invoke
    barrel = fish_sort (pond)

    #Analysis
    assert barrel == expected