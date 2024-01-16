#bytes datatype
vals = [1,2,3,4]
a = bytes(vals)

print(type(a)) #bytes

for i in a:
    print(i) #bytes are preserved

print(a[2]) #3 (indexing allowed)
print(a[:2]) #[1,2] (slicing allowed)

a[3]=28
print(a) #error (bytes are immutable)

vals.append(300)
b = bytes(vals) #bytes must be in range(0,256)

#bytearray datatype
ab = [11,12,13,14,15]
c = bytearray(ab)

print(type(c)) #bytearray type

ab[2]=35
c=bytearray(ab)
print(*c) #[11,12,35,14,15] (bytearrays are mutable)

print(c[2]) #35 (allows indexing)

print(*c[1:4]) # 12 35 14 (allows slicing)

ab.append(270)
c = bytearray(ab) #range must be(0,256)


#List datatype: A group of elements in single entity
d = [24,27,30,12,11] #represent with square brackets
print(type(d)) #list

d.append(5) #append function: adding values in list
d.append("qwr")
print(d) #[24, 27, 30, 12, 11, 5, 'qwr'] (insertion order is preserved)

d.append(False)
d.append(4.78)
print(d) #[24, 27, 30, 12, 11, 5, 'qwr', False, 4.78] (it allows hetrogenius datatypes(different datatypes))

d[1]=20
print(d) #[24, 20, 30, 12, 11, 5, 'qwr', False, 4.78] (lists are mutable)

print(d[2]) #30 (allows indexing)
print(d[:3]) #[24, 20, 30] (allows slicing)

d.append(5)
d.append(False)
print(d) #[24, 27, 30, 12, 11, 5, 'qwr', False, 4.78, 5, False] (allows duplicates)

d = [11,12,13,14,15]
print(d*2) #[11, 12, 13, 14, 15, 11, 12, 13, 14, 15] (multiplication with number)
print(d+d) #[11, 12, 13, 14, 15, 11, 12, 13, 14, 15] (addition operator with list)
print(d*d) #type error
print(d+2) #type error


#Tuple datatype: A group of elements in single entity
e = (1,2,'ravi') #represents with round brackets
print(type(e)) #tuple 

#tuples are immutable
#e[1] = 7
print(e) #error

#it allows hetrogenius datatypes
e = (10,20,True,7.8,'s')
print(e) #(10, 20, True, 7.8, 's')

#allows indexing and slicing
print(e[1]) #20
print(e[1:3]) #(20, True)

#allows duplicates
e = (10,20,30,20,10)
print(e) #(10,20,30,20,10)

#add and multiple operations
print(e+e) #(10, 20, 30, 20, 10, 10, 20, 30, 20, 10)
print(e*2) #(10, 20, 30, 20, 10, 10, 20, 30, 20, 10)
print(e+2) #type error
print(e*e) #type error


#Set datatype: A group of elements in single entity
f = {}
print(type(f)) #dict type (empty curly brackets represent a dictionary)

f = {22,17,14,29}
print(type(f)) #set

#order is not preserved
print(f) #{22,17,14,29}

#it allows hetrogenius datatypes
f.add('S')
f.add(8.33)
f.add(False)
print(f) #{False, 8.33, 14, 17, 'S', 22, 29}

#doesn't allows indexing and slicing
print(f[2]) #error
print(f[:3]) #error

#doesn't allows duplicates
f.add(22)
f.add(14)
print(f) #{False, 8.33, 14, 17, 22, 'S', 29}

# sets are mutable
f.add(6) #{False, 6, 8.33, 14, 17, 'S', 22, 29}


#Frozenset datatype: similer to set datatype but immutable
g = {10,20,30,40}
h = frozenset(g)
h.add(10) #error


#Dictionary datatype : represent with key and value pairs as elements
i = {"name":"ravi", 'uid':1}
print(type(i)) #dict

#indexing not used in dictionary

#allows hetrogeniuselements
i = {"name":"ravi", 'uid':1, "passed": True}
print(i) #{'name': 'ravi', 'uid': 1, 'passed': True}

#keys are unique
i = {"name":"ravi", 'uid':1, "name":"vijay"}
print(i) #{'name': 'vijay', 'uid': 1}

#values can be duplicate
i = {"name":"ravi", 'uid':1, "other":"ravi"}
print(i) #{'name': 'ravi', 'uid': 1, 'other': 'ravi'}

#mutable
i['name']="ajay"
print(i) #{'name': 'ajay', 'uid': 1, 'other': 'ravi'}