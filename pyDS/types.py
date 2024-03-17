import pandas
import matplotlib.pyplot as plt

dl = pandas.read_csv('C:/projects/CL_Cup/prod_dim.csv')
dl.to_csv('./prod_dim.csv')

plt.pie(dl['prod_type'].value_counts(), labels=dl['prod_type'].unique())
plt.show()