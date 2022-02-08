# ülesanne 4
# Kristofer Andres
# 03.02.2022

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
a= 5
for rida in range(0,a):
    a=a-1
    for veerg in range(0,5):
            print('* ', end=' ')
    print()