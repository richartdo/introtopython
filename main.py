number1 = float(input("Enter the first number: "))
operator = input("Enter the mathematical operator: ")
number2 = int(input("Enter the second number: "))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "/":
    result = number1 / number2
elif operator == "*":
    result = number1 * number2

print(result)