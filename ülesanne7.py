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
    
    def kuup():
        a = int(input('Sisesta kuubi külg: '))
        print()
        print(f'kuubi pindala: {a*a*a}')
        print()
    
    def kera():
        a = int(input('Sisesta kera diameeter: '))
        print()
        print(f'kera ruumala: {a*a*math.pi}')
        print()
        
    def koonus():
        a = int(input('Sisesta koonuse põhja raadius: '))
        b = int(input('Sisesta koonuse kõrgus: '))
        print()
        print(f'koonuse ruumala: {a*a*math.pi*(1/3)*b}')
        print()
        
    def silinder():
        a = int(input('Sisesta silindri põhja raadius: '))
        b = int(input('Sisesta silindri kõrgus: '))
        print()
        print(f'koonuse ruumala: {a*a*math.pi**b}')
        print()
        
        
    kujund()
    valik = int(input('Vali kujund: '))
    if valik==1:
        kuup()
    elif valik == 2:
        kera()
    elif valik == 3:
        koonus()
    elif valik == 4:
        silinder()
    else:
        i = 1

    