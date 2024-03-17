import pandas
import openpyxl
import matplotlib.pyplot as plt

df = pandas.read_csv("CL_Cup IT 2024_P&G_datasets/pos_general.csv")
mdf = pandas.read_csv("CL_Cup IT 2024_P&G_datasets/prod_dim.csv")
#print(df.info())
df = df.merge(mdf, left_on=['prod_key'], right_on=['EAN'], how='left')
#print(df.info())
df.sort_values(by=['period_end_date', 'prod_type', 'pos_sales_qty'])
print(df.groupby(['period_end_date', 'prod_type'])['pos_sales_qty'].max().to_string())
df['period_end_date'] = df['period_end_date'].apply(lambda x: x[11:13])
#print(df[['period_end_date', 'pos_sales_qty', 'prod_type']].head(20))
print(df.groupby(['period_end_date', 'prod_type'])['pos_sales_qty'].max().to_string())
file_name="most_sold_items_hours.xlsx"
df.groupby(['period_end_date', 'prod_type'])['pos_sales_qty'].max().to_excel(file_name)
