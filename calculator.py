
print("Enter The First Number: ")
num1 = float(input())
print("Enter The First Number: ")
num2 = float(input())
print("Choose A Mathematical Operation (+,-,*,/):")
ops = input()

result = 0

print("Result: " if ops == ('+' or '-' or '*' or '/') else "Incorrect Operation", end="")

if ops == '+':
    result = num1 + num2
elif ops == '-':
    result = num1 - num2
elif ops == '*':
    result = num1 * num2
elif ops == '/':
    result = num1 / num2

print(result)