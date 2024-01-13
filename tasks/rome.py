"""
    Program do konwersji liczb zapisanych w systemie Rzymskim na liczby zapisane w systemie dziesietnym.

    Przyklady:

    IX: 9
    XLII: 42
    CCXIII: 213
    DCCCXC: 890
    CMXCIX: 999
    MMCDXLV: 2445
    MCMXCIV: 1994 
"""

def convert_rome_to_decimal(rome_digit):

    database = { "I":1, "V":5, "X":10, "L":50, "C": 100, "D":500, "M":1000 }

    result = []
    for sign in range(0, len(rome_digit)-1):
        if database[rome_digit[sign]] < database[rome_digit[sign+1]]:
            result.append(database[rome_digit[sign]] * ( -1 ))
        else:
            result.append(database[rome_digit[sign]])
    
    result.append(database[rome_digit[len(rome_digit)-1]])

    return sum(result)

assert convert_rome_to_decimal("IX") == 9
assert convert_rome_to_decimal("XLII") == 42
assert convert_rome_to_decimal("CCXIII") == 213
assert convert_rome_to_decimal("DCCCXC") == 890
assert convert_rome_to_decimal("CMXCIX") == 999
assert convert_rome_to_decimal("MMCDXLV") == 2445
assert convert_rome_to_decimal("MCMXCIV") == 1994
