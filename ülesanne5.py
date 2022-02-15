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

print()

#duplikaadid
nimed = ['juhan','kati','mario','mario','mati','mati']
prinditud = []
for a in range(len(nimed)):
    
    if nimed[a] not in prinditud:
        prinditud.append(nimed[a])
for a in range(len(prinditud)):
    print(f'{prinditud[a]}')
    
print()
    
#vanused
kogusumma = 0
vanused = ['12','15','64','13']
vanused.sort()
print(f'suurim arv: {vanused[-1]}')
print(f'väikseim arv: {vanused[0]}')
for a in range(len(vanused)):
    kogusumma += int(vanused[a])
print(f'kogusumma: {kogusumma}')
print(f'keskmine: {kogusumma/len(vanused)}')

print()

#tärnid
numbrid = ['6','2','3','4','5']
for a in range(len(numbrid)):
    print()
    for b in range (0,int(numbrid[a])):
        print('*', end = '')