#Odd nums series
n = int(input('Enter a number: '))
sum = 0

for i in range(1,(2*n)+1,2): #10 odd numbers: 1,3,5,7,9,11,13,15,17,19
    sum+=i 

print(sum) #100

#squares series
num = int(input())
tot = 0
for i in range(1,num+1):
    tot+= i*i 
print(tot)