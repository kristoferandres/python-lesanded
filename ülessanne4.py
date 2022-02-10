# ülesanne 4
# Kristofer Andres
# 03.02.2022
import random

#ruut
a= int(input("Sisesta esimene külg: "))
b= int(input("Sisesta teine külg: "))

if a==b:
    print('See on ruut')
else:
    print('see on ristkülik')

#tehted
a= int(input("Sisesta esimene arv: "))
b= int(input("Sisesta teine arv: "))
c= input("Sisesta tehte märk: ")

if c=="+":
    d= a + b
elif c=="-":
    d= a - b
elif c=="*":
    d= a * b
else:
    d= a / b
print(f"{a}{c}{b}={d}")

#juubel
aeg= input("Sisesta sünniaeg formaadis dd.mm.yyyy: ")
p, k, a= aeg.split(".")
vanus = 2022 - int(a)
if vanus%5 == 0:
    print("on juubel")
else:
    print("ei ole juubel")
    
#hind
hind= int(input("Sisesta hind: "))
if hind > 10:
    hind= hind +hind*0.2
else:
    hind= hind +hind*0.1
print(hind, "€")

#meeskond
a= input("Sisesta sugu: ")
if a == "m": 
    b= int(input("Sisesta vanus: "))
    if b >= 16 and b<= 18:
        print('sobib')
    else:
        print('ei sobi')
else: 
    print('ei sobi')

for rida in range(0,5):
    for veerg in range(0,5):
        print('* ', end=' ')
    print()
print()
print()
a= 0
for rida in range(0,5):
    a=a+1
    for veerg in range(0,a):
            print('* ', end=' ')
    print()
print()
print()
a=6
print()
for rida in range(0,5):
    a=a-1
    for veerg in range(0,a):
            print('* ', end=' ')
    print()
print()
for a in range(0,5):
    print(random.randint(1,9), end='')

for number in range(0,100):
    if number%2==0:
        print('paaris')
    else:
        print('paaritu')
print()

#viisikud
for a in range(0,10):
    print(f'{a} x 5 = ', a*5)
    
for a in range(0,100):
    if a%5==0:
        print(f'{a}')
        
kordus=1
while kordus == 1:
    arv = random.randint(1,30)
    katseid= 3
    for a in range(1,4):
        arvamus = int(input(f"Arva arv vahemikus 1-30, katseid jäänud {katseid}: "))
        katseid-=1
        if arvamus == arv:
            print (f'arvasid ära {a} korraga.')
            break
    print(f'arv oli {arv}')
    valik = input('kas tahad uuesti proovida? (jah, ei)')
    if valik == 'ei':
        kordus = 0
        
aastad = 5
summa = 10000
intress =0.05
print(f'{"aasta ":4}  {"algsumma ":6}  {"juurde ":8}  {"lõppsumma":10}')
for aastad in range(1,aastad+1):
    intressjuurde = summa *intress
    lõppsumma = summa + intressjuurde
    print(f'{aastad:4}  {summa:6}  {intressjuurde:8}  {lõppsumma:10}')
    summa = summa + intressjuurde
print()
 
print(f'{"arv":4} {"ruut":6} {"kuup":8}')
for arv in range(1,11):
    print(f'{arv:4} {arv**2:6} {arv**3:8}')
    



        


