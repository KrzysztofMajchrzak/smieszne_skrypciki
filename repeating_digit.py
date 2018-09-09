def RepeatingDigit(list_of_digits):
    """
    Returns first duplicate from the list and indexes of the first two same elements

    Arguments:
    list_of_digits - list with digits from 0 to 9 (included); must contain at least one pair of the same elements
    """	
    for second_index in range(0, len(list_of_digits)):
        for first_index in range(0, second_index):
            if list_of_digits[second_index] == list_of_digits[first_index] and first_index != second_index:
                return list_of_digits[second_index], first_index, second_index
                
list_of_digits = [4, 4, 6, 4, 3, 4, 6, 2, 1, 7, 3, 6, 8, 8, 9,]                                                 
print (RepeatingDigit(list_of_digits))   