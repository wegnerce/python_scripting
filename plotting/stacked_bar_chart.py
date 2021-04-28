# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 14:36:17 2017

@author: calle
"""

# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 5
totalMeans = (31.0, 66.1, 7.9, 30.2, 5.9)
#seqIMeans = (2.7, 5.9, 0.7, 2.9, 0.5)
#seqIIMeans = (0.2, 0.77, 0.12, 0.58, 0.14)
#totalStd = (0.1, 0.07, 0.04, 0.2, 0.01)
#seqIStd = (0.03, 0.02, 0.008, 0.05, 0.05)
#seqIIStd = (0.003, 0.01, 0.0, 0.03, 0.008)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, totalMeans, width, color='#d62728')
#p2 = plt.bar(ind, seqIMeans, width, bottom=totalMeans)
#p3 = plt.bar(ind, seqIIMeans, width, bottom=totalMeans+seqIMeans)


plt.ylabel('microg/g')
plt.title('Ln total ex + seq ex')
plt.xticks(ind, ('Ln', 'Ce', 'Pr', 'Nd', 'Sm'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0]), ('Total'))

plt.show()