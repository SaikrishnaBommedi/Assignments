#arthamatic operators

#int and int
a = 25
b = 10
print(a+b) #35  
print(a-b) #15
print(a*b) #250
print(a/b) #2.5
print(a%b) #5

#int and string
a = 3
b = "hello"
print(a+b) #Unsupported error  
print(a-b) #Unsupported error
print(a*b) #hellohellohello
print(a/b) #Unsupported error
print(a%b) #Unsupported error

#string and string
a = 'hi'
b = 'hello'
print(a+b) # hihello
print(a-b) #unsupported error
print(a*b) #unsupported error
print(a/b) #unsupported error
print(a%b) #unsupported error

#bool and int
a = True
b = 1
print(a+b) #2
print(a-b) #0
print(a*b) #1
print(a/b) #1.0
print(a%b) #0

#bool and bool
a = True
b = False
print(a+b) #1
print(a-b) #1
print(a*b) #1
print(a/b) #Zerodivision Error
print(b/a) #0.0
print(a%b) #Zerodivision Error
print(b%a) #0

#float and int
a = 2.3
b = 's'
print(a+b) #unsupport error
print(a-b) #unsupport error
print(a*b) #unsupport error
print(a/b) #unsupport error
print(a%b) #unsupport error


#Comparison operators
#int and int
a = 10
b = 15
print(a>b) #False
print(a<b) #True
print(a==b) #False
print(a!=b) #True

#int and string
a = 5
b = 's'
print(a<b) #unsupport error
print(a>b) #unsupport error
print(a==b) #False
print(a!=b) #True

#int and bool
print(0==False) #True
print(1==False) #False
print(1>False) #True
print(1!=False) #True
print(1<False) #False

#string and bool
print('s'==False) #False
print('s'==True) #False
print('s'!=False) #True
print('s'>False) #Unsupported error
print('s'<False) #Unsupported error

#Logical Operators
#int and int
a = 10
b = 5
print(a>5 and b<10) #True
print(a>5 or b>10) #True
print(not(a>5 or a>10)) #False

