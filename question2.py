def fish_sort (a_list):
    """
    This function finds and removes the smallest value in an unsorted list and adds it to a sorted list.
    """
    unsorted_list = [element for element in a_list] # Copies every element in a_list using list comprehension, this is to prevent pass by reference modification
    sorted_list = [] # Initialize empty list

    while len(unsorted_list) > 0:
        
        # Find the maximum value in a list
        max_value = 0
        for element in unsorted_list:
            if element > max_value:
                max_value = element
            
        # Find the mininum value
        min_value = max_value # Start with the highest value
        for element in unsorted_list:
            if element < min_value:
                min_value = element
        
        for i in range(0,len(unsorted_list)):
            if unsorted_list[i] == min_value:
                sorted_list.append(unsorted_list.pop(i)) # Pop the same smallest minimum value from the list and append it to the sorted list
                break # Break immediately

    return sorted_list



def main ():
    '''Ad Hoc tests you write should go in here'''
    some_list = [5,3,10,2,1]
    print(fish_sort(some_list))

if __name__ == "__main__":
    main ()
    