# -*- coding: utf-8 -*-
"""
Created on Sat Mar 04 10:31:09 2017

@author: localadmin
"""

import sys, math
sys.path.append('E:/directory/dataiap-master/resources/util')
import email_util
from collections import Counter, defaultdict

def get_terms(terms):
    terms = terms.lower().split()
    try:
        terms=terms[:terms.index('>')]
    except:
        pass
    terms = filter(lambda term: len(term) > 3, terms)
    from email_util import STOPWORDS
    terms = filter(lambda term: term not in STOPWORDS, terms)
    
    import re
    pattern=r"^[a-zA-Z]+[a-zA-Z\-\']*[a-zA-Z]+$"
    terms=filter(lambda term:re.match(pattern,term),terms)
    return terms

folder_tf=defaultdict(Counter)


for e in email_util.EmailWalker('E:/directory/dataiap-master/datasets/emails/lay-k'):
    terms_in_email = get_terms(e['text'])
    folder_tf[e['folder']].update(terms_in_email)

def cal_i2norm(vect):
    vect=[item*item for item in vect]
    return math.sqrt(sum(vect))

for key in folder_tf.keys():
    vect=[v for (k,v) in folder_tf[key].items()]
    vect_i2norm=cal_i2norm(vect)
    i2nrom_value=dict([(k,v/vect_i2norm) for (k,v) in folder_tf[key].items()])
    folder_tf[key]=i2nrom_value



terms_per_folder=defaultdict(set)
nemails=0
for e in email_util.EmailWalker('E:/directory/dataiap-master/datasets/emails/lay-k'):
    terms_in_email=get_terms(e['text'])
    terms_per_folder[e['folder']].update(terms_in_email)



allterms=Counter()
for folder,terms in terms_per_folder.items():
    allterms.update(terms)
    
idfs={}
nfolders=len(terms_per_folder)
for term,count in allterms.iteritems():
    idfs[term]=math.log(nfolders/(1.0+count))
    
tfidfs={}
for folder,tfs in folder_tf.iteritems():
    tfidfs[folder]=map(lambda (k,v):(k,v*idfs[k]),tfs.items())

for folder,terms in tfidfs.items():
    sorted_by_count_top20=sorted(terms,key=lambda(k,v):v,reverse=True)[:20]
    print sorted_by_count_top20
    
from math import *
def cal_similarity(folder1_tfidfs,folder2_tfidfs):
    folder1_score=dict(folder1_tfidfs)
    folder2_score=dict(folder2_tfidfs)
    
    numerator=0.0
    for key,value in folder1_score.iteritems():
        dotscore=folder1_score[key]*folder2_score.get(key,0.0)
        numerator+=dotscore
    
    folder1_norm=math.sqrt(sum([score**2 for score in folder1_score.values()]))
    folder2_norm=math.sqrt(sum([score**2 for score in folder2_score.values()]))
    denominator=folder1_norm*folder2_norm+1.0
    similarity=numerator/denominator
    return similarity

def sort_by_count(key_value,top_n):
    sorted_by_count_topn=sorted(key_value,key=lambda(k,v):v,reverse=True)[:top_n]
    return sorted_by_count_topn

num_of_folders=len(tfidfs.keys())

folder_similarity=dict()
for i in range(0,num_of_folders-1):
    for j in range(i+1,num_of_folders):
        folder1=tfidfs.keys()[i]
        folder2=tfidfs.keys()[j]
        similarity=cal_similarity(sort_by_count(tfidfs[folder1],100),sort_by_count(tfidfs[folder2],100))
        key='%s and %s'%(folder1,folder2)
        folder_similarity[key]=similarity
        print folder_similarity
                         
sorted_similarity=sort_by_count(folder_similarity.items(),len(folder_similarity))
print('the sorted folder similarities are:')
for k,v in sorted_similarity:
    print('%s , %s '%(k,v))