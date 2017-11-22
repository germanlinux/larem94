# parsing du des infos du parisien
# pour preparartion fichier SQL  pour alimenter la table mesureth
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
#    del lignes[0]
hash_com ={}
ligne = lignes[0][0:-1]
tdata  =ligne.split('\\n')
print("code commune;nom;foyer;exoneration2017;exoneration2020;degrevement2020;taux actuel; taux 2020")
for item  in tdata:
    tabitem = item.split('\\t')
    numcommune = tabitem[0]
    code = str(tabitem[0][-2:])
    nom = tabitem[1]
    foyer =  int(tabitem[2])
    degrever_encours = int(tabitem[3])
    degrever_2020 =int(tabitem[4])
    total = int(tabitem[5])
    tauxa = float(tabitem[6].replace(',','.'))
    tauxb = float(tabitem[7].replace(',','.'))
    print("{};{};{};{};{};{};{};{}".format(code,nom,foyer,degrever_encours,degrever_2020,total,tauxa,tauxb))
#    insert = "INSERT INTO COMITES (id_comite,url) VALUES \
 #   ('{}', '{}');".format(id_comite,url)
#   print(insert)
#for t in hash_com:
#    print(t)


