#Sous licence GPL2
#By @germanlinux LaREM94
import requests
from bs4 import BeautifulSoup
import re
import sys
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
#    del lignes[0]
for ligne in lignes:
    ligne= ligne[:-1]
    affiche = ligne
    r = requests.get('https://en-marche.fr/comites/' + ligne)
    code = r.status_code
    content_page=r.content
    soup = BeautifulSoup(content_page,'html.parser')
    animateurs= soup.find_all("li", "committee-host text--body text--bold")
    for anim in animateurs:
         st = anim.get_text().split('\n')
         for lignea in st:
            if len(lignea.lstrip())> 0:
                if not re.search(r'(Contact)',lignea):
                    print("{};{}".format(lignea.lstrip(),affiche))




