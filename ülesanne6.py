# ülesanne 6
# Kristofer Andres
# 15.02.2022
RE = 0
KESK = 0
osad = []
with open('asd.txt', 'r') as minu_fail:
    for rida in minu_fail:
        enimi,pnimi, osa, valimisi =rida.split(" ")
        print(f'{enimi:11}{pnimi:11}{osa:4}{valimisi:5}')
        if osa=='RE':
            RE = RE +1
        elif osa=='KE':
            KESK = KESK +1
        if osa not in osad:
            osad.append(osa)
            
print(f'reformierakonnast: {RE}')
print(f'keskerakonnast: {KESK}')
print(f'erinevaid osakonde: {len(osad)}')
with open('asdasd.txt', 'w') as minu_fail:
     for nr in range(1,100):
         fail_kirjutamiseks.write(str()+'\n')