# parsing du des comite et de leur identifiant larem
# pour preparartion fichier SQL  pour alimenter la table comite
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
argv_file= sys.argv[1]
from datetime import datetime
madate  = datetime.now()
strdate = madate.strftime("%Y-%m-%d")
with open(argv_file,"r") as f:
    lignes = f.readlines()
    #del lignes[0]
hash_com ={}
for lbrute in lignes:
    ligne = lbrute[0:-1]  # enlever le retour charriot
    tdetail = ligne.split(',')
    #libelle = tdetail[6].replace(chr(39),"''" )
    id_comite = tdetail[0]
    nom =  tdetail[2]
    insert = "INSERT INTO animateurs (nom, id_comite,datefrom ) VALUES \
    ({},{},'{}');".format(nom,id_comite,strdate)
    print(insert)
    #print(nom, len(id_comite))
#for t in hash_com:
#    print(t)


