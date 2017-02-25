# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 09:28:16 2017

@author: Administrator
"""
import os 
os.chdir('E:\directory\dataiap-master\day3')
import csv

def read_csv(file_name, cols, check_reliable):
    reader = csv.DictReader(open(file_name, 'rU'))
    rows = {} # map "statename__countyname" to the column names in cols
    for row in reader:
        if check_reliable and row['Unreliable'] == "x": # discard unreliable data
            continue
        if row['County'] == "": # ignore the first entry for each state
            continue
        rname = "%s__%s" % (row['State'], row['County'])
        try: # if a row[col] is empty, float(row[col]) throws an exception
            rows[rname] = [float(row[col]) for col in cols]
        except:
            pass
    return rows

import numpy

def get_arrs(dependent_cols, independent_cols):
    ypll = read_csv("E:/directory/dataiap-master/datasets/county_health_rankings/ypll.csv", dependent_cols, True)
    measures = read_csv("E:/directory/dataiap-master/datasets/county_health_rankings/additional_measures_cleaned.csv", independent_cols, False)

    ypll_arr = []
    measures_arr = []
    for key, value in ypll.iteritems():
        if key in measures: # join ypll and measures if county is in both
            ypll_arr.append(value[0])
            measures_arr.append(measures[key])
    return (numpy.array(ypll_arr), numpy.array(measures_arr))

dependent_cols = ["YPLL Rate"]
independent_cols = ["Population", "< 18", "65 and over", "African American",
                    "Female", "Rural", "%Diabetes" , "HIV rate",
                    "Physical Inactivity" , "mental health provider rate",
                    "median household income", "% high housing costs",
                    "% Free lunch", "% child Illiteracy", "% Drive Alone"]

ypll_arr, measures_arr = get_arrs(dependent_cols, independent_cols)
print ypll_arr.shape
print measures_arr[:,1].shape
                  
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(6,10))

subplot=fig.add_subplot(411)
subplot.scatter(measures_arr[:,6],ypll_arr)
subplot.set_title("ypll vs. % of population with diabetes")

subplot = fig.add_subplot(412)
subplot.scatter(measures_arr[:,1], ypll_arr, color="#1f77b4") # 1 = age
subplot.set_title("ypll vs. % population less than 18 years of age")

subplot = fig.add_subplot(413)
subplot.scatter(measures_arr[:,10], ypll_arr, color="#1f77b4") # 10 = income
subplot.set_title("ypll vs. median household income")

subplot = fig.add_subplot(414)
subplot.scatter(measures_arr[:,12], ypll_arr, color="#1f77b4") # 10 = income
subplot.set_title("ypll vs. Free lunch")

plt.savefig('four-scatters.png', format='png')

import ols

model=ols.ols(ypll_arr,measures_arr[:,6],"YPLL RATE",["% Diabetes"])
model.summary()
