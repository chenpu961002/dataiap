# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:11:37 2017

@author: Administrator
"""
import os 
os.chdir('E:\directory')
import sys
sys.path.append('E:/directory/dataiap-master/resources/util/')
import email_util

walker=email_util.EmailWalker('E:/directory/dataiap-master/datasets/emails/lay-k')
for email_dict in walker:
    print(email_dict['subject'])
    
import os,sys,math
sys.path.append('dataiap/resources/util')
from email_util import *
from collections import Counter,defaultdict

folder_tf = defaultdict(Counter)

for e in email_util.EmailWalker('E:/directory/dataiap-master/datasets/emails/lay-k'):
    terms_in_email = e['text'].split() # split the email text using whitespaces
    folder_tf[e['folder']].update(terms_in_email)

terms_per_folder=defaultdict(set)
nemails=0
for e in email_util.EmailWalker('E:/directory/dataiap-master/datasets/emails/lay-k'):
    terms_in_email=e['text'].split()
    terms_per_folder[e['folder']].update(terms_in_email)
    
allterms=Counter()
for folder,terms in terms_per_folder.iteritems():
    allterms.update(terms)

idfs={}
nfolders=len(terms_per_folder)

for term,count in allterms.iteritems():    
    idfs[term]=math.log(nfolders/(1.0+count))
    
tfidfs={}
for folder,tfs in folder_tf.items():
    tfidfs[folder]=map(lambda(k,v):(k,v*idfs[k]),tfs.items())
    
for folder,terms in tfidfs.items():
    sorted_by_top_20=sorted(terms,key=lambda(k,v):v,reverse=True)[:20]
    
print sorted_by_top_20