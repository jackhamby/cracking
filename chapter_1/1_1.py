import string

def is_unique(a_string):
    hash_array = [ [] for i in range(27) ]
    for letter in a_string:
        index = string.ascii_lowercase.index(letter)
        if (len(hash_array[index]) > 0):
            return False
        hash_array[index].append(letter)
    return True

unique_letters = "abcdefgh"
nonunique_letters = "abcdefghig"

print(is_unique(unique_letters))
print(is_unique(nonunique_letters))
    
