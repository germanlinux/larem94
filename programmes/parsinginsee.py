# parsing du fichier insee  commune population
# pour preparartion fichier SQL  pour alimenter la table commune
# l insee attribue un code commune qui est repris dans d autres opendata.
# ce code servira d identifiant.
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r",encoding='windows-1252') as f:
    lignes = f.readlines()
for lbrute in lignes:
    ligne = lbrute[0:-1]  # enlever le retour charriot
    tdetail = ligne.split(';')
    libelle = tdetail[6].replace(chr(39),"''" )
    libelle =libelle.replace("' ","'")

    code_commune = int(tdetail[5])
    canton = int(tdetail[4])
    arrondissement= int(tdetail[3])
    str_population= tdetail[-1]
    population = int(str_population.replace(chr(160),''))
    insert = "INSERT INTO COMMUNES (code_commune, libelle, arrondissement, canton, population) VALUES \
    ({}, '{}', {}, {}, {});".format(code_commune, libelle, arrondissement, canton, population)
    print(insert)

