# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:58:06 2024

@author: s1505470
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:09:11 2022

@author: Mathew
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from skimage import io
import numpy as np
import pandas as pd
import csv
# Optionally, tweak styles.
mpl.rc('figure',  figsize=(5, 5))
mpl.rc('image', cmap='gray')



pathlist=[]

filename_contains='Pep_TMR_'

pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\1/")
pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\2/")
pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\3/")


for path in pathlist:
    
    name='All_MSD_Cropped.csv'
    
    data = pd.read_table(path+name,sep=",",header=None)
    
    number_of_tracks=data.shape[1]
    
    lengths=[]
    
    for a in range(1,number_of_tracks):
        col=data[a][1:]
        
        l=col.max()
        
        
        lengths.append(l)
    
    lengths_df = pd.DataFrame(lengths, columns=['Max_MSD'])
    lengths_df.to_csv(path + 'Lengths.csv', index=False)
        
    plt.hist(lengths, bins = 50,range=[0,1], rwidth=0.9,color='#ff0000',cumulative=True,density=True, histtype='step')
    plt.xlabel('Maximum MSD (nm)',size=20)
    plt.ylabel('Cumulative freq',size=20)
    plt.savefig(path+'Lengths.pdf')
    plt.show()
    
    plt.hist(lengths, bins=20, range=[0,0.6], rwidth=0.9, color='#ff0000')
    plt.xlabel('Maximum MSD (nm)', size=20)
    plt.ylabel('Frequency', size=20)
    plt.savefig(path + 'Lengths_Histogram.pdf')
    plt.show()