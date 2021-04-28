'''
Created on December 11, 2012
@author: Carl-Eric Wegner - AG Liesack - Molecular Ecology - MPI Marburg
The below script interleaves paired-end reads (in .fastaq format) for 
downstream processing for instance im velvet. Submitting files in a zipped
form e.g. gzip is also possible. The use of a while loop makes this script
extremely memory-efficient and fast.
'''

import gzip
import argparse

def interface():
    args = argparse.ArgumentParser()
    args.add_argument('-l', '--left-input',
                      help='The first input file in fastq format.')

    args.add_argument('-r', '--right-input',
                      help='The first input file in fastq format.')

    args.add_argument('-o', '--output',
                      help='The output file in fastq format.')

    args = args.parse_args()
    return args


def process_reads(args):

    if args.left_input.endswith('.gz') or args.right_input.endswith('.gz'):

        left = gzip.open(args.left_input,'rb')
        right = gzip.open(args.right_input,'rb')
        fout = gzip.open(args.output,'wb')

    else:
        left = open(args.left_input,'rU')
        right = open(args.right_input,'rU')
        fout = open(args.output,'wb')


# USING A WHILE LOOP MAKE THIS SUPER FAST
# Details here:
# http://effbot.org/zone/readline-performance.htm

    while 1:

# process the first file
        left_line = left.readline()
        if not left_line: break
        fout.write(left_line)

        left_line = left.readline()
        fout.write(left_line)

        left_line = left.readline()
        fout.write(left_line)

        left_line = left.readline()
        fout.write(left_line)


# process the second file
        right_line = right.readline()
        fout.write(right_line)

        right_line = right.readline()
        fout.write(right_line)

        right_line = right.readline()
        fout.write(right_line)

        right_line = right.readline()
        fout.write(right_line)

    left.close()
    right.close()
    fout.close()
    return 0

if __name__ == '__main__':
    args = interface()
    process_reads(args)