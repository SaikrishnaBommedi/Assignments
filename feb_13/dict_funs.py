#update 
d = {1:"raj", 2:"ganesh"}
d[1] = 'ravi'
print(d)

#delete
d = {1:"raj", 2:"ganesh"}
del d[2]
print(d)

#clear
d = {1:"raj", 2:"ganesh"}
d.clear()
print(d)

#imp fun /methods of dict
a = [(100,"vijay"),(200,"srinu")] #list
b = ((10,"ram"),(20,"ravi")) #tuple
d1 = dict(a)
d2 = dict(b)
print(d1)
print(d2)

#length
d = {1:"raj", 2:"ganesh"}
print(len(d))

#get 
d = {1:"raj", 2:"ganesh"}
print(d.get(2))
print(d.get(3)) #None
#print(d[3]) #Key Error

#pop
d = {1:"raj", 2:"ganesh"}
#print(d.pop()) #Type Error
print(d.pop(1)) #raj

#popitem
d = {1:"raj", 2:"ganesh"}
print(d.popitem()) #(2, 'ganesh')

#keys
d = {1:"raj", 2:"ganesh"}
print(d.keys()) #dict_keys([1, 2])

#Vals
print(d.values()) #dict_values(['raj', 'ganesh'])

#items
print(d.items()) #dict_items([(1, 'raj'), (2, 'ganesh')])

#copy()
d = {1:"raj", 2:"ganesh"}
d2 = d.copy()
print(d2)

#setdefualt
d.setdefault(1,"ravi")
print(d[1]) #raj
d.setdefault(3,"ajay")
print(d[3]) #ajay

#update()
d = {1:"raj", 2:"ganesh"}
d1 = {3:"ajay", 4:"vijay"}
d.update(d1)
print(d)