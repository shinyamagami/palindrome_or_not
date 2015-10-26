# Shin Yamagami
# Oct 26th, 2015
# This program check if a string given by a user is palindrome or not.
# This program is case-insensitive.

# get a string
c = input('Please input a sequence of characters: ').lower()
# define a function that judge if the string is palindrome or not
def is_palindrome(c):
    i = 0
    a = 0
    b = -1
    # Repeat until the variable i reach to the length of the string
    while i < len(c):
        if c[a] != c[b]:
            return False
        a += 1
        b -= 1
        i += 1
    return True
# output True or False
print(is_palindrome(c))
