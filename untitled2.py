# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lQBKBOkmKQpCniB9t1nLY2l7d3kA6qvi
"""

import pandas as pd
df=pd.DataFrame ( { 'Ism': [ 'Hurixon','Moxichehra','Mushtariybonu','Madina','Bibifotima','Oybek','Nurmuhammad','Muhammadaziz','Humoyunmirzo'],
   'Familiya':['Joraboyeva', 'Yusupaliyeva','Qadamova','Amakihonova','Joraboyeva','Akramov','Jumanazorov','Rozaliyev','Dehqonov'],
    'Yoshi':['19','20','21','19','19','19','19','19','19'],
    'Kursi':['2','2','2','2','2','2','2','2','2']})
print(df)

df.to_excel('hurixon.xlsx', index=False, sheet_name='Sheet1')
