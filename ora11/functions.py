import random
import math
print(chr(80),chr(121), chr(116), chr(104), chr(111), chr(110),sep="")
print(ord("p"))
print(ord("a"))
print(ord("a"))
print(ord(chr(80)))
print(float("3.5"))
print(type(float("3.5")))
print(int("12"))
print(int("12", base=16))
print(hex(18))
print(bin(18))
print(oct(18))
number=23.35452
print(number)
print(round(number))
print(round(number,2))
print(round(number,0))

print(float("5"))

a,b=2,4
if a==4 or b!=4:
    print("nyert")
if a==4 or b==4:
    print("majdnem nyert")

number=3
if number !=2:
    print("vesztett")
elif number==3:
    print("kis türelmet kérek")
else:
    print("nyert")

s=int(input("adja meg a sebességet! kmh/h"))
print("a megadott sebesség m/sben:",s*3.6)

list=[]
for i in range(10):
    n=random.randint(-1000,1000)
    list.append(n)
ps=[]
ptl=[]
for s in list:
    if s%2==0:
        ps.append(s)
    if s%2!=0:
        ptl.append(s)

print(list)
print(ps)
print(ptl)

l=int(input("Adja meg a háromszög egyik oldalát:"))
f=int(input("adja meg a háromszög mésodik oldalát:"))
t=int(input("adja meg a háromszög harmadik oldalát:"))
ker=l+f+t
d=(l+f+t)/2
kt=(d*(d-l)*(d-f)*(d-t))
ter=math.sqrt(kt)
print(ker,ter)

ertekek=[]
while len(ertekek)==0 or ertekek[-1]!="":
    ertekek.append(input("Adjon meg valamit"))
ertekek.remove("")
print(ertekek)

f=True
t=[]
while f:
    s=input("Adjon meg valamit:")
    if s!="":
        t.append(s)
    else:
        f=False
print(t)

list3=[]
for i in range(20):
    n = random.randint(-1000, 1000)
    list3.append(n)
maxi=list3[0]
mini=list3[0]
for elem in list3:
    if elem>maxi:
        maxi=elem
    if elem<mini:
        mini=elem
print(list3,maxi,mini)

nev=input("adja meg a nevét! ")
nem=input("adja meg a nemét! ")
if nem=="férfi" or nem=="Férfi":
    print(nev,"Úr")
elif nem=="nő" or nem=="Nő":
    print(nev, "Asszony")
else:
    print("Hibás adatot adott meg")