###Anagram detection interview practice 
### anagram is a string that is the same value when reversed.
def detect_anagram(s: str, t: str)->bool:
    if s is None :
        raise ValueError("The string 's' is None")
    
    if t is None:
        raise ValueError("The string 't' is None")
    
    if not isinstance(s, str) or not isinstance(t, str):
        raise TypeError("The two arguments should be strings")
    
    if len(s)!= len(t):
        return False
    
    #Normalise to lower case
    s=s.lower()
    t=t.lower()
    dict_s={}
    dict_t={}
    for i in range(len(s)):
        key = s[i]
        dict_s[key] = dict_s.get(key, 0) + 1
        key = t[i]
        dict_t[key] = dict_t.get(key, 0) + 1

    # Now to compare the frequencies for both dictionaries
    for k in dict_s.keys():
        if dict_s.get(k, 0) !=dict_t.get(k, 0):
            return False
        
    return True

print("Testing Anagrams ....")
# print(detect_anagram("listen", "silent"))
print(detect_anagram("conversation", "voicesranton"))
# print(detect_anagram("hello", "hell"))
# print(detect_anagram(12, "21"))        
    
    
