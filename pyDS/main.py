import pandas
import matplotlib.pyplot as plt
df = pandas.read_csv('C:/projects/CL_Cup/pos_general.csv')
df.to_csv('./pos_general.csv')

print(df.groupby('payment')['pos_sales_net'].mean())      #среднее значение по карте и по наличным



count_pg = df['units_on_hand'].notna().sum()
count_compet = df['units_on_hand'].isna().sum()

data = [count_pg, count_compet]
comp = ['P&G', 'Competitors']

plt.pie(data, labels=comp)       #competitors
plt.show()

df['pos_sales_qty'].plot(kind='hist')
plt.show()                                  #purcases_amount
