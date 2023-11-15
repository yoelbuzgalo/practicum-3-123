def longest_words(word_list):
    """
    This function loops through words in a list, adds to the dictionary the longest word for any first character
    """
    longest_word_dict = dict()
    
    for word in word_list:
        if word[0] not in longest_word_dict:
            longest_word_dict[word[0]] = word
        else:
            if len(word) > len(longest_word_dict[word[0]]):
                longest_word_dict[word[0]] = word
    
    return longest_word_dict

