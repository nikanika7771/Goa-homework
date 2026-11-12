#1

shopping_list = ["პური", "რძე", "კვერცხი", "ყველი", "ყავა"]

new_product = input("შეიყვანეთ ახალი პროდუქტი: ")
shopping_list.append(new_product)

print(shopping_list)

#2

students = ["გიორგი", "ანი", "ლუკა", "ნინო", "დემეტრე"]

students.sort()

print(students)

#3
animals = ["ლომი", "ვეფხვი", "დათვი", "მგელი", "მელა", "კურდღელი"]

animal_to_remove = input("შეიყვანეთ ცხოველის სახელი, რომელიც გსურთ წაშალოთ: ")

if animal_to_remove in animals:
    animals.remove(animal_to_remove)
    print("განახლებული სია:", animals)
else:
    print("ეს ცხოველი სიაში არ მოიძებნა.")
    #4

    numbers = [10, 20, 30, 40, 50]

numbers.pop()

index = int(input("შეიყვანეთ ინდექსი, სადაც გსურთ ახალი რიცხვის დამატება: "))
value = int(input("შეიყვანეთ ახალი რიცხვი: "))
numbers.insert(index, value)

numbers.reverse()

print(numbers)