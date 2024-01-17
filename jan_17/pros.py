#program to find biggest of 2 given numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1>num2:
    print(num1," is bigger than ",num2)
else:
    print(num2," is bigger than ",num1)

#program to print biggest of 3 number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter second number: "))

if num1>num2 and num1>num3:
    print(num1," is bigger than ",num2," and ",num3)
elif num2>num1 and num2>num3:
    print(num2," is bigger than ",num1," and ",num3)
else:
    print(num3," is bigger than ",num1," and ",num2)

#program to check weather the given number is in between 1 to 100
n = int(input("Enter the number: "))
if n>0 and n<=100:
    print(n," is in between 1 to 100")
else:
    print(n," is not in between 1 to 100")