# -*- coding: utf-8 -*-
"""Grp1 KJ Visual3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MHiiW9gsRwb7H5SmiivyUqVPyUbn1gOw
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

# reading csv files
pitdata = pd.read_csv('/content/drive/MyDrive/CSC302 Group Project/Data Set/pit_stops.csv')
crdata = pd.read_csv('/content/drive/MyDrive/CSC302 Group Project/Data Set/constructor_results.csv')
cdata = pd.read_csv('/content/drive/MyDrive/CSC302 Group Project/Data Set/constructors.csv')
  
# using merge function by setting how='outer'
vdf = pd.merge(pd.merge(pitdata, crdata, on='raceId', how='outer'),cdata,on='constructorId',how='outer')
vdf.head()

#limit the data to what is needed for the visual to improve performance
vdf = vdf[['duration','name']]
#vdf.head()

#limit the scope of the data to make visual easier to view
vdf['duration'] = pd.to_numeric(vdf['duration'], errors='coerce')
vdf = vdf.loc[vdf['duration'] < 30]

fig, ax = plt.subplots(figsize=(30, 15))
ax.set(xlabel='Formula 1 Constructor', 
       ylabel='Pit Stop Duration (in Seconds)', 
       title='Pit Stop Duration by Constructor')
ax.title.set_size(28)
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
plt.yticks(fontsize=16)
plt.xticks(fontsize=20, rotation=70)
sns.stripplot(data=vdf, x='name', y='duration', hue='duration', 
              jitter=.3, s=8, 
              palette=sns.color_palette("RdYlGn_r", as_cmap=True), 
              linewidth=1, edgecolor='black', legend=False)
sns.set(rc={'axes.facecolor':'white', 'figure.facecolor':'white'})