#1
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

user_input = float(input("შეიყვანეთ რიცხვი: "))
print(check_number(user_input))

#2
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(calculate_sum(5))
#3
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "ნულზე გაყოფა შეუძლებელია"
        return num1 / num2
    else:
        return "Invalid Operation"

print(calculator(10, 5, "+"))


#4
def password_checker(password):
    if len(password) <= 8:
        return False
    
    has_letter = False
    has_digit = False
    
    for char in password:
        if ("a" <= char <= "z") or ("A" <= char <= "Z"):
            has_letter = True
        elif "0" <= char <= "9":
            has_digit = True
            
    return has_letter and has_digit

print(password_checker("Password123"))
