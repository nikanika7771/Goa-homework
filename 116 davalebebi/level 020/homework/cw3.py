# Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

# The order of the sequence has to stay the same.

# Examples:

def distinct(seq):
    sum = []
    for i in seq:
        if i not in sum:
            sum.append(i)
    return sum


# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

# a can contain numbers or strings. x can be either.

# Return true if the array contains the value, false if not.
def check(seq, elem):
    return elem in seq



# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)



def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'




# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the array is empty, return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: [-2.398]
# Output: -2.398

# Input: []
# Output: 0

# Assumptions


def sum_array(a):
    return sum(a)