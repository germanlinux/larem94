# parsing du fichier des comites de la vue referent
# a partir de la liste des commutes du 94 , verifier l intitule du comitev et l'URL
#Sous licence GPL2
#By @germanlinux LaREM94
import json
import sys
import re
#import requests
#argv_file= sys.argv[1]
def helper_nom2url(nom):
     url = nom.lower()
     url= url.replace(" - ","-")
     url= url.replace(" !","")
     url= url.replace("!","")
     url= url.replace("  "," ")
     url= url.replace(" ","-")
     url= url.replace("é","e")
     url= url.replace("è","e")
     url= url.replace("ê","e")
     url= url.replace("à","a")
     url= url.replace("'","-")
     url= url.replace("(","")
     url= url.replace(")","")
     url= url.replace("/","-")
     url= url.replace("#","")
     return(url)

argv_comite94 =  sys.argv[1]
with open(argv_comite94,"r") as f:
    comites = f.readlines()

for item in comites:
     item= item[0:-1]
     tabl = item.split(';')
     nom = tabl[1]
     url = helper_nom2url(nom)
     print(url)
