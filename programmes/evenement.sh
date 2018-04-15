# create table comites_03_2018  as select * from comites_02_2018;
python parsingmajeve.py comite94.csv    > evenement94.mix
grep 'INSERT' evenement94.mix  > evenement94.sql
python  injecteve.py  evenement94.sql
grep  -v 'INSERT' evenement94.mix|grep -v 'CAL'   > evenement94.csv
grep 'CAL' evenement94.mix  > evenement94.sics
python formatvcal.py evenement94.sics > evenement94.ics
python evecomplete.py


