
###
# Question 1:Write a function to move all zeros in a list to the end
###


l = [0, 3,1,0,50,1200,56]
print(l)

print("Task is to move all the zeros to the end of the list")


# My approach is to filter out the zero into another list 
# and then remove them from the first list, then append 
# the zero list to the filtered list"

zero_list = [x for x in l if x == 0]
for x in zero_list:
    l.remove(x)


print(zero_list+l)

###
# Question 2: How would you check if a word/string is a palindrome?
###
s =  "Hannah"
t = "Hanna"

def is_pal(s: str) -> bool:
    s = s.strip().lower()
    str_len = len(s)
    if s == "":
        return True
    if str_len==1:
        return True
    left, right = 0, str_len - 1
    while left != right:
        if s[left] != s[right]:
            return False
        left +=1
        right -= 1
    return True 


### 
# Question 3: Given a sentence, find the shortest word.
###
def find_shortest_word(sentence: str) -> str:
    # Convert the sentence into a dictionary of word->length
    word_list = sentence.split()
    print (f"Debugging>>> Word list type: {type(word_list)} and contains: {word_list}")
    #Create an array of arrays that has the format [word, word_length]
    word_length = [[word, len(word)] for word in word_list]
    print(f"Debugging>>> Type of word_length is {type(word_length)} and contains: {word_length}")
    # Sort the resulting 2d array by the second element. element at index 1 asc
    word_length.sort(key=lambda x: x[1])
    print(word_length)
    return word_length[0][0]


if __name__ == "__main__":
    print("Testing is_palindrome method which for now returns TRUE always.")
    print(is_pal("Ana  "))
    print("Testing shortest word in a sentence")
    print(find_shortest_word("I am a boy"))
