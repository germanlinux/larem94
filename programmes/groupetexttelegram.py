#groupetexttelegram.py
import sys
import re
argv_file= sys.argv[1]
with open(argv_file,"r") as f:
    lignes = f.readlines()
cp = len(lignes) - 1
while cp > 0:
    if re.match('online',lignes[cp]):
       print(lignes[cp-1][0:-1])
    if re.match('last',lignes[cp]):
       print(lignes[cp-1][0:-1])
    cp-=1
