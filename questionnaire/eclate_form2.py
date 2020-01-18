import sys
import re
import datetime as date

datetrt = date.date.today()
strdatetrt = datetrt.strftime("%Y%m%d")  
file = sys.argv[1]
tablepropre = []
dict_ville ={}
with open(file, 'r')  as f:
   table = f.readlines()
   #table= table[1:]
entete = table[0][:-1]
table = table[1:]   
for item in table:
    tab = item.split(';')
    ville = tab[1]
    if ville in dict_ville:
        dict_ville[ville].append(item)
    else:
        dict_ville[ville] = [item]
total = 0
for item in dict_ville.keys():
    print(item, len(dict_ville[item]))
    total += len(dict_ville[item])
print(total) 
with open("bilan.csv",'a+') as bilan:
    for item in dict_ville.keys():
        bilan.write(f"{item};{strdatetrt};{len(dict_ville[item])}\n")
    
for item in dict_ville.keys():
    with open(f"quest-{item.lower()}-{strdatetrt}.csv",'w') as sortie:
        sortie.write(entete + '\n')
        for ligne in dict_ville[item]:
            sortie.write(ligne)
