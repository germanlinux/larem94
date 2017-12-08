#Sous licence GPL2
#By @germanlinux LaREM94
#select * from comites_ref left join  comites on comites.id_comite = comites_ref.id_comite where comites.id_comite is null;

import psycopg2
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='192.168.99.100' ")
cur_sel = conn.cursor()
cur_sel.execute("SELECT id_comite, url FROM comites;")
for ligne in cur_sel:
    print("'{}';{}".format(ligne[1],ligne[0] ))
