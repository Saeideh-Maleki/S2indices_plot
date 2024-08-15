#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from matplotlib.dates import MonthLocator, DateFormatter
import matplotlib.dates as mdates
import matplotlib.font_manager as font_manager
from datetime import datetime as dt
from datetime import datetime, timedelta
################################
########Graph for S2 indices
######################################
# Load dataset
region = 'Dijon'
year = 2020

# Define input and output directries
inuput_directory = f'F:/Project/{region}{year}'
output_directory = f'{inuput_directory}/Figs/S2indices'
os.makedirs(output_directory, exist_ok=True)

dataset = np.load(f'{inuput_directory}/S2_important.npz', allow_pickle=True)

#To create a variable from each array in npz file
y, S2, S2_ind = dataset["y"], dataset["S2"],  dataset["S2_ind"]
 id_parcels_S2, dates_S2 = dataset["id_parcels_S2"],dataset["dates_S2"]

# Define crop types and their colors
crop_types = ['TRN', 'SOJ', 'MIS', 'MIE', 'MID']
colors = ['blue', 'red', 'green', 'goldenrod', 'deeppink']

# To create graph for mean os all parcells of each crop type in crop_types
means = {crop: np.mean(S2_ind[y == crop], axis=0) for crop in crop_types}

# Define labels for y-axis
labels = ['LSWI', 'NBR2', 'NDRE', 'RESI', 'NDSVI', 'MODCRC', 'CIgreen', 'CI_red_edge', 'NDWI', 'RENDVI', 'GNDVI', 'EVI', 'MSAVI','NDVI']

# Plot and save each figure
for i, label in enumerate(labels):
    plt.figure(figsize=(15, 6))
    for crop, color in zip(crop_types, colors):
        plt.plot(dates_S2, means[crop][:, i], color=color, label=f'  {crop}')
    
    plt.xticks(rotation=45, fontsize=18,fontname='Palatino Linotype', fontweight="heavy")
    plt.yticks(fontsize=18,fontname='Palatino Linotype', fontweight="heavy")
    plt.xlabel('Date', fontsize=18, fontname='Palatino Linotype', fontweight="heavy")
    plt.ylabel(label, fontsize=18, fontname='Palatino Linotype', fontweight="heavy")
    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    font = font_manager.FontProperties(family='Palatino Linotype',size=18)
    plt.legend(loc=(0.15, -0.38),
            fancybox=True, shadow=True, ncol=5, prop=font)
    
    # Save figure
    plt.savefig(f'{output_directory}/Fig_{i}_{region}_{year}_{label}.jpg', bbox_inches='tight')
    plt.show()  

print("All plots saved successfully.")

