# Edits: - insert
#        - remove
#        - replace
# given 2 strings, can they be equal in 0 or 1 edits?

# Key points
    # only 0 to 1 edits, which means only 1 replace, an insert or a removal

# Big O
    # O(n) where n is the size of larger string
    # 


def edits(str1, str2):
    if (str1 == str2):
        return True
    elif ( not(-2 < len(str1) - len(str2) < 2)):
        return False
    elif (len(str1) > len(str2)):
        # Add to str2
        for i, letter in enumerate(str1):
            if (i == len(str1)):
                str2 += letter
            if (letter != str2[i]):
                str2 = str2[0:i] + letter + str2[i:]
                break
        if (str1 == str2):
            return True
        return False
    elif (len(str1) < len(str2)):
        # Add to str1
        for i, letter in enumerate(str2):
            if (i == len(str2)):
                str1 += letter
            if (letter != str1[i]):
                str1 = str1[0:i] + letter + str1[i:]
                break
        if (str1 == str2):
            return True
        return False
    else:
        # Replace
        for i, letter in enumerate(str2):
            if (letter != str1[i]):
                str1 = str1[0:i] + letter + str1[i + 1:]
                break
        if (str1 == str2):
            return True
        return False

        


    

result = edits("pale", "ple")
print(result)  # True
result = edits("ple", "pale")
print(result)  # True
result = edits("pale", "bale")
print(result) # True
result = edits("pale", "bake")
print(result) # False


