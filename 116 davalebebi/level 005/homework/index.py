2
name = input("შეიყვანეთ თქვენი სახელი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
height = float(input("შეიყვანეთ თქვენი სიმაღლე: "))
print("user name is: " + name)
print("user age is: " + age)
print("user height is: " + height)

#3
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

4
productname = input("შეიყვანეთ პროდუქტის სახელი: ")
price = float(input("შეიყვანეთ პროდუქტის ფასი: "))
howmuch = int(input("შეიყვანეთ პროდუქტის რაოდენობა: "))
print(productname)
print("სრული ფასი არის :" + str(howmuch * price))


#5
name = input("შეიყვანეთ მოსწავლის სახელი: ")
grade1 = int(input("შეიყვანეთ ინგლისურის ქულა: "))
grade2 = int(input("შეიყვანეთ ისტორის ქულა: "))
grade3 = int(input("შეიყვანეთ მათემატიკის ქულა: "))
print(grade1, grade2, grade3)
averagegrade = int(input("Enter the total number for all three of your subjects"))

print(name)
print("your english grade is " +  "" + str(grade1))
print("your history grade is" + " " + str(grade2))
print("your math grade is " + " " + str(grade3))
print("your average grade is" + " " + str(averagegrade // 3))