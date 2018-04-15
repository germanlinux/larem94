#Sous licence GPL2
#By @germanlinux LaREM94
import requests
import psycopg2
from bs4 import BeautifulSoup
import sys
import re
conn = psycopg2.connect("dbname='larem94' user='postgres'   password ='pass' host ='172.17.0.2' ")
cur_sel = conn.cursor()
chaine = "SELECT * from evenements where slug is not Null;"
cur_sel.execute(chaine)
for eve in cur_sel:
    slug = eve[5]
    if eve[6] == 'C':
         continue
    r = requests.get('https://en-marche.fr/evenements/' + slug)
    content_page=r.content
    soup = BeautifulSoup(content_page,'html.parser')
    adresse = soup.find_all("span","committee-event-address")
    str_adresse= adresse[0].text
    dateenclair = soup.find_all("span","committee-event-date")
    str_dateenclair= dateenclair[0].text
    nb = soup.find_all("div","text--body text--white icon--with-text l__row--center b__nudge--top-10 committee-event-attendees")
    #nbx = nb[0].text.split('\n')
    nbst = nb[0].text
    nbinsc = re.search(r"\d+",nbst)
    nb = int(nbinsc[0])
    clot = soup.find_all("div","text--body text--white")
    est_clos = 'V'
    for item in clot:
         if re.search(r'(est termin)',item.text):
             est_clos = 'C'
    chaine = "UPDATE evenements  set dateenclair = '{}' , adresse = '{}', nombre = {}, statut = '{}' where id_evenement = '{}' ;".format(str_dateenclair,str_dateenclair, nb, est_clos,eve[0])
    print(chaine)
    cur_up = conn.cursor()
    cur_up.execute(chaine)
    conn.commit()

  #  <span class="committee-event-address">
   # acceder evenement
   #  recuperer l heure et le lieu, nb inscrits
   #  le passer statut à N
