a = "  Hello world!"
print(a.strip()) #Hello world!

b = "//Hi all//"
print(b.strip("/")) #Hi all

c = "  Welcome"
print(c.lstrip()) #Welcome

c1 = "??Welcome??"
print(c1.lstrip("?")) #Welcome??

d = "Welcome    "
print(d.rstrip()) #Welcome

d1 = "!!Welcome!!"
print(d1.rstrip("!")) #!!Welcome