
# Determine if a string has all unique characters
# Qs: Type of the string? 
    # Is it ascii?
    # Unicode?
        # Utf-8
        # Utf-16
        # etc? 

# Assumptions: Is extended ascii so limit of 256 chars
# Big O
    # Let N be the length of a_string
    # O(N)

import string

def is_unique(a_string):
    hash_array = [ False for i in range(256) ]
    for letter in a_string:
        index = string.ascii_lowercase.index(letter)
        if (hash_array[index]):
            return False
        hash_array[index] = True
    return True

unique_letters = "abcdefgh"
nonunique_letters = "abcdefghig"

print(is_unique(unique_letters))
print(is_unique(nonunique_letters))
    
