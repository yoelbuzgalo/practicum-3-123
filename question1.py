def make_word_tuples(word_list):
    """
    This function returns a list of tuples, where each element of each tuple are letters of each word
    """
    return [tuple(word) for word in word_list]

# For manual testing purposes, you may change as needed
def main():
    word_list = ["dog","car","it","cake"]
    word_tuple_list = make_word_tuples(word_list)
    print("Word Tuples:",word_tuple_list)

if __name__ == "__main__":
    main()