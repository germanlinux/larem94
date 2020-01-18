# coding: utf-8
def _datebrute(date):
    strd = date[-4:] + date[3:4] + date[:1]
    return strd 

def _recherche(table,comite, date):
    nb = 0
    for ligne in table:
        titem = ligne.split(';')
        if titem[1] == date and titem[0] == comite:
              nb = int(titem[2][:-1])
    return nb
synthese={}
entreedate = set()
entrecomite = set()
with open("bilan.csv",'r') as bilan:
     table = bilan.readlines()
# pour chaque ligne
# lire la date et l' ajouter au set
# lire le comite et l ajouter au set
for ligne in table:
    titem = ligne.split(';')
    entreedate.add(titem[1])
    entrecomite.add(titem[0])

# puis 
# generer entete
ligne = ';' 
ldat = list(entreedate)
ldat.sort()
for dt in ldat:
      fdt = dt[-2:] + '/' + dt[4:6] + '/' + dt[:4]
      ligne += fdt + ";"
print(f"commune{ligne}")


# pour chaque comite
for comm in entrecomite:
    ligne = f"{comm};"
    for dat in ldat:
        # rechercher dans le bilan le commite et la date
        nombre = _recherche(table, comm,dat )
        ligne+= str(nombre) + ";"
    print(ligne)   
# pour chaque date

# recherche dans table
# si trouve prendre total sinon 0
# generer un csv

