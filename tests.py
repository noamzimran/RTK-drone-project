
 # used to handle data
import pandas as pd

# used to handle gcp data

import geopandas as gpd

# used for manipulating directory paths
import os

# Scientific and vector computation for python
import numpy as np
from scipy.interpolate import griddata

# Plotting library
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cbook
from matplotlib.colors import LightSource
import seaborn as sns


import folium



rms1 = pd.read_csv(r'data\points_errors_No_GCP_acc.csv')

# Create rms1 GoeDataFrame
points2 = gpd.points_from_xy(x=rms1.x, y=rms1.y)
rms1['geometry'] = points2
rms1 = gpd.GeoDataFrame(rms1, geometry='geometry', crs="EPSG:2039")
#%%
# calculate total error
for i, row in rms1.iterrows():
    rms1.loc[i,'error'] = np.sqrt(row['Error X']**2+row['Error Y']**2+row['Error Z']**2)
#%%

z = rms1['error']
z = z[:,np.newaxis]
#%%
x = np.linspace(rms1['x'].min(), rms1['x'].max(), 200)
y = np.linspace(rms1['y'].min(), rms1['y'].max(), 200)
z = np.linspace(rms1['error'].min(), rms1['error'].max(), 200)
#%%
z2,y2 = np.meshgrid(z, y)
x2, y2 = np.meshgrid(x, y)
#%%
# region = np.s_[5:50, 5:50]
# x, y, z = x[region], y[region], z[region]

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))


ls = LightSource(270, 45)
# To use a custom hillshading mode, override the built-in shading and pass
# in the rgb colors of the shaded surface calculated from "shade".
# rgb = ls.shade(z, cmap=cm, vert_exag=0.1, blend_mode='soft')
# surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=rgb,
#                        linewidth=0, antialiased=False, shade=False)

surf = ax.plot_surface(x2, y2, z2, rstride=1, cstride=1,antialiased=False, shade=False)
plt.show()
