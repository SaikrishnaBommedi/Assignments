'''#compound assignment operators
a = 12
a &=7 
print(a) #4

a = 10
a +=5
print(a) #15

a = 10
a *= 5
print(a) #50

a = 10
a -= 5
print(a) #5

a = 10
a /= 5
print(a) #2.0

a = 10
a %= 5
print(a) #0

#Identity operator
a  = 25
b = 25
print(a is b) #True

a = 25
b = 20
print(a is b) #False

a = [1,2,3]
b = [1,2,3]
print(a is b) #False

a = 'hi'
b = 'hi'
print(a is b) #True

a = True
b = 1 
print(a is b) #False

#Membership operator
a = [1,2,3,'hi',7.6]
print(7.6 in a) #True

a = (10,21,True)
print(True not in a) #False

a = "Good morning guys"
print('guys' in a) #True

a = 171
print(1 in a) #Type Error

a = [1,2,3,4,5,5,6]
print(7 not in a) #True

#Ternary Operator
a = 21 if 21%3==0 else 10
print(a)

a = 10 if 10>21 else 25
print(a)

#input and output statements
a = int(input("enter first val:"))
b = int(input("enter second val:"))
print("sum of values:",a+b)
'''
#Bitwise operators
a = 10
b = 25
print(a%5==0 & b%5==0) #True

a = 20
b = 25
print(a|b) #29

a = 10
b = 20
print(a^b) #30
print(a<<b) #10485760
print(a>>b) #0