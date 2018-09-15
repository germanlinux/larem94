import ovh
import json
import sys
import random
import re
import smtplib
from email.mime.text import MIMEText
argv = sys.argv[1]
if len(sys.argv)== 3 :
    typemail = sys.argv[2]
else:
    typemail ='bf'


class Generatore:
    def  __init__(self,lg):
       self.lg = lg
       self.base = "abcdefghijkmnpqrstuvwxyz234567890ABCDEFGHJKLMNPQRSTUVWXYZ"
       self.passe = "".join(random.sample(self.base,self.lg ))
       while self.__invalid__():
          self.passe  = "".join(random.sample(self.base,self.lg ))
    def __invalid__(self):
       cp=0
       if re.search(r'[a-z]',self.passe):
           cp +=1
       if re.search(r'[A-Z]',self.passe):
           cp +=1
       if re.search(r'[0-9]',self.passe):
           cp +=1
       if cp != 3:
          return True
       else:
          return False

p = Generatore(9)
password = p.passe

with open(argv, "r") as f:
    lignes = f.readlines()


# create a client using configuration
client = ovh.Client(config_file='.ovh.conf')

# Request RO, /me API access
'''
ck = client.new_consumer_key_request()
ck.add_recursive_rules(ovh.API_READ_WRITE, "/email")
ck.add_rules(ovh.API_READ_ONLY, "/me")
# Request token
validation = ck.request()
'''
#print( f"Please visit {validation['validationUrl']} to authenticate")
#input("and press Enter to continue...")

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'])
#print(f"Btw, your 'consumerKey' is {validation['consumerKey']}")
result = client.get('/email/domain/enmarche94.fr/account')
print(json.dumps(result, indent=4))
### pour chacun mettre eq%mailcontact
#put zone description
server = smtplib.SMTP('SSL0.OVH.NET', 587)
server.starttls()
server.login("")



for ligne in lignes:
    ligne= ligne[:-1]
    p = Generatore(9)
    password = p.passe
    tab= ligne.split(';')
    email= tab[0]
    backup = tab[1]
    backup ='german.eric@gmail.com'
    msg = MIMEText(f'''     bonjour, \n

                    La boite mail de votre comité est disponible: {email}@enmarche94.fr \n
                    Le mot de passe est : {password}\n
                    La boite est consultable par un webmail  sur le lien https://mail.ovh.net/roundcube\n
                    Vous pouvez aussi l'utiliser  dans votre messagerie habituelle.\n
                    La documentation pour configurer vos supports: https://docs.ovh.com/fr/emails/generalites-sur-les-emails-mutualises/ \n
                    \n\n
                    Cordialement\n
                    Eric German: support  enmarche94''')
    msg['Subject']  =  "création de la boite mail de votre comité"
    msg['From']  ='Support Enmarche94 <support@enmarche94.fr>'
    msg['To']  ='german.eric@gmail.com'



    result = client.post(f"/email/domain/enmarche94.fr/account/",accountName =f"{email}",description=f"{typemail}%{backup}",password=f"{password}")
    print(json.dumps(result, indent=4))
    #print(f"{ligne};{password}")
    server.sendmail("support@enmarche94.fr", backup, msg.as_string())
server.quit()
