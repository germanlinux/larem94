# parsing du fichier mint  commune resultat election 2017
# pour preparartion fichier SQL  pour complter la table commune
# l insee attribue un code commune qui est repris dans d autres opendata.
# ce code servira d identifiant.
#import psycopg2
#conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='192.168.99.100' ")
#cur_sel = conn.cursor()
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
for lbrute in lignes:
    ligne = lbrute[0:-1]  # enlever le retour charriot
    tdetail = ligne.split(',')
    code_commune = int(tdetail[2])
    str_inscrit= tdetail[4]
    inscrit = int(str_inscrit)
    update = "UPDATE  COMMUNES SET inscrits= {}  WHERE code_commune= {};".format(inscrit,code_commune)
    print(update)
