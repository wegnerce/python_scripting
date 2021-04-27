#! /usr/bin/env python
import sys, string
sys.path.append('/u/t/dev/slippy/lib')
import fastaFile
import sets

matches_dict = {}

def handle_record(lines, line_n):
    line = lines[line_n]
    if line[0:6] != 'BLASTN':
        raise Exception("error, line_n is not at a BLAST record start.")

    # first find Query=
    while 1:
        line_n += 1
        if lines[line_n].find('Query= ') == 0:
            query_seq = lines[line_n][7:].strip()
            break

    # now, for each matching record, make a note of it:
    line_n += 11

    matches = {}
    line = lines[line_n].rstrip()
    while len(line) and not line[0] in string.whitespace:
        match = line[0:60].rstrip()

        matches[match] = 1

        line_n += 1
        line = lines[line_n].rstrip()

    #print len(matches), 'matches to', query_seq
    if len(matches):
        matches_dict[query_seq] = matches

    # now finish it off
    while line_n < len(lines):
        if lines[line_n][0:6] == 'BLASTN':
            return line_n
        line_n += 1

    return len(lines)

########

print 'opening files'

fasta_file = sys.argv[1]
lines = open(sys.argv[2]).readlines()

print 'iterating over records'

line_n = handle_record(lines, 0)
try:
   while line_n < len(lines):
      line_n = handle_record(lines, line_n)
except Exception, exc:
   print 'EXCEPTION:'
   print str(exc)
   print 'continuing!'

#
# now uniq
#

print 'uniqing'

l = matches_dict.keys()
sets_list = []

for seq in l:
    sets_list.append(sets.Set(matches_dict[seq]))

did_merge = 1
n = 1
while did_merge:
    leftovers = []
    did_merge = 0

    print n, '-->', len(sets_list)
    n += 1
    
    for i in range(0, len(sets_list)):
        set_a = sets_list[i]
        for j in range(i + 1, len(sets_list)):
            set_b = sets_list[j]
            
            if set_a.intersection(set_b):
                set_a.union_update(set_b)
                did_merge = 1
            else:
                leftovers.append(set_b)

        if did_merge:
            leftovers.extend(sets_list[: i + 1])
            sets_list = leftovers
            break

        leftovers = []

#
# load sequences
#

print 'loading sequences'

fasta_dict = {}
f = fastaFile.load(fasta_file)
for (name, seq) in f:
    fasta_dict[name] = seq

#
# iterate through & spit out
#

for n in range(0, len(sets_list)):
    o = open('clumps/clump.%d' % (n,), 'w')
    s = sets_list[n]
    for name in s:
        o.write('>%s\n%s\n' % (name, fasta_dict[name]))
        del fasta_dict[name]

    o.close()
