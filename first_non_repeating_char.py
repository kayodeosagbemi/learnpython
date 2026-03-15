def first_non_repeating_char(s: str)->str:
    """
    Problem Statement
    Given a string s consisting of lowercase English letters, 
    find the first character that does not repeat anywhere in the string.

    If there is no such character, return '_'.
    Your solution should return the character 
    whose first occurrence has the smallest index.
    """
    dict = {}
    for c in s:
        dict[c] = dict.get(c, 0) + 1

    
    # loop through the dictionary and find the first string which has a frequency of 1. break early
    for  k, v in dict.items():
        if v == 1:
            return k 
        
    return "_"

print(first_non_repeating_char("abbaccscc"))
