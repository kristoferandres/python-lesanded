# ülesanne 7
# Kristofer Andres
# 16.02.2022

import math

def tervitus(keel="ge"):
    nimi = input("sisesta oma nimi: ")
    keel = input("sisesta keel (pole vajalik):")
    if keel == "et":
        print(f'{nimi}, tere')
    elif keel == "en":
        print(f'{nimi}, hello')
    else:
        print(f'{nimi}, hallo')

i= 0
while i == 0 :
    def kujund():
        print("VALI KUJUND")
        print('1 kuup')
        print('2 kera')
        print('3 koonus')
        print('4 silinder')
    
    def kuup(a):
        v=a**3
        return v
    def kera(a):
        v=(4*math.pi*a**3)/3
        return v
    def koonus(a,b):
        v=(math.pi*a**2*b)/3
        return v         
    def silinder(a,b):
        v=math.pi*a**2*b
        return v 
            
        
        
    kujund()
    valik = int(input('Vali kujund: '))
    if valik==1:
        print()
        a = int(input('Sisesta kuubi külg: '))
        print(kuup(a))
        print()
          
        
    elif valik == 2:
        a = int(input('Sisesta kera raadius: '))
        print()
        print(kera(a))
        print()
    elif valik == 3:
        a = int(input('Sisesta koonuse põhja raadius: '))
        b = int(input('Sisesta koonuse kõrgus: '))
        print()
        print(koonus(a,b))
        print()
    elif valik == 4:
        a = int(input('Sisesta silindri põhja raadius: '))
        b = int(input('Sisesta silindri kõrgus: '))
        print()
        print(silinder(a,b))
        print()
    else:
        i = 1

    