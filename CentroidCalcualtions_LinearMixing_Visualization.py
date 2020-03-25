#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 13 2020

This scripts explores 2 different types of spectral calculations.

1) Spectral centroid calculations
2) Linear mixing

It also produces plots of data.
These plots were used in Scheller & Ehlmann (2020), JGR

Creator: Eva L. Scheller, Email: evalinghan@gmail.com

Not all test data set belong to the creator.
See Data folder for data set references. 
"""

import numpy as np
import matplotlib.pyplot as plt

def value_locates(wvs, num):
    '''
    This function finds the index of a list of wavelengths (wvs) that is the 
    subscript of a wavelength value closest to a given numerical value (num)
    Inputs: 
        wvs: a list of wavelengths
        num: a numerical value
    Return: 
        subscript: the index of wavelength value of interest
    '''
    diff_lst = []
    for i in wvs:
        diff_item = np.abs(i-num)
        diff_lst.append(diff_item)
    subscript = diff_lst.index(min(diff_lst))
    return subscript

def get_centroid(wvs, intensities, lower_lim, upper_lim):
    '''
    This function calculates the spectral centroid of a spectrum for a given range of wavelengths
    Input: 
        wvs: list of wavelengths
        intensities: list of associated spectral intensities
        lower_lim: lower limit of wavelength range of interest
        upper_lim: upper limit of wavelength range of interest
    Return: 
        centroid: the spectral centroid of the given wavelength range
    
    '''
    lower_lim = value_locates(wvs, lower_lim)
    upper_lim = value_locates(wvs, upper_lim)
    sum_1 = 0.0
    sum_2 = 0.0
    for i in range(lower_lim,upper_lim):
        sum_1 += intensities[i]*wvs[i]
        sum_2 += intensities[i]
    centroid = sum_1/sum_2
    return centroid

#! Set up your lower and upper lim for the wavelength range of which you are going to calculate the centroid
lower_lim = 1.0
upper_lim = 2.0

#______________Import and process all data_______________________#
#Import all spectra from the test data Klima_2007.txt
OPX_Brown_library = np.genfromtxt('Data/Klima_2007.txt',delimiter='\t')
wvs_Brown_OPX = OPX_Brown_library[2:,0]
OPX_1_Brown = OPX_Brown_library[2:,1]
OPX_2_Brown = OPX_Brown_library[2:,2]
OPX_3_Brown =OPX_Brown_library[2:,3]
OPX_4_Brown = OPX_Brown_library[2:,4]
OPX_5_Brown = OPX_Brown_library[2:,5]
OPX_6_Brown = OPX_Brown_library[2:,6]
OPX_7_Brown =OPX_Brown_library[2:,7]
OPX_8_Brown = OPX_Brown_library[2:,8]
OPX_9_Brown = OPX_Brown_library[2:,9]
OPX_10_Brown = OPX_Brown_library[2:,10]
OPX_11_Brown =OPX_Brown_library[2:,11]
OPX_12_Brown = OPX_Brown_library[2:,12]
OPX_13_Brown = OPX_Brown_library[2:,13]
OPX_14_Brown = OPX_Brown_library[2:,14]
OPX_15_Brown =OPX_Brown_library[2:,15]
OPX_16_Brown = OPX_Brown_library[2:,16]

All_OPX_Brown_spectra = [OPX_1_Brown,OPX_2_Brown,OPX_3_Brown,OPX_4_Brown,OPX_5_Brown,OPX_6_Brown,OPX_7_Brown,OPX_8_Brown,OPX_9_Brown,OPX_10_Brown,OPX_11_Brown,OPX_12_Brown,OPX_13_Brown,OPX_14_Brown,OPX_15_Brown,OPX_16_Brown]

#Now process the centroid of all the spectra
All_OPX_centroid = []
for lst in All_OPX_Brown_spectra:
    centroid = get_centroid(wvs_Brown_OPX,lst,lower_lim,upper_lim)
    All_OPX_centroid.append(centroid)

#Import all spectra from the test data HCPX_brown.txt
HCP_library = np.genfromtxt('Data/HCPX_brown.txt',delimiter='\t')
wvs_Brown_HCP = HCP_library[2:,0]
CPXL_1 = HCP_library[2:,1]
CPXL_2 = HCP_library[2:,2]
CPXL_3 = HCP_library[2:,3]
CPXL_4 = HCP_library[2:,4]
CPXL_5 = HCP_library[2:,5]
CPXL_6 = HCP_library[2:,6]
CPXL_7 = HCP_library[2:,7]
CPXL_8 = HCP_library[2:,8]
CPXL_9 = HCP_library[2:,9]
CPXL_10 = HCP_library[2:,10]
CPXL_11 = HCP_library[2:,11]
CPXL_12 = HCP_library[2:,12]
CPXL_13 = HCP_library[2:,13]
CPXL_14 = HCP_library[2:,14]
CPXL_15 = HCP_library[2:,15]
CPXL_16 = HCP_library[2:,16]
CPXL_17 = HCP_library[2:,17]
CPXL_18 = HCP_library[2:,18]
CPXL_19 = HCP_library[2:,19]
CPXL_20 = HCP_library[2:,20]
CPXL_21 = HCP_library[2:,21]
CPXL_22 = HCP_library[2:,22]
CPXL_23 = HCP_library[2:,23]
CPXL_24 = HCP_library[2:,24]
CPXL_25 = HCP_library[2:,25]

All_HCP_Brown_spectra = [CPXL_1,CPXL_2,CPXL_3,CPXL_4,CPXL_5,CPXL_6,CPXL_7,CPXL_8,CPXL_9,CPXL_10, 
                 CPXL_11,CPXL_12,CPXL_13,CPXL_14,CPXL_15,CPXL_16,CPXL_17,CPXL_18,CPXL_19,CPXL_20,
                 CPXL_21,CPXL_22,CPXL_23,CPXL_24,CPXL_25]

#Now process the centroid of all the spectra
All_HCP_centroid = []
for lst in All_HCP_Brown_spectra:
    centroid = get_centroid(wvs_Brown_HCP,lst,lower_lim,upper_lim)
    All_HCP_centroid.append(centroid)

#Import all spectra from the test data LCPX_brown.txt
LCPX_library = np.genfromtxt('Data/LCPX_brown.txt')
wvs_Brown_LCP = LCPX_library[:,0]
CPXL_1 = LCPX_library[:,1]
CPXL_2 = LCPX_library[:,2]
CPXL_3 = LCPX_library[:,3]
CPXL_4 = LCPX_library[:,4]
CPXL_5 = LCPX_library[:,5]
CPXL_6 = LCPX_library[:,6]
CPXL_7 = LCPX_library[:,7]
CPXL_8 = LCPX_library[:,8]
CPXL_9 = LCPX_library[:,9]
CPXL_10 = LCPX_library[:,10]
CPXL_11 = LCPX_library[:,11]
CPXL_12 = LCPX_library[:,12]
CPXL_13 = LCPX_library[:,13]

All_LCP_Brown_spectra = [CPXL_1,CPXL_2,CPXL_3,CPXL_4,CPXL_5,CPXL_6,CPXL_7,CPXL_8,CPXL_9,CPXL_10, 
                 CPXL_11,CPXL_12,CPXL_13]

#Now process the centroid of all the spectra
All_LCP_centroid = []
for lst in All_LCP_Brown_spectra:
    centroid = get_centroid(wvs_Brown_LCP,lst,lower_lim,upper_lim)
    All_LCP_centroid.append(centroid)

#set up indexing for figure
index_OPX = []
index_LCP = []
index_HCP = []
for i in All_OPX_centroid: 
    index_OPX.append(1)
for i in All_LCP_centroid: 
    index_LCP.append(2)
for i in All_HCP_centroid: 
    index_HCP.append(3)

#Import all spectra from the test data cannon_2017.txt
glasses_data = np.genfromtxt('Data/cannon_2017.txt')
wvs_glasses_nm = list(glasses_data[:,0])
wvs_glasses = [wv/1000 for wv in wvs_glasses_nm]
#Processes the centroid of all spectra
glasses_centroids = []
for glass_index in range(1,len(glasses_data[0])):
    glass_intensity = list(glasses_data[:,glass_index])
    centroid = get_centroid(wvs_glasses,glass_intensity,lower_lim,upper_lim)
    glasses_centroids.append(centroid)
glasses_index = [-3] * len(glasses_centroids) #set up indexing for figure

#Import and calcualte centroid for all spectra for the various test data below
#Plateau_9D44
Plateau_9D44 = list(np.genfromtxt('Data/9D44_plateau.csv',delimiter=','))
Plateau_161EF = list(np.genfromtxt('Data/16EF_Plateau.csv',delimiter=','))
All_plateau = Plateau_9D44 + Plateau_161EF
Plateau_index = [-1]*len(All_plateau) #set up indexing for figure
#BFU_9D44
BFU_9D44 = list(np.genfromtxt('Data/9D44_BFU.csv',delimiter=','))
AlteredBFU_9D44 = list(np.genfromtxt('Data/9D44_BFU_altered.csv',delimiter=','))
All_BFU = AlteredBFU_9D44 + BFU_9D44
BFU_index = [-2]*len(All_BFU) #set up indexing for figure
#MixLithPlan
MLP_9D44 = list(np.genfromtxt('Data/9D44_MixLithPlan.csv',delimiter=','))
MLP_161EF = list(np.genfromtxt('Data/16EF_MixLithPlan.csv',delimiter=','))
All_MLP = MLP_9D44 + MLP_161EF
MLP_index = [0]*len(All_MLP) #set up indexing for figure
#Dunes
Dune1 = np.genfromtxt('Data/Dune1_FRT000199C7_tab.txt',delimiter='\t')
wvs_dune1 = Dune1[:,0]
I_dune1 = Dune1[:,1]
Dune2 = np.genfromtxt('Data/Dune2_FRT000064D9_tab.txt',delimiter='\t')
wvs_dune2 = Dune2[:,0]
I_dune2 = Dune2[:,1]
dunes_centroid = [get_centroid(wvs_dune1,I_dune1,lower_lim,upper_lim),get_centroid(wvs_dune2,I_dune2,lower_lim,upper_lim)]
dunes_index=[-4]*len(dunes_centroid) #set up indexing for figure

print('I have finished importing all data....')

print('Now plotting data visualization figure...')
#Make a figure that visualizes all of the calculated centroid data
#Some data are shown as boxplots
plt.figure(1)
pt1, = plt.plot(index_OPX,All_OPX_centroid,'o',markeredgecolor='black',color='purple',label='Library OPX')
pt2, = plt.plot(index_LCP,All_LCP_centroid,'o',markeredgecolor='black',color='palevioletred',label='Library LCP')
pt3, = plt.plot(index_HCP,All_HCP_centroid,'o',markeredgecolor='black',color='orange',label='Library HCP')
bp1=plt.boxplot(All_BFU,positions=[-2],widths=0.75,showfliers=False,patch_artist=True,boxprops=dict(facecolor='dodgerblue'),medianprops=dict(color='black'))
bp2=plt.boxplot(All_plateau,positions=[-1],widths=0.75,showfliers=False,patch_artist=True,boxprops=dict(facecolor='green'),medianprops=dict(color='black'))
bp3=plt.boxplot(All_MLP,positions=[0],widths=0.75,showfliers=False,patch_artist=True,boxprops=dict(facecolor='darkviolet'),medianprops=dict(color='black'))
pt4, = plt.plot(glasses_index,glasses_centroids,'o',markeredgecolor='black',color='brown',label='Library glasses')
pt5, = plt.plot(dunes_index,dunes_centroid,'o',markeredgecolor='black',color='grey',label='Study area dunes')
plt.xlim(-6,6)
plt.legend()
plt.legend([pt1, pt2, pt3, pt4, pt5, bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['Library OPX','Library LCP','Library HCP','Library glasses','Study area dunes','BFU', 'LPU', 'MLPU'], loc='best')
plt.ylabel('Centroid')

#Moving on to the data processing step
#We will now calculate linear mixtures of selected spectra from all of our imported data
#Next we will calculate the spectral centroid of these linear mixtures and save these

#First we perform linear mixture calculations with the ValerieSmectitesWL data
percentages = list(np.arange(0.0,1.0,0.01))

#First we perform linear mixture calculation for glasses dataset
glass_spectrum = list(glasses_data[:,1])
#Perform linear mixture calculations with the spectrum named OPX_4_Brown 
OPX_glasses_centroids = []
LCP_glasses_centroids = []
HCP_glasses_centroids = []
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_OPX)):
        index=value_locates(wvs_glasses,wvs_Brown_OPX[i])
        new_intensity = perc*OPX_4_Brown[i]+(1-perc)*glass_spectrum[index]
        new_spectrum.append(new_intensity)
    OPX_glasses_centroids.append(get_centroid(wvs_Brown_OPX,new_spectrum,lower_lim,upper_lim))
#Perform linear mixture calculations with the spectrum #5 from All_LCP_Brown_spectra
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_LCP)):
        index=value_locates(wvs_glasses,wvs_Brown_LCP[i])
        new_intensity = perc*All_LCP_Brown_spectra[5][i]+(1-perc)*glass_spectrum[index]
        new_spectrum.append(new_intensity)
    LCP_glasses_centroids.append(get_centroid(wvs_Brown_LCP,new_spectrum,lower_lim,upper_lim))
#Perform linear mixture calculations with the spectrum #2 from All_LCP_Brown_spectra
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_HCP)):
        index=value_locates(wvs_glasses,wvs_Brown_HCP[i])
        new_intensity = perc*All_LCP_Brown_spectra[2][i]+(1-perc)*glass_spectrum[index]
        new_spectrum.append(new_intensity)
    HCP_glasses_centroids.append(get_centroid(wvs_Brown_LCP,new_spectrum,lower_lim,upper_lim))

#Repeat the same calculations as above for the dunes dataset
dunes_spectrum = I_dune2
OPX_dunes_centroids = []
LCP_dunes_centroids = []
HCP_dunes_centroids = []
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_OPX)):
        index=value_locates(wvs_dune2,wvs_Brown_OPX[i])
        new_intensity = perc*OPX_4_Brown[i]+(1-perc)*dunes_spectrum[index]
        new_spectrum.append(new_intensity)
    OPX_dunes_centroids.append(get_centroid(wvs_Brown_OPX,new_spectrum,lower_lim,upper_lim))
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_LCP)):
        index=value_locates(wvs_dune2,wvs_Brown_LCP[i])
        new_intensity = perc*All_LCP_Brown_spectra[5][i]+(1-perc)*dunes_spectrum[index]
        new_spectrum.append(new_intensity)
    LCP_dunes_centroids.append(get_centroid(wvs_Brown_LCP,new_spectrum,lower_lim,upper_lim))
for perc in percentages:
    new_spectrum = []
    for i in range(len(wvs_Brown_HCP)):
        index=value_locates(wvs_dune2,wvs_Brown_HCP[i])
        new_intensity = perc*All_LCP_Brown_spectra[2][i]+(1-perc)*dunes_spectrum[index]
        new_spectrum.append(new_intensity)
    HCP_dunes_centroids.append(get_centroid(wvs_Brown_LCP,new_spectrum,lower_lim,upper_lim))

print('I am done calculating all linear mixtures....')

print('Now plotting linear mixture visualization figure...')
#Now visualize all of our calculated centroids for the linear mixtures
#Box plots of BFU, plateau, and MLPU data are shown for easy comparison
plt.figure(2)
pt1, =plt.plot(percentages,OPX_glasses_centroids,color='brown')
plt.plot(percentages,LCP_glasses_centroids,color='brown')
plt.plot(percentages,HCP_glasses_centroids,color='brown')
pt2, =plt.plot(percentages,OPX_dunes_centroids,color='grey')
plt.plot(percentages,LCP_dunes_centroids,color='grey')
plt.plot(percentages,HCP_dunes_centroids,color='grey')
bp1=plt.boxplot(All_BFU,positions=[1.1],widths=0.1,showfliers=False,patch_artist=True,boxprops=dict(facecolor='dodgerblue'),medianprops=dict(color='black'))
bp2=plt.boxplot(All_plateau,positions=[1.2],widths=0.1,showfliers=False,patch_artist=True,boxprops=dict(facecolor='green'),medianprops=dict(color='black'))
bp3=plt.boxplot(All_MLP,positions=[1.35],widths=0.1,showfliers=False,patch_artist=True,boxprops=dict(facecolor='darkviolet'),medianprops=dict(color='black'))
plt.legend()
plt.xlim(0,2.2)
plt.xlabel('Pyroxene fraction')
plt.ylabel('Centroid')
plt.legend()
plt.legend([pt1, pt2, bp1["boxes"][0], bp2["boxes"][0], bp3["boxes"][0]], ['PX + Glass Mixtures','PX + Dune Mixtures','BFU', 'LPU', 'MLPU'], loc='best')


plt.show()




