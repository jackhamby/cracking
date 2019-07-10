# Method to replace all spaces with '%20'

# Assumptions: 
    # string array can hold any new characters (dont need to extend)
    # given length of string

# Big O
    # N is the length of string we're replacing
    # O(N)

def replaceSpace(string1):
    lstString = list(string1)
    for i, letter in enumerate(lstString):
        if (letter == " "):
            lstString[i] = "%20"
    return "".join(lstString)

sample_string = "hello my name is jack"
print(replaceSpace(sample_string))