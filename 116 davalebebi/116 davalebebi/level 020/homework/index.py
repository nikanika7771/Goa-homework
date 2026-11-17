#2
fruits = {"ვაშლი", "ბანანი", "ფორთოხალი", "მარწყვი", "ყურძენი", "ატამი"}
new_fruit = input("შეიყვანეთ ახალი ხილის სახელი: ")
fruits.add(new_fruit)
print(fruits)

#3
students = {"გიორგი", "ნინო", "დავითი", "მარიამი", "ლუკა"}
user_name = input("შეიყვანეთ მოსწავლის სახელი მოსაძებნად: ")
if user_name in students:
    print(f"დიახ, {user_name} არის მოსწავლეების Set-ში!")
else:
    print(f"არა, {user_name} არ არის მოსწავლეების Set-ში.")

#4
numbers = {4, 8, 15, 23, 42, 16, 10}
print(numbers)
num_to_remove = int(input("შეიყვანეთ რიცხვი, რომლის წაშლაც გსურთ: "))
if num_to_remove in numbers:
    numbers.remove(num_to_remove)
    print("წარმატებით წაიშალა!")
else:
    print("რიცხვი არ მოიძებნა Set-ში.")
print(numbers)

#5

animals = {"ლომი", "ვეფხვი", "დათვი", "მგელი", "მელა", "კურდღელი"}
print(len(animals))
new_animal = input("შეიყვანეთ ახალი ცხოველის სახელი: ")
animals.add(new_animal)
print(animals)
print(len(animals))


#6

colors = {"წითელი", "ლურჯი", "მწვანე", "ყვითელი", "შავი"}
color1 = input("შეიყვანეთ პირველი ფერი: ")
color2 = input("შეიყვანეთ მეორე ფერი: ")
if color1 in colors:
    print(f"ფერი '{color1}' არის Set-ში.")
else:
    print(f"ფერი '{color1}' არ არის Set-ში.")
if color2 in colors:
    print(f"ფერი '{color2}' არის Set-ში.")
else:
    print(f"ფერი '{color2}' არ არის Set-ში.")

    