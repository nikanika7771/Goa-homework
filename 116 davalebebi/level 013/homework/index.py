#1 

number = 123675312354
digit = 2

count = 0
temp = number

if temp == 0 and digit == 0:
    count = 1
else:
    while temp > 0:
        last_digit = temp % 10
        if last_digit == digit:
            count += 1
        temp //= 10

print(count)


#2

number = 360
temp = number

divisor = 2
factors = []

while temp > 1:
    while temp % divisor == 0:
        factors.append(divisor)
        temp //= divisor
    divisor += 1

print(*factors)


#3


limit = 100

a = 0
b = 1

while a < limit:
    print(a, end=" ")
    a, b = b, a + b

print()



#4

numbers = [4, 17, 2, 9, 31, 6]

if numbers:
    max_num = numbers[0]
    min_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    print(f"უდიდესი: {max_num}, უმცირესი: {min_num}")

    #5

    numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]
    left += 1
    right -= 1

print(numbers)