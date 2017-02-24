# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:41:53 2017

@author: Administrator
"""
import os
os.chdir('E:\directory\dataiap-master\day3')

from collections import defaultdict
import matplotlib.pyplot as plt
import csv,datetime

reader = csv.DictReader(open("donations_sampled.txt",'r'))

obamadonations=[]
obamacumulations=defaultdict(lambda:0)
mccaindonations=[]
mccaincumulations=defaultdict(lambda:0)
amount1=0
amount2=0

for row in reader:
    name=row['cand_nm']
    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
    date=datetime.datetime.strptime(datestr,'%d-%b-%y')
    receipt_desc=row['receipt_desc']
    if True:
        if 'Obama' in name:
            obamadonations.append(amount)
        if 'McCain' in name:
            mccaindonations.append(amount)

plt.ylim((-250,1250))
plt.boxplot([obamadonations,mccaindonations],whis=1)

import welchttest
print("Welch's T-Test p-value:",welchttest.ttest(obamadonations,mccaindonations))[1]

import scipy.stats

print "Mann-Whitney U p-value", scipy.stats.mannwhitneyu(obamadonations,mccaindonations)[1]
#def sorted_by_date(donation_by_date):
#    return(sorted(donation_by_date.items(),key=lambda(key,val):key))

#sorted_by_date_obama=sorted_by_date(obamadonations)
#sorted_by_date_mccain=sorted_by_date(mccaindonations)

