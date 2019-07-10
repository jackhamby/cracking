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


# For the string, calulate all permutations
string1 = "tacocat"

def getPermutations(string1):
    permutations = []
    if (len(string1) == 0):
        return permutations
    perms = permute("", string1[0], string1[1:])
    return perms

def permute(permutation, letter, string1):
    permutation += letter
    permutations = []
    if (len(string1) == 0):
        return permutation
    for i, l in enumerate(string1):
        permutations.extend( permute(permutation, l,  string1[0:i] + string1[i + 1:]) )
    return permutations

def factorial(n):
    product = 1
    while (n > 0):
        product *= n
        n -= 1
    return product




perms = getPermutations("tacocat")

print(f'string was {string1}')
print(f'permutation count was {len(perms)}')
print(f'should be {factorial(len(string1))}')
