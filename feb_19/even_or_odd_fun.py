def even_or_odd(num):
    if num%2==0:
        return "Even number"
    else:
        return "Odd number"

n = int(input("Enter a number: "))
print(even_or_odd(n))