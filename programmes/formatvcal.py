# parsing du fichier evenement recuperé avec l'API en marche
# à partir de la liste des commutes du 94 , vérifier l intitulé du comitev et l'URL
#Sous licence GPL2
#By @germanlinux LaREM94
import json
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
print("BEGIN:VCALENDAR")
print("VERSION:1.0")

for item in lignes:
   item = item[0:-1]
   tab= item.split(';')
   print('BEGIN:VEVENT')
   print('CATEGORIES:MEETING')
   mydate = tab[0]
   fordate = re.match(r"(\d\d\d\d)-(\d\d)-(\d\d)",mydate)
   stabledate = fordate[1] + fordate[2] + fordate[3]
   print("DTSTART:",stabledate)
   print("SUMMARY:",tab[1])
   print("DESCRIPTION:",tab[2])
   print("END:VEVENT")

print("END:VCALENDAR")
