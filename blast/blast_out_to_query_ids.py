#! /usr/bin/env python
"""
A script to find all of the query sequences in a given BLAST output file.

Useful after 'filter-hits.py' is run on a file, when it can be used
to extract the names of all of the "interesting" query sequences from
the original query list.  This can then be fed into 'extract.py' to
create a fasta list of all of the interesting query sequences.

Inputs:
   * arg 1 -- batch BLAST output file.

Outputs:
   * stdout -- list of names.
"""
import sys, _mypath

all_hits = open(sys.argv[1]).read()
length = len(all_hits)

top = 0
bot = all_hits.find('\nBLAST', 1)

while 1:
    if top == length:
        break
    
    if bot == -1:
        bot = length

    query_loc = all_hits.find('Query= ', top, bot)
    assert query_loc > -1
    
    query_loc_end = all_hits.find('\n', query_loc, bot)
    assert query_loc_end > -1

    # pull out the query.
    print all_hits[query_loc + 7:query_loc_end]

    top = bot
    bot = all_hits.find('\nBLAST', top + 1)
