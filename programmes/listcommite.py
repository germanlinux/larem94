# parsing du fichier insee  commune population
# pour preparartion fichier SQL  pour alimenter la table commune
# l insee attribue un code commune qui est repris dans d autres opendata.
# ce code servira d identifiant.
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
    code_commune = int(tdetail[1])
    for i in range(2,5):
        if tdetail[i] :
          hash_com[tdetail[i]]  = 1

    #insert = "INSERT INTO COMMUNES (code_commune, libelle, arrondissement, canton, population) VALUES \
    #({}, '{}', {}, {}, {});".format(code_commune, libelle, arrondissement, canton, population)
    #print(insert)
for t in hash_com:
    print(t)


