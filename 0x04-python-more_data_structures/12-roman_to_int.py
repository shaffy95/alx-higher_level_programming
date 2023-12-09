#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    sum_value = 0
    roman_value = 0

    for numeral in roman_string:
        if numeral not in value:
            return 0

        roman_dict = value[numeral]
        sum_value += roman_dict

        if roman_dict > roman_value:
            sum_value -= 2 * roman_value

        roman_value = roman_dict

    return sum_value
