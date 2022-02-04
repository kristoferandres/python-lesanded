# ülesanne 2
# Kristofer Andres
# 31.01.2022
from math import *
import math

#kolmnurga ümbermööt
a = int(input("Sisesta kolmnurga külg a="))
b = int(input("Sisesta kolmnurga külg b="))
c = int(input("Sisesta kolmnurga külg c="))
P = a+b+c
print("Kolmnurga ümbermõõt:",  str(P)+"cm")

#toote hind
hind= 36.75
soodustus= hind*0.4
kogus = 3
kokku = (hind-soodustus)*kogus
print("Kolme toote hind kokku:", kokku,"€")

#pitsa
pitsahind = 12.90
jootraha = pitsahind*0.1
makse = (pitsahind+jootraha)/3
print("Iga üks peab maksma:", makse,"€")

#rulluisutajad
kiirus = 29.9
minutikiirus = kiirus*1000/3600
vahemaa = minutikiirus * 24
print("Vahemaa:", str(vahemaa)+"m")

#hypotenuus
a=16
b=9
c = sqrt(pow(a, 2)+pow(b, 2))
print("kolmas külg", str(c)+"cm")

#ajateisendus
aeg = int(input("sisesta aeg minutites"))
tunnid = math.floor(aeg/60)
minutid = aeg % 60
print("aeg:", tunnid, ":", minutid)

#arvsysteemid
a= int(input("sisesta kümnendarv"))
print(bin(a))
print(hex(a))

#kytusekulu
kütus = int(input("sisesta kütus liitrites:"))
km = int(input("sisesta kilomeetrid:"))
kulu= kütus*100/km
print('liitreid 100 kilomeetri peale:', kulu)


