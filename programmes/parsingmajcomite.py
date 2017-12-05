# parsing du fichier commite recuperé avec l'API en marche
# à partir de la liste des commutes du 94 , vérifier l intitulé du comitev et l'URL
#Sous licence GPL2
#By @germanlinux LaREM94
import json
import sys
import re
argv_file= sys.argv[1]
argv_comite94 =  sys.argv[2]
hash_com ={}
with open(argv_file,"r") as f:
    lignes = f.readlines()
tab= json.loads(lignes[0] )
for a in tab:
    hash_com[a['uuid']] = a
with open(argv_comite94,"r",encoding='windows-1252') as f:
    comites = f.readlines()
for item in comites:
     item= item[0:-1]
     tabl = item.split(';')
     libelle = hash_com[tabl[1]]['url']
     lib = re.match(r"\/comites\/(.+)",libelle)
     nom = lib[1]
     tabl[0] = tabl[0].replace("'","")
     if tabl[0] != nom:
         print("{} --> {}".format(tabl[0],nom))




