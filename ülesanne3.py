# ülesanne3
# Kristofer Andres
# 01.02.2022

#palindroom
s = input("sisesta sõna: ")
def isPalindrome(s):
    return s == s[::-1]
ans = isPalindrome(s)
 
if ans:
    print("Jah, on palindroom")
else:
    print("Ei ole palindroom")
    
#nimi
nimi = input("sisesta oma nimi: ")
nimi = nimi.strip()
nimi = nimi.capitalize()
print("tere,", nimi)

#vandumine
tekst = input("Kirjuta midagi: ")
tekst = tekst.replace ("kurat", "*****")
print(tekst)

#email
tekst = input("sisesta oma email: ")
if "@" in tekst:
    print("See on mail")
else:
    print("see ei ole mail")

#tundide ajad
algus = input("sisesta algus: ")
lõpp = input ("sisesta lõpp: ")

algus1, algus2 = algus.split(":")
lõpp1, lõpp2 = lõpp.split(":")
vastus = (int(lõpp1)*60+int(lõpp2))-(int(algus1)*60+int(algus2))
tund = vastus//60
minut = vastus%60
print(f"{tund}:{minut}")


