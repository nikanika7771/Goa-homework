# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded down.

# For example:

#1

def litres(time):
     return int(time * 0.5 )

#Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers 
# has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2  %  2 == 1:
        return True
    elif flower1 % 2 == 1 and flower2 % 2 == 0:
        return True
    else:
        return False



    #3

    # Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]

def digitize(n):
    List = []
    for i in str(n):
        List.append(int(i))
    List.reverse() 
    return List

#4
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts a non-negative integer and returns an integer.

# Happy Coding!

def square_digits(num):
    numbers = ""
    for i in str(num):
        numbers += str(int(i) ** 2)
    return int(numbers)
#5
# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.


def disemvowel(string_):
    result = ""
    xmovnebi = "AEIOUaeiou"
    for i in string_:
        if i not in xmovnebi:
            result += i
    return result
        