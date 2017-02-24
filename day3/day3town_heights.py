# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:39:10 2017

@author: Administrator
"""

import os
os.chdir('E:\directory\dataiap-master\day3')
import matplotlib.pyplot as plt
import numpy
town1_heights=[5,6,7,6,7.1,6,4]
town2_heights=[5.5,6.5,7,6,7.1,6]

town1_mean=numpy.mean(town1_heights)
town2_mean=numpy.mean(town2_heights)

print("Town 1 avg. height",town1_mean)
print("Town 2 avg. height",town2_mean)
print("Effect size",abs(town1_mean-town2_mean))

fig=plt.figure()
sub=fig.add_subplot(111)
sub.boxplot([town1_heights,town2_heights],whis=1)
plt.savefig('town_boxplots.png',format='png')

import welchttest
print("Welch's T-Test p-value:",welchttest.ttest(town1_heights,town2_heights))[1]

import scipy.stats
print("Town 1 Shapiro-Wilks p-value",scipy.stats.shapiro(town1_heights)[1])

import scipy.stats

print "Mann-Whitney U p-value", scipy.stats.mannwhitneyu(town1_heights, town2_heights)[1]

