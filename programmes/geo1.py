#traitement fichier geojson
#Sous licence GPL2
#By @germanlinux LaREM94
#syntaxe  python ./geo1.py <nom du fichier geojson issu de umap> <taux d abstention par bureau de vote>
#{'type': 'Feature', 'properties': {'_storage_options': {'showLabel': True, 'color': 'chocolate', 'iconClass': 'Drop'}, 'name': '6'}, 'geometry': {'type': 'Point', 'coordinates': [2.540030479431153, 48.83106574838852]}}
import sys
import re
import json

argv_filejson  =  sys.argv[1]
argv_fileABS   =  sys.argv[2]
with open(argv_fileABS,"r") as f:
    abs = f.readlines()
taux =[]
for item in abs:
     tab = item.split(';')
     index= int(tab[1])
     chaine = ': Abs ' + tab[2][:-1] + '%'
     taux.append(chaine)


data = json.load(open(argv_filejson))
#print('eg')
for item in data['features']:
    if '_storage_options' in item['properties']:
          if 'iconClass' in item['properties']['_storage_options']:
#               print(item['properties']['name'])
              index = int(item['properties']['name'])
              item['properties']['name'] += taux[index-1]
#               print(item['properties']['name'])

print(json.dumps(data))
