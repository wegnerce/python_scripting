# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:28:45 2016

@author: calle
"""

prefixes = ["@", "author", "journal", "number", "pages", "title", "volume", "year", "doi", "}"]
#prefixes = ["url"]

open('/home/calle/Desktop/references_fixed.bib','w').writelines([ line for line in open('/home/calle/Desktop/references.bib') if line.startswith(tuple(prefixes))])
