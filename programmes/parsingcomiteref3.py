# parsing du fichier des comites de la vue referent
# a partir de la liste des commutes du 94 , verifier l intitule du comitev et l'URL
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
#import re
import psycopg2
#import requests
#argv_file= sys.argv[1]
def helper_nom2url(nom):
     url = nom.lower()
     url= url.replace(" / ","-")
     url= url.replace(" - ","-")
     url= url.replace(" -","-")
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
     url= url.replace(")","")

     url= url.replace("/","-")
     url= url.replace("#","")
     return(url)
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='172.17.0.2' ")
cur_sel = conn.cursor()
argv_comite94 =  sys.argv[1]
with open(argv_comite94,"r") as f:
    comites = f.readlines()

for item in comites:
     item= item[0:-1]
     tabl = item.split(';')
     nom = tabl[0]
     #url = helper_nom2url(nom)
     #print(url)
     #chaine = "SELECT * from comites_09_2018 where url='{}'".format(nom)
     #cur_sel.execute(chaine)
     #if cur_sel.rowcount == 0:
     #     print("{} : {} not found ".format(nom,url))
     #else:
     chaine = f"update comites_10_2018 set adherents = {tabl[2]}   where id_comite='{nom}'"
     cur_sel.execute(chaine)
     conn.commit()

