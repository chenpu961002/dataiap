# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:41:53 2017

@author: Administrator
"""

import os
os.chdir('E:\directory\\')

from collections import defaultdict
import matplotlib.pyplot as plt
import csv,datetime

reader = csv.DictReader(open("donations_sampled.txt",'r'))

obamadonations=defaultdict(lambda:0)
obamacumulations=defaultdict(lambda:0)
mccaindonations=defaultdict(lambda:0)
mccaincumulations=defaultdict(lambda:0)
amount1=0
amount2=0

for row in reader:
    name=row['cand_nm']
    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
    date=datetime.datetime.strptime(datestr,'%d-%b-%y')
    receipt_desc=row['receipt_desc']
    
    if 'REATTRIBUTION TO SPOUSE' in receipt_desc:
        if 'Obama' in name:
            obamadonations[date]+=amount
            print(amount)
        if 'McCain' in name:
            mccaindonations[date]+=amount
            print(amount)

def sorted_by_date(donation_by_date):
    return(sorted(donation_by_date.items(),key=lambda(key,val):key))

sorted_by_date_obama=sorted_by_date(obamadonations)
sorted_by_date_mccain=sorted_by_date(mccaindonations)

def cumulated_donations(sorted_donations):
    accumulated_donations=[sorted_donations[0]]
    for index in range(1,len(sorted_donations)):
        accumulated_to_date=accumulated_donations[-1][1]+sorted_donations[index][1]
        accumulated_donations.append((sorted_donations[index][0],accumulated_to_date))
    return(accumulated_donations)

#accumulated_obama=cumulated_donations(sorted_by_date_obama)
accumulated_mccain=cumulated_donations(sorted_by_date_mccain)

#xs1,ys1=zip(*accumulated_obama)
xs2,ys2=zip(*accumulated_mccain)
#plt.plot(xs1,ys1,label='Obama\' donations')
plt.plot(xs2,ys2,label='McCain\' donations')
plt.legend(loc='upper center',ncol=4)
plt.savefig('reattribution to spouse.png',format='png')
