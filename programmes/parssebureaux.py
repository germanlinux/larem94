# traitement des resultats election par commune , bureau de vote
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
from decimal import *
argv_filecsv  =  sys.argv[1]
with open(argv_filecsv,"r",encoding='windows-1252') as f:
    bureaux = f.readlines()
hash_ville={}
hash_ville_cp = {}
for un_bureau in bureaux:
  tab_bureaux = un_bureau.split(';')
  print("{};{};{}".format(tab_bureaux[5],tab_bureaux[6],tab_bureaux[9]))
  if tab_bureaux[5] in hash_ville:
    hash_ville[tab_bureaux[5]] += Decimal(tab_bureaux[9].replace(',','.'))
    hash_ville_cp[tab_bureaux[5]] += 1
  else:
    hash_ville[tab_bureaux[5]] =  Decimal(tab_bureaux[9].replace(',','.'))
    hash_ville_cp[tab_bureaux[5]] = 1

for stat in hash_ville_cp:
   moy = hash_ville[stat] / hash_ville_cp[stat]
   print("{};{}".format(stat,round(moy,2)))
