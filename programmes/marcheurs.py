# traitement des pages adherents issu de la vue referent
#Sous licence GPL2
#By @germanlinux LaREM94
import sys
import re
class Marcheur:
  def __init__(self, id):
    self.id = id
    self.state ='CREE'
    self.comite = []
  def add(self,com):
    self.comite.append(com)
#argv_file= sys.argv[1]
argv_filecsv  =  sys.argv[1]
hash_marcheur= {}
hash_stat= [0,0,0,0,0,0,0,0,0,0,0,0]
with open(argv_filecsv,"r") as f:
    marcheurs = f.readlines()
marcheurs_list = marcheurs[1:]
marcheur = Marcheur(None)
total =0
marcheur.state = 'INIT'
for un_marcheur  in marcheurs_list:
    tab = un_marcheur[0:-1].split(';')
   # print(tab)
    debut = re.search(r"\d{7}",tab[0])
    if debut:
       if marcheur.state == 'CREE':
          total += 1
          print(marcheur.__dict__)
          hash_stat[len(marcheur.comite)] += 1
       marcheur = Marcheur(tab[0])
    fin = tab[-1]
    lib = re.search(r" \d\d:\d\d",fin)
    if lib:
     marcheur.add(tab[-2])
     #  marcheur.fin
    else:
     marcheur.add(tab[-1].replace('\"',''))
if marcheur.state == 'CREE':
          print(marcheur.__dict__)
          hash_stat[len(marcheur.comite)] += 1
          total += 1
print(hash_stat)
print(total)
