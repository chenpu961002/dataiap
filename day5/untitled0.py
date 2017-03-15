# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:59:53 2017

@author: localadmin
"""
import sys
import math
from mrjob.protocol import JSONValueProtocol
from mrjob.job import MRJob
from term_tools import get_terms

class MRtermidf(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def mapper(self, key, email):
        for term in get_terms(email['text']):
            yield term, 1

    def reducer(self, term, howmany):
        idf=math.log(516893.0/sum(howmany))
        yield None, {'term': term, 'idf': idf}

if __name__ == '__main__':
        MRtermidf.run()

