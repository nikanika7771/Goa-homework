#2
user = input("enter your name: ")
age = int(input("enter your age"))
print (user > 18)

#3
number1 = int(input("enter your favourite number"))
number2 = int(input("enter number you dont like"))
print(number1 > number2)
print(number1 < number2)
print(number1 == number2)

#4
age = 18
password  = "arvici123"

age2 = int(input("enter your age: "))
password2 = input("enter your password: ")

print (age == age2)
print (password == password2 )

#5

age7 = int(input("enter your age: "))
product = int(input("enter product price: "))

result = (age7 >= 18) and (product > 100)
print(result)
