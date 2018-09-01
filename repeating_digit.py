digits = [1, 5, 7, 3, 5, 8, 3, 6]
for d1 in range(0, len(digits)):
    for d2 in range(1, len(digits)):
        if digits[d1] == digits[d2] and d1 != d2:
            print (digits[d1])
            
print ("Indeks pierwszego:",digits.index(d1))

