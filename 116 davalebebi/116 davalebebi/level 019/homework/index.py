#1

fruits = ("ვაშლი", "ბანანი", "ფორთოხალი", "მარწყვი", "ყურძენი", "ატამი")
print("პირველი ხილი:", fruits[0])      
print("მესამე ხილი:", fruits[2])     
print("ბოლო ხილი:", fruits[-1])
print("Tuple-ის სიგრძე:", len(fruits))

#2
students = ("გიორგი", "ნინო", "დავითი", "მარიამი", "ლუკა")
user_name = input("შეიყვანეთ მოსწავლის სახელი მოსაძებნად: ")
if user_name in students:
    print(f"დიახ, {user_name} არის მოსწავლეების სიაში!")
else:
    print(f"არა, {user_name} არ არის მოსწავლეების სიაში.")

    #3
numbers = (4, 8, 15, 8, 23, 42, 8, 16)
target = 8
count_target = numbers.count(target)
index_target = numbers.index(target)
print(f"რიცხვი {target} tuple-ში მეორდება {count_target}-ჯერ.")
print(f"რიცხვი {target}-ის პირველი გამოჩენის ინდექსია: {index_target}")


#4
cities = ("თბილისი", "ბათუმი", "ქუთაისი", "რუსთავი", "ზუგდიდი", "ფოთი")
print("პირველი სამი ქალაქი:", cities[:3])
print("ბოლო სამი ქალაქი:", cities[-3:])
print("მთლიანი Tuple:", cities)