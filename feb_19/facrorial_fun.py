def factorial(num):
    if num==1:
        return num
    else:
         return num*factorial(num-1)

n = int(input("Enter a number: "))
print(factorial(n))