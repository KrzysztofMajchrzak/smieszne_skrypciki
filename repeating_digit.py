digits = [7, 6, 4, 3, 1, 1, 7, 3, 6, 8, 8, 9,]
def repeating_digit(digits):
    for first_digit in range(0, len(digits)):
        for second_digit in range(0, first_digit):
            if digits[first_digit] == digits[second_digit] and first_digit != second_digit:
                return digits[first_digit]                                                 
print (repeating_digit(digits)) 