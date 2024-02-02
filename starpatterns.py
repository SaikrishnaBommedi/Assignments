#Star patterns

#Right Angle Traingle Patterns
n = int(input("Enter a Number: "))
for i in range(1,n+1):
    print(" * "*i)   

n = int(input("Enter a Number: "))
for i in range(n+1):
    print(" * "*(n-i))

n = int(input("Enter a Number : ")) 

for i in range(1, n+1): 
    for j in range(1, n+1): 
        if(j <= n - i): 
            print(' ', end = '  ') 
        else: 
            print("*", end = '  ') 
    print() 

n = int(input("Enter a Number : ")) 

for i in range(1, n+1): 
    for j in range(1, n+1): 
        if(j < i):
            print(' ', end = '  ')
        else:
            print('*', end = '  ')
    print()
