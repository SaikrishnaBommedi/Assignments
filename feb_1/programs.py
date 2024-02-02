s = "Hello World!"
print(s.upper()) #HELLO WORLD!
print(s.lower()) #hello world!

s = "hello world"
print(s.capitalize()) #Hello world
print(s.title()) #Hello World
print(s.swapcase()) #HELLO WORLD

s = "HELLO WORLD"
print(s.swapcase()) #hello world

s = "hiall"
p = "Hi1223"
q = "Welcome 10"
r = "HI ALL"
print(s.isalnum()) #True
print(p.isalnum()) #True
print(q.isalnum()) #False
print(r.isalnum()) #False

print(s.isalpha()) #True
print(p.isalpha()) #False
print(q.isalpha()) #False
print(r.isalpha()) #False

t = "17069"
print(s.isdigit()) #False
print(p.isdigit()) #False
print(q.isdigit()) #False
print(r.isdigit()) #False
print(t.isdigit()) #True

print(s.islower()) #True
print(r.islower()) #False

print(s.isupper()) #False
print(r.isupper()) #True

s = "Hi all"
p = " Hi all "
q = " "
r = "  "
print(s.isspace()) #False
print(p.isspace()) #False
print(q.isspace()) #False
print(r.isspace()) #False