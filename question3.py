def unique_elements(a_sequence):
    """
    This function generates and returns a list of unique elements in a given sequence
    """

    unique_set = set(a_sequence) # Initialize an unique set, passing every item in a sequence

    return [set_item for set_item in unique_set] # Return a list of unique items

# For manual testing purposes, you may change as needed
def main():
    print(unique_elements("aardvark"))
    print(unique_elements([1, 4, 0, 3, 0, 4, 8, 1]))

if __name__ == "__main__":
    main()