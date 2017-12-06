# parsing du fichier evenement recuperé avec l'API en marche
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
with open(argv_comite94,"r",encoding='windows-1252') as f:
    comites = f.readlines()
for item in comites:
     item= item[0:-1]
     tabl = item.split(';')
     tabl[0] = tabl[0].replace("'","")
     hash_com[tabl[0]] = 0
#print(hash_com)
for a in tab:
     #print(a)
     if 'committee_url' in a:
         comite= a['committee_url']
         lib = re.match(r"\/comites\/(.+)",comite)
         nom = lib[1]
         if nom in hash_com:
            mydate = a['slug'][0:10]
            motif  = a['name']
            hash_com[nom] += 1
            print("{};{};{}".format(mydate,nom,motif))
#for item in hash_com:
#    if hash_com[item] > 0:
#         print("{} --> {}".format(item,hash_com[item]))
