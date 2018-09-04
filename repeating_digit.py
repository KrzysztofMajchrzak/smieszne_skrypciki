digits = [1, 7, 1, 6, 3, 1, 1, 7, 3, 6, 8, 8, 9]
def sprawdzanie(digits):
    global d1
    for d1 in range(0, len(digits)):
        for d2 in range(0, d1):
            if digits[d1] == digits[d2] and d1 != d2:
                return digits[d1] 
print (sprawdzanie(digits))      