#! /usr/bin/env python
"""
A script to pull out all interesting hits from a batch BLAST.

Inputs:
   * arg 1 -- batch BLAST output file.

Outputs:
   * all interesting hits are printed to stdout.
   
"""
INVERT = 0

import sys, _mypath, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "i", ("inverted",))
    for (a, o) in opts:
        if a in ("-i", "--inverted"):
            INVERT = 1

    (filename,) = args

except:
    sys.stderr.write("""\

Usage:
        %s [ -i|--inverted] blast_output_file

Description:
        Reads a BLAST output file and removes all entries with no matches.

        -i/--inverted removes all entries *with* matches.
        
""" % (sys.argv[0],))
    sys.exit(-1)


sys.stderr.write("Opening hits file '%s'...\n" % (filename,))

all_hits = open(filename).read()
length = len(all_hits)

sys.stderr.write("Read %d bytes.\n" % (length,))

PROGRAM = all_hits[0:50].split(' ')[0]
sys.stderr.write('program: %s\n' % (PROGRAM,))

assert PROGRAM in ('BLASTX', 'BLASTP', 'BLASTN', 'TBLASTN', 'TBLASTX')

MARKER = '\n%s' % (PROGRAM,)

top = 0
bot = all_hits.find(MARKER, 1)
total_bytes = 0

while 1:
    if top == length:
        break
    
    if bot == -1:                       # last BLAST; set to length.
        bot = length

    found = all_hits.find(" No hits found ", top, bot)
        
    if not INVERT:
        if found == -1: # not found!
           s = all_hits[top:bot]
           total_bytes += len(s)
           print s.strip()
    else:
        if found != -1:
            s = all_hits[top:bot]
            total_bytes += len(s)
            print s.strip()

    top = bot
    bot = all_hits.find(MARKER, top + 1)

sys.stderr.write("Done -- wrote %d bytes.\n" % (total_bytes,))
