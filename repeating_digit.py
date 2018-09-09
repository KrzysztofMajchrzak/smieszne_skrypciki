def RepeatingDigit(list_of_digits):
    for first_index in range(0, len(list_of_digits)):
        for second_index in range(0, first_index):
            if list_of_digits[first_index] == list_of_digits[second_index] and first_index != second_index:
                return list_of_digits[first_index], second_index, first_index
                
list_of_digits = [4, 4, 6, 4, 3, 4, 6, 2, 1, 7, 3, 6, 8, 8, 9,]                                                 
print (RepeatingDigit(list_of_digits))   