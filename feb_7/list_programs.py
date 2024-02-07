l = [10,15,"Ajay",4,50]
l.sort()
print(l) #Type Error

l = [15,11,13,21,5]
l.sort()
print(l) #[5, 11, 13, 15, 21]

l = [10,6.5,13,9.8]
l.sort()
print(l) #[6.5, 9.8, 10, 13]

# 4*4 matrix 
l = [[2,4,6,8],[10,12,14,16],[18,20,22,24],[26,28,30,32]]

#list comperhensive 
#1>Odd numbers in the range 0-30
odd_nums = [i for i in range(31) if i%2!=0]
print(odd_nums)

#2>Power of 2 
res = [2**i for i in range(1,11)]
print(res)

#3>Multiples of 2 
res = [2*i for i in range(1,11)]
print(res)

#4>words program
words=['balaya','shafi','chiru']
res = [w[0] for w in words]
print(res)

#5>vowels program 
a = input()
v = ['a','e','i','o','u']
s = [i for i in a if i in v]
print(s)