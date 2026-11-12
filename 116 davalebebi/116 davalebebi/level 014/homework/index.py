#1
n = int(input("შეიყვანეთ მთელი დადებითი რიცხვი: "))
temp = n
digit_count = 0
digit_sum = 0
even_count = 0
odd_count = 0

if temp == 0:
    digit_count = 1
    digit_sum = 0
    even_count = 1
else:
    while temp > 0:
        d = temp % 10
        digit_count += 1
        digit_sum += d
        if d % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        temp //= 10

sum_parity = "ლუწია" if digit_sum % 2 == 0 else "კენტია"

print(f"ციფრების რაოდენობა: {digit_count}")
print(f"ციფრების ჯამი: {digit_sum}")
print(f"ლუწი ციფრების რაოდენობა: {even_count}")
print(f"კენტი ციფრების რაოდენობა: {odd_count}")
print(f"ციფრების ჯამი {sum_parity}")


#2

numbers = []
for i in range(15):
    num = float(input(f"შეიყვანეთ მე-{i+1} რიცხვი: "))
    numbers.append(num)

max_num = numbers[0]
min_num = numbers[0]
positive_count = 0
negative_count = 0
zero_count = 0
total_sum = 0

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

    total_sum += num

average = total_sum / len(numbers)

if average > 0:
    avg_status = "დადებითია"
elif average < 0:
    avg_status = "უარყოფითია"
else:
    avg_status = "ნულის ტოლია"

print(f"უდიდესი: {max_num}")
print(f"უმცირესი: {min_num}")
print(f"დადებითი რიცხვების რაოდენობა: {positive_count}")
print(f"უარყოფითი რიცხვების რაოდენობა: {negative_count}")
print(f"ნულის ტოლი რიცხვების რაოდენობა: {zero_count}")
print(f"საშუალო არითმეტიკული: {average}")
print(f"საშუალო არითმეტიკული {avg_status}")

#3

secret_number = 37
attempts = 7
won = False

for i in range(attempts):
    guess = int(input(f"მცდელობა {i+1}/{attempts} - გამოიცანით რიცხვი: "))
    if guess == secret_number:
        print("გილოცავთ! თქვენ გამოიცანით საიდუმლო რიცხვი.")
        won = True
        break
    elif guess < secret_number:
        print("საიდუმლო რიცხვი უფრო დიდია.")
    else:
        print("საიდუმლო რიცხვი უფრო პატარაა.")

if not won:
    print(f"თამაში დასრულდა! სწორი პასუხი იყო {secret_number}.")


    #4
    start = int(input("შეიყვანეთ საწყისი რიცხვი: "))
end = int(input("შეიყვანეთ საბოლოო რიცხვი: "))

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0

for num in range(start, end + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count += 1
    elif num % 3 == 0:
        print("Fizz")
        fizz_count += 1
    elif num % 5 == 0:
        print("Buzz")
        buzz_count += 1
    else:
        print(num)

print(f"\nFizz რაოდენობა: {fizz_count}")
print(f"Buzz რაოდენობა: {buzz_count}")
print(f"FizzBuzz რაოდენობა: {fizzbuzz_count}")