#Sous licence GPL2
#By @germanlinux LaREM94
import psycopg2
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='192.168.99.100' ")
cur_sel = conn.cursor()
cur_sel.execute("SELECT * FROM communes ORDER BY libelle;")
print("'Commune';'numero';'arrondissement;'canton';population;inscrits")
for ligne in cur_sel:
    print("'{}';{};{};{};{};{}".format(ligne[1],ligne[0],ligne[2],ligne[3],ligne[4],ligne[5] ))
