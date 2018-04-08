import matplotlib.pyplot as plt
import pandas
from pandas.plotting import scatter_matrix
names = ['comite', 'janvier', 'fevrier', 'mars', 'progression', 'evenement', 'reunion']
data = pandas.read_csv('pourpanda2.csv',sep = ';', names=names)
df = data[['progression','evenement', 'reunion']]
scatter_matrix(df,figsize=(20,20), s= 1000)
plt.show()
