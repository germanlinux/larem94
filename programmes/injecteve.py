#Sous licence GPL2
#By @germanlinux LaREM94
import psycopg2
import sys
import re
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='172.17.0.2' ")
cur_sel = conn.cursor()
argv_eve =  sys.argv[1]
with open(argv_eve,"r") as f:
    eves = f.readlines()
for ev in eves :
    ev= ev[0:-1]
    tabma =re.search(r'VALUES \((.+?), ' , ev)
    if tabma:
        chaine = "SELECT * from evenements where id_evenement={}".format(tabma[1])
        cur_sel.execute(chaine)
        if cur_sel.rowcount == 0:
           print(ev)
           chaine= ev
           cur_sel.execute(chaine)
conn.commit()
