# Palindrome permutation
    # Given a string, check if it the permutation of some palindrome
    # palidrome: same spelled forwards as it is backwards

# Assumptions
    # Dictionary words not required
    # Spaces and non-letter characters dont count

# Big O
    # Get all permutations for given word of length N
    # O(N!)
    # For each permutation check if palindrome
        # Reverse char array
            # O(N)
    # O(n!) * O(N)

non_letters =  "!@#&()–[{}]:;',?/*"

def get_permutations(string1):
    permutations = []
    if (len(string1) == 0):
        return permutations
    perms = permute("", string1[0], string1[1:])
    return perms

def permute(permutation, letter, string1):
    permutation += letter
    permutations = []
    if (len(string1) == 0):
        return [permutation]
    for i, l in enumerate(string1):
        permutations.extend( permute(permutation, l,  string1[0:i] + string1[i + 1:]) )
    return permutations

def reverse(word):
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_word += word[i]
    return reversed_word

def factorial(n):
    product = 1
    while (n > 0):
        product *= n
        n -= 1
    return product

def is_palidrome(word):
    if (word == reverse(word)):
        return True
    return False


def palidrome_permutation(word):
    for letter in word:
        if (letter in non_letters):
            print(f'replacing {letter} with space')
            word = word.replace(letter, "")
            print(word)
    perms = get_permutations(word)
    for perm in perms:
        if (is_palidrome(perm)):
            return True
    return False


result = palidrome_permutation("pareper")
print(result)