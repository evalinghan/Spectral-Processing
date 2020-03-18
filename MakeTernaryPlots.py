"""
Created March 12 2020

This program helps you plot a heat map in a ternary diagram
You will need the following python modules: matplotlib and ternary installed
Visit https://github.com/marcharper/python-ternary to install and use ternary

Creator: Eva L. Scheller, Email: eschelle@caltech.edu
"""



import matplotlib.pyplot as plt
import ternary


# Example data copied from another research project
# This example data includes 3 sets of data, each set includes 4 lists:
# 3 lists specify the position coordinates of the data points
# 1 list specify the value of the data points for the heat map
# Here you could load in your own data instead

Fe_content_1 = [98, 59, 93, 57, 0, 68, 0, 77, 90, 50, 0, 70, 60]
Mg_content_1 = [0, 38, 0, 38, 91, 22, 90, 13, 0, 36, 83, 11, 18] 
Ca_content_1 = [2, 3, 7, 5, 9, 10, 10, 10, 10, 14, 17, 19, 22]
Centroid_1 = [1.5663141918005208, 1.5035735692639427, 1.5522376756729193, 1.5013684821827553, 1.544054129000404,
              1.5345684149987764, 1.5473273907400225, 1.5434759685419552, 1.5636080706605098, 1.5192536792164231,
              1.5459514661419942, 1.5488698597004218, 1.5414350570636635]
Fe_content_2 = [34, 39, 45, 56, 58, 71, 75, 0, 0, 0, 65, 0, 9, 25, 33, 37, 47, 61, 0, 3, 9, 15, 31, 36, 41]
Mg_content_2 = [39, 36, 28, 18, 19, 6, 0, 70, 70, 71, 0, 62, 52, 36, 29, 24, 15, 0, 54, 52, 46, 38, 23, 18, 14]
Ca_content_2 = [27, 25, 27, 26, 23, 23, 25, 30, 30, 29, 35, 38, 39, 39, 38, 39, 38, 39, 46, 45, 45, 47, 46, 46, 45]
Centroid_2 = [1.5567326134155026, 1.5574378033787177, 1.5514673738419444, 1.5656649231729229, 1.5546261113202895,
              1.5836978688841856, 1.5832283693340561, 1.5471732966867326, 1.5472628741271099, 1.593486101199258,
              1.6039692698812396, 1.5474015507925021, 1.5646891743853011, 1.5677276467839809, 1.5744374460871111,
              1.5792900410850985, 1.5772091549738434, 1.5737918984994617, 1.5490999134774697, 1.5620145099347964,
              1.5642518156976908, 1.5903951612341563, 1.5849454312105162, 1.5774697695986533, 1.5948061433256078]
Fe_content_3 = [70, 75, 83, 83, 92, 100, 25, 25, 30, 50, 65, 0, 3, 10, 20, 20]
Mg_content_3 = [30, 25, 17, 17, 8, 0, 75, 75, 70, 50, 35, 100, 97.5, 90, 80, 80]
Ca_content_3 = [0] * 16
Centroid_3 = [1.4885488530953273, 1.49085469581267, 1.5131577760125254, 1.5106547043803769, 1.5278714837958016,
              1.5307164217398321, 1.5082361633704571, 1.5013357213744387, 1.4963409122334101, 1.4871330627720085,
              1.508818489411315, 1.5512324507319111, 1.5281724808813257, 1.52008539190772, 1.4857864379164432,
              1.4901761483541052]

# Collecting all of my copied data
Fe_full = Fe_content_1 + Fe_content_2 + Fe_content_3 #Position coordinate #1
Mg_full = Mg_content_1 + Mg_content_2 + Mg_content_3 #Position coordinate #2
Ca_full = Ca_content_1 + Ca_content_2 + Ca_content_3 #Position coordinate #3 - optional
Centroid_full = Centroid_1 + Centroid_2 + Centroid_3 #Value of data points

# You will need to construct a dictionary of your data in order to create the ternary plot
# Order your position coordinates as a tuble and use them as keys in the dictionary
# You need at least 2 position coordinates but you can use 3 as well
# Your dictionary values will be the value of your data point
data = {}
for i in range(len(Fe_full)):
    data[(Fe_full[i], Ca_full[i])] = Centroid_full[i] #Dictionary constructed

# Dictionary of axes colors for bottom (b), left (l), right (r).
axes_colors = {'b': 'g', 'l': 'r', 'r': 'b'}

#Set up ternary plot with the ternary module
scale = 100 #Set up the size of your axes (mine are set to be 0 -> 100)
numTicks = 10 #Set up how many ticks you want on axes

fig, ax = plt.subplots()
ax.axis("off")
figure, tax = ternary.figure(ax=ax, scale=scale)

# Use the line below to choose a ternary diagram style - read more in the github repos linked above
# Choose a colormap layout from the plt.cm module
# You can also change the markersize/style etc. if needed
tax.heatmap(data, scale, style='dual-triangular',cmap=plt.cm.get_cmap('plasma'))

# Specify boundary and gridline formats
tax.boundary(linewidth=0.5)
tax.gridlines(multiple=1, linewidth=2, alpha=0.1)

# Set and format axes ticks.
ticks = [i / float(numTicks) for i in range(numTicks + 1)]
tax.ticks(ticks=ticks, linewidth=1, clockwise=True, offset=0.03, tick_formats="%0.01f")
tax.clear_matplotlib_ticks()
tax._redraw_labels()
plt.tight_layout()

# Show and save your file - remember to label your file something useful
tax.show()
#_________Label your file________#
tax.savefig('YourTernaryPlot.png')
