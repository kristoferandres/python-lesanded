# ülesanne 5
# Kristofer Andres
# 10.02.2022



#nimede lisamine loendisse
sisesta = input('Sisesta viis nime: ')
nimed = sisesta.split(", ")
nimed.sort()
for a in range(len(nimed)):
    print (nimed[a])
    
print()
    

#nimed loendist
nimed = ['Juhan','Kati','Maarja','Mario','Mati']
for a in range(len(nimed)):
    print(f'{a+1}. {nimed[a]}')
valik= int(input("sisesta muudetava number: "))
uus= input("sisesta uus nimi: ")
nimed[valik-1] = uus
print(nimed)


