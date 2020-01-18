import sys
import re
file = sys.argv[1]
tablepropre = []
with open(file, 'r')  as f:
   table = f.readlines()
   entete = table[0][:-1]
   table= table[1:]
for ligne in table:
    ligne = ligne[:-1]
    tab = ligne.split(';')
    #print(tab[1]) 
    if re.match(r'\d\d?\/', tab[0]):
  #      print('ok',tab[0])
        tablepropre.append(tab)
    else: 
        tablepropre[-1] += tab    
#print(tablepropre)
print(entete)
for ligne in tablepropre:
    print(';'.join(ligne))

      