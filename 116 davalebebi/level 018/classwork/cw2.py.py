#You get an array of numbers, return the sum of all of the positives ones.

def positive_sum(arr):
    total = 0
    for i in arr:
        if i >0:
            total += i 
    return total

#Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    total = 0
    for i in numbers:
        total += i ** 2
    return total 

#Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count = 0
    for letter in sentence:
        if letter in "aeiou":
            count += 1
    return count 

#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")
    x = 0
    o = 0
     
    for letter in s:
        if letter == "x":
            x += 1
        elif letter == "o":
             o += 1

    if  x == 0:
        return True
    else:
        return False