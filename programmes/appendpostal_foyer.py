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
    del lignes[1]
    del lignes[0]

for lbrute in lignes:
    ligne = lbrute[0:-1]  # enlever le retour charriot
    tdetail = ligne.split(';')
    code_commune = int(tdetail[1])
    postal = int(tdetail[6])
    foyer = int(tdetail[7])

    update = "UPDATE  COMMUNES SET code_postal= {} , nb_foyer_fiscaux = {} WHERE code_commune= {};".format( postal,foyer,code_commune)
    print(update)
