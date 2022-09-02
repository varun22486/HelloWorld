from typing import Type

import pandas as pd
import openpyxl as xl
df=pd.read_csv('pokemon_data.csv')
# df_xlsx=pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))
#df=pd.read_csv('pokemon_data.txt',delimiter='\t')
#Read columns
#print(df.columns)
#Read each COlumn
#print(df['Name'][0:5])
#Read each COlumn
#print(df[['Name','Type 1','HP']])

#print(df.iloc[2,2:5])
#print(df.loc[df['Type 1'] == "Grass"])
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head(3))
# for index, row in df.iterrows():
#     print(index,row[['Name','Type 1']])