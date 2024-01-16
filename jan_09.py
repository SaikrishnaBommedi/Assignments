#Typecasting

#Int Type
a = "14421" #string
print(int(a)) #14421

b = 231.78 #float
print(int(b)) #231

c = True #Boolean
print(int(c)) #1

d = '121n'
print(int(d)) #error

#string
s = 5683 #Number
print(str(s)) #"5683"

p = 345.97 #float
print(str(p)) #"345.97"

q = True #bool
print(str(q)) #"True"


#Float
l = 'skrt'
print(float(l)) #error

m = 74
print(float(m)) #74.0

n = False
print(float(n)) #0.0

o = '7465d' #complex
print(float(o)) #error

#Slicing

ss = "Ravi goes to the gym and exercises three times a week"
print(ss[5:9]) #goes
print(ss[2:10:3]) #vgs
print(ss[-2:-6:-1]) #eew
print(ss[:4]) #Ravi
print(ss[-4:]) #week
print(ss[7:-14]) #es to the gym and exercises thre
print(ss[10:-10:2]) #t h y n xrie he i
print(ss[::-1]) #keew a semit eerht sesicrexe dna myg eht ot seog ivaR
print(ss[::2]) #Rv ost h y n xrie he ie  ek