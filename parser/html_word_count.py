# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 10:14:16 2014

@author: calle
"""

import nltk
import string
from urllib import urlopen
from itertools import imap

url = "/media/TOSHIBA EXT/_projects/_rice_straw_breakdown/mRNA-tag/analysis/CAZymes/SigP_THMM/data/GHs/BS7dC_+.html"
html = urlopen(url).read()
text = nltk.clean_html(html)
text_noPunc = text.translate(string.maketrans("",""), string.punctuation)
words = text_noPunc.split()
max_word_len = max(imap(len, words))
vocabulary = nltk.probability.FreqDist(words)

for word in vocabulary:
    print word,
    print ' ' * (max_word_len + 5 - word.__len__()),
    print str(vocabulary[word])