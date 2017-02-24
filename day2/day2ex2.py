# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 08:52:48 2017

@author: Administrator
"""

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
amount_obama=[]
amount_mccain=[]

for row in reader:
    name=row['cand_nm']
    datestr=row['contb_receipt_dt']
    amount=float(row['contb_receipt_amt'])
    date=datetime.datetime.strptime(datestr,'%d-%b-%y')
    receipt_desc=row['receipt_desc']
    
    if True:
        if 'Obama' in name:
            amount_obama.append(amount)
        if 'McCain' in name:
            amount_mccain.append(amount)

#def sorted_by_date(donation_by_date):
#    return(sorted(donation_by_date.items(),key=lambda(key,val):key))

#sorted_by_date_obama=sorted_by_date(obamadonations)
#sorted_by_date_mccain=sorted_by_date(mccaindonations)

def sorted_by_amount(donation_by_amount):
    return(sorted(donation_by_amount))

sorted_by_amount_obama=sorted_by_amount(amount_obama)
sorted_by_amount_mccain=sorted_by_amount(amount_mccain)

def accumulated_donations(sorted_by_amount):
    accumulated_donations=[]
    i=0
    for amount in sorted_by_amount:
        if i==0:
            accumulated_donations.append(amount)
        else:
            accumulated_donations.append(accumulated_donations[i-1]+sorted_by_amount[i])
        i+=1
    return(accumulated_donations)

accumulated_obama=accumulated_donations(sorted_by_amount_obama)
accumulated_mccain=accumulated_donations(sorted_by_amount_mccain)


fig=plt.figure(figsize=(10,6))
plt.plot(sorted_by_amount_obama,accumulated_obama,label='Obama\' donations')
plt.plot(sorted_by_amount_mccain,accumulated_mccain,label='McCain\' donations')

plt.legend(loc='upper right',ncol=4)
plt.title('Donation_Buckets')
plt.xlabel('Accumulated Buckets')
plt.savefig('day2ex2.png',format='png')
