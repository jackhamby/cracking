
# Check permutation, given 2 strings, is one a permutation
# of the other

# Qs: 
    # What kind of strings? Ascii or unicode? If ascii is extended ascii? 
    # I need to know possible character count and mem usage

# Assumtions:
    # Assume extented ascii, i.e. 256 avail chars, each char represented by 8 bits

# Big O 
    # Let N equal size of each string (assuming strings are same size)
    # time_complexity = O(N) + O(N) + O(256)
    #                 = O(N) + O(N) + O(1)
    #                 = O(N)

import string

def perm(string1, string2):
    if (len(string1) != len(string2)):
        return False
    seenLetters = [ [] for i in range(256)] # Assume string extended ascii
    seenLetters2 = [ [] for i in range(256)] 
    for letter in string1:
        index = string.ascii_lowercase.index(letter)
        seenLetters[index].append(letter)
    for letter in string2:
        index = string.ascii_lowercase.index(letter)
        seenLetters2[index].append(letter)
    for i, arr in enumerate(seenLetters):
        if (len(arr) != len(seenLetters2[i])):
            return False
    
    return True


# True
test1 = "abcd"
test12 = "cdab"

# False
test2 = "asbsdsaf"
test22 = "asbsdsaef"


print(perm(test1, test12))
print(perm(test2, test22))


    
    
    