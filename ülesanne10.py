# 03.03.2022
# Ülesanne 10
# Kristofer Andres

import re

fail = open('tekst.txt')
print("Ip aadressid: ")
for a in fail:
    aa= "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    if re.search(aa, a):
        print(a, end = "")
print("")
print("Sobilikud paroolid: ")
fail = open('tekst.txt')
for a in fail:
    if re.search('[a-z]', a):
        if re.search('[A-Z]', a):
            if re.search('[0-9]', a):
                print(a, end = "")
