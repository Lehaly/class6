import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('housing.data',
                 sep='\s+',
                 header=None)

os.makedirs('plots', exist_ok=True)

df.columns = ['CRIME', 'ZN', 'INDUS', 'CHASRIVER', 'NOX', 'ROOM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'BLK', 'LSTAT', 'MEDV']


# Histogram
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.hist(df['MEDV'], bins=30, color='g', label='MEDV')
axes.set_title('Median price')
axes.set_xlabel('Price')
axes.set_ylabel('Mean Simmetry')
axes.legend()
plt.savefig('plots/boston_mean_simmetry_hist.png', dpi=300)

# Pie
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.pie(df['CRIME'].value_counts(), labels=df['CRIME'].value_counts().index.tolist())
axes.set_title('Crime rate')
axes.legend()
plt.savefig('plots/crime_rate_pie.png', dpi=300)

# Bar
fig, axes = plt.subplots(1, 1, figsize=(5, 5))
axes.bar(np.arange(0, len(df['INDUS'])), df['INDUS'], color='y', label='mean symmetry')
axes.set_title('Industry')
axes.set_xlabel('Index')
axes.set_ylabel('Industry rate')
axes.legend()
plt.savefig('plots/industry_mean_simmetry_bar.png', dpi=300)

# Correlation Heatmap
fig, axes = plt.subplots(1, 1, figsize=(20, 20))
df['ROOM']=df['MEDV'].map({'B': 0, 'M': 1})
correlation = df.corr().round(2)
im = axes.imshow(correlation)
cbar = axes.figure.colorbar(im, ax=axes)
cbar.ax.set_ylabel('Correlation', rotation=-90, va="bottom")
numrows = len(correlation.iloc[0])
numcolumns = len(correlation.columns)
axes.set_xticks(np.arange(numrows))
axes.set_yticks(np.arange(numcolumns))
axes.set_xticklabels(correlation.columns)
axes.set_yticklabels(correlation.columns)
plt.setp(axes.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
for i in range(numrows):
    for j in range(numcolumns):
        text = axes.text(j, i, correlation.iloc[i, j], ha='center', va='center', color='w')
axes.set_title('Density')
fig.tight_layout()
plt.savefig('plots/density_heatmap.png')


plt.close()
