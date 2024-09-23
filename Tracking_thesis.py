# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 22:56:34 2024

@author: s1505470
"""

from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from skimage import io
import trackpy as tp
import numpy as np

# Optionally, tweak styles.
mpl.rc('figure',  figsize=(5, 5))
mpl.rc('image', cmap='gray')



pathlist=[]

filename_contains='Pep_TMR_'

pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\1/")
pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\2/")
pathlist.append(r"D:\Back_UP\TIRFM\20220408_101Aand101B_heat_treatment\BSA_100nM101B_1nMCy3B_2022-04-08_12-05-59\3/")


# fig, ax = plt.subplots()
# ax.hist(f['mass'], bins=20)
# plt.figure()
# tp.subpx_bias(f)


        

# This detects all of spots in 1 frame and shows. 
def single(fr,num,mass):
    si=tp.locate(frame[fr], num, minmass=mass)
    plt.figure()
    tp.annotate(si, frame[fr],imshow_style={'vmin':0,'vmax':3000},plot_style={'markersize':5,'markeredgewidth':0.8})
    fig, ax = plt.subplots()
    ax.hist(si['mass'], bins=20)
    plt.figure()
    tp.subpx_bias(si);
          
               


def tracks():    
    # Find tracks: First number is the jump distance, the second is how many frames it can be missing by

    t = tp.link_df(f, 5, memory=5)
    # Next, filter those tracks in which the length isn't long enough   
    t1 = tp.filter_stubs(t, 5)
    # Compare the number of particles in the unfiltered and filtered data.
    print('Before:', t['particle'].nunique())
    print('After:', t1['particle'].nunique())
    save=plt.figure()
    ax = tp.plot_traj(t1)
    save.savefig(path+'tracks.pdf')
    t1.to_csv(path  + 'Track_results.csv') 
    d = tp.compute_drift(t1)
    tm = tp.subtract_drift(t1.copy(), d)
    tm.to_csv(path  + 'Track_results_drift.csv') 
    plt.figure()
    
    return t1
   
def stats(t1):
    global im     
    
    im = tp.imsd(t1, 103/1000.,50)  # microns per pixel = 100/285., frames per second = 24
 
    
    im.to_csv(path  + 'All_MSD_Cropped_8000.csv')
    
    em = tp.emsd(t1, 103/1000.,20)
    fig, ax = plt.subplots()
    ax.plot(em.index, em, 'o')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set(ylabel=r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]',
           xlabel='lag time $t$')
    ax.set(ylim=(1e-2, 10));
    tp.utils.fit_powerlaw(em)



for path in pathlist:
    
    for root, dirs, files in os.walk(path):
                for name in files:
                        if filename_contains in name:
                            # if ".txt" in name:
                                # if "_FitResults" not in name:
                                resultsname = name
                                print(resultsname)
    
    image_path=path+resultsname
    
    # Load the frames:
    frame=io.imread(image_path)


    # Test single:
        
    # single(100,7,2000)  
    
    # Detect all spots
    if __name__ == '__main__':   
        f = tp.batch(frame[0:500], 7, minmass=2000)
    
        t1=tracks()
    
        im = tp.imsd(t1, 103/1000.,50)  # microns per pixel = 100/285., frames per second = 24
        im.to_csv(path  + 'All_MSD_Cropped.csv')
    
        
        # imy=np.linspace(0.02,2,100)

        # imx=im[0]
        # plt.plot(imy,imx)
        # a,b = np.polyfit(imy, imx, 1)
        # plt.plot(imy, a*imy+b)
        # plt.show()
        
        em = tp.emsd(t1,103/1000.,50)
        em.to_csv(path  + 'Ave_MSD_Cropped.csv')
        
        
        