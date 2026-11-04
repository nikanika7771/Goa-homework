#2
person = int(input("enter number: "))
if person > 0:
    print("დადებითი რიცხვი")
elif person <0:
    print("უარყოფითი რიცხვი")
else:
    print("ნულის ტოლი")
2
score = int(input("enter your score: "))
if 90<= score <= 100:
    print("A")
elif 80<= score <=89:
    print("B")
elif 70<= score <= 79:
    print("C")
elif 60 <= score <=69:
    print("D")
elif 0<= score <=59:
    print("F")
else:
    print("არასწორი მონაცემი")

#3

number = 7
guess = int(input("guess number: "))
while guess != number:
    print("Try again")
    guess = int(input("guess the number: "))
print("you guessed the number")

#4
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
operator = input("enter operator(+, *, / , : )")
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("you cant calculate")