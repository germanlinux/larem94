#Sous licence GPL2
#By @germanlinux LaREM94
import requests
from bs4 import BeautifulSoup
import re
import sys
argv_fic = sys.argv[1]

with open(argv_fic,"r") as f:
    lignes = f.readlines()
    content_page= ''.join(lignes)

soup = BeautifulSoup(content_page,'html.parser')
mails = soup.find_all(class_= 'T10')
for mail in mails:
    texte = mail.text
    lig = texte.split('\n')
    print(lig[0])
    #print('eg')
#print('eg')
