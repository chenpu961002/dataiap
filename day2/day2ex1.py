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
    
    if True:
        if 'Obama' in name:
            obamadonations[date]+=amount
        if 'McCain' in name:
            mccaindonations[date]+=amount

#def sorted_by_date(donation_by_date):
#    return(sorted(donation_by_date.items(),key=lambda(key,val):key))

#sorted_by_date_obama=sorted_by_date(obamadonations)
#sorted_by_date_mccain=sorted_by_date(mccaindonations)

filtered_donations_obama=filter(lambda(x,y):y>=-18000 and y<=19000, obamadonations.items())
filtered_donations_mccain=filter(lambda(x,y):y>=-22000 and y<=22000, mccaindonations.items())

def donation_bucket(donations):
    donation_bucket=defaultdict(lambda:0)
    for row in donations:
        bucket = int(row[1]/100)
        donation_bucket[bucket]+=1
        print(donation_bucket.items())
    return(donation_bucket)

donation_bucket_obama=donation_bucket(filtered_donations_obama)
sorted_donation_bucket_obama=sorted(donation_bucket_obama.items(), key=lambda (key, value):key)
donation_bucket_mccain=donation_bucket(filtered_donations_mccain)
sorted_donation_bucket_mccain=sorted(donation_bucket_mccain.items(), key=lambda (key, value):key)


#accumulated_obama=cumulated_donations(sorted_by_date_obama)
#accumulated_mccain=cumulated_donations(sorted_by_date_mccain)

xs1,ys1=zip(*sorted_donation_bucket_obama)
xs2,ys2=zip(*sorted_donation_bucket_mccain)

fig=plt.figure(figsize=(10,6))
plt.bar(xs1,ys1,label='Obama\' donations')
plt.bar(xs2,ys2,label='McCain\' donations')
plt.bar(xs1,ys1,linewidth=0)
plt.bar([x + 0.25 for x in xs2],ys2,linewidth=0)
plt.legend(loc='upper right',ncol=4)
plt.title('Donation_Buckets')
plt.xlabel('$100 Buckets')
plt.savefig('donation_bucket_bar.png',format='png')
