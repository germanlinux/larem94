import sys
#import re
import psycopg2
#import requests
#argv_file= sys.argv[1]

class Comite:
    def __init__(self, id, nom, adherents_a):
        self.id = id
        self.nom =  nom
        self.adhA = adherents_a
    def add_b(self, adherents_b):
        self.adhB = adherents_b
    def add_c(self, adherents_c):
        self.adhC = adherents_c
    def add_ev(self, nb):
        self.Ev = nb
    def add_evr(self, nb):
        self.Evr = nb
    def  vide(self):
          if  self.adhA is None:
               self.adhA ='0'

          if  self.adhB is None:
               self.adhB ='0'
          if self.adhC  is None:
               self.adhC ='0'
          accrois = self.adhC - self.adhA
          if self.adhA == 0:
            i_accrois = 0
          else:
            i_accrois = int (round(accrois /   self.adhA * 100))
          print("{};{};{};{};{};{};{}".format(self.nom, self.adhA, self.adhB, self.adhC,i_accrois, self.Ev,self.Evr))


dico_comite = {}
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='172.17.0.2' ")
cur_sel = conn.cursor()
argv_comite94 =  sys.argv[1]
with open(argv_comite94,"r") as f:
    comites = f.readlines()

for item in comites:
     item= item[0:-1]
     tabl = item.split(';')
     nom = tabl[1]
     id_comite = tabl[0]
     #print("eric", item)
     #print(url)
     # mois A
     chaine = "SELECT * from comites_01_2018  where id_comite ='{}'".format(id_comite)
     cur_sel.execute(chaine)
     if cur_sel.rowcount == 0:
          #print("{}  not found ".format(nom))
          com = Comite(id_comite,nom,0)
     else:
          for ligne in cur_sel:
            adherents = ligne[2]
          com = Comite(id_comite,nom,adherents)
          dico_comite[id] = com
     # mois B
     chaine = "SELECT * from comites_02_2018  where id_comite ='{}'".format(id_comite)
     cur_sel.execute(chaine)
     if cur_sel.rowcount == 0:
          print("{} : {} not found mois2 ".format(nom))
     else:
        for ligne in cur_sel:
            adherents = ligne[2]
        com.add_b(adherents)
     chaine = "SELECT * from comites_03_2018  where id_comite ='{}'".format(id_comite)
     cur_sel.execute(chaine)
     if cur_sel.rowcount == 0:
          print("{} : {} not found mois3 ".format(nom))
     else:
        for ligne in cur_sel:
            adherents = ligne[2]
        com.add_c(adherents)

     chaine = "SELECT count(*) from evetrim1  where id_comite ='{}' ".format(id_comite)
     cur_sel.execute(chaine)
     eve =0
     if cur_sel.rowcount != 0:
       for ligne in cur_sel:
         eve = ligne[0]
         com.add_ev(eve)
     chaine = "SELECT count(*) from evetrim1  where id_comite ='{}' and type ='R' ".format(id_comite)
     cur_sel.execute(chaine)
     ever =0
     if cur_sel.rowcount != 0:
       for ligne in cur_sel:
         ever = ligne[0]
         com.add_evr(ever)
     com.vide()

