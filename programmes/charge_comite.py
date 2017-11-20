# parsing du des comite et de leur identifiant larem
# pour preparartion fichier SQL  pour alimenter la table comite
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
    del lignes[0]
hash_com ={}
for lbrute in lignes:
    ligne = lbrute[0:-1]  # enlever le retour charriot
    tdetail = ligne.split(';')
    #libelle = tdetail[6].replace(chr(39),"''" )
    id_comite = tdetail[2]
    url =  tdetail[0]
    insert = "INSERT INTO COMITES (id_comite,url) VALUES \
    ('{}', '{}');".format(id_comite,url)
    print(insert)
#for t in hash_com:
#    print(t)


