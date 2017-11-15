#Sous licence GPL2
#By @germanlinux LaREM94
import requests
import re
import sys
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
#    del lignes[0]
for ligne in lignes:
    ligne= ligne[:-1]
    r = requests.get('https://en-marche.fr/comites/' + ligne)
    code = r.status_code
    page=r.text
    nb =re.search(r'>(\d+) adh',page)
    print("{};{}".format(ligne,nb.group(1)))

