# method for string compression, if compressed string is larger than input
# return input string
#   input: aaaabbbbcccdddaa
#   output: a4b4c3d3a2

# Questions
    # What kind of string is it? Ascii or Unicode? 
        # Effects amount of memory i will use, is it extended ascii?
    

# Assumptions:
    # assume lower case letters from a-z

# Big O
    # O(N) we loop through N times, where N is the size of string1


def compress(string1):
    previous_letter = False
    repeat = 0
    compressed_string = ""
    for i, letter in enumerate(string1):
        if (not previous_letter):
            previous_letter = letter
            repeat = 1
        elif (previous_letter == letter):
            repeat += 1
        elif (previous_letter != letter):
            compressed_string += f'{previous_letter}{repeat}'
            previous_letter = letter
            repeat = 1
    if (previous_letter):
        compressed_string += f'{previous_letter}{repeat}'

    return compressed_string



sample_string = "aabcccccaag"
sample_string2 = "abcdefg"

print(compress(sample_string))
# print(compress(sample_string2))