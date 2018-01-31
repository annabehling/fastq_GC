#!/usr/bin/env python3
import sys

def at(line):
    """count a and t in dna sequence"""
    count = 0
    for letter in line:
        if (letter == "A") or (letter == "T"):
            count += 1
    return count


def at_file(infile, outfile):
    """count a and t in dna sequence in any fastq file
    infile is a .fastq file, outfile is a .txt file
    outfile will contain the AT percentage of each DNA sequence in the fastq file"""
    count = 0
    with open (infile) as fastq_file:
        outhandle = open(outfile, "w")
        for i,line in enumerate(fastq_file):
            if i % 4 == 1:
                at_pct = (at(line)/len(line))
                outhandle.write("{}\n".format(at_pct))
          
        
if __name__ == '__main__':
    try:
        infile = sys.argv[1]
        outfile = sys.argv[2]    
        print('i got executed')
    except IndexError:
        print("Usage: ./fast_GC.py [infile] [outfile]")
        sys.exit(1)
    at_file(infile, outfile)
    sys.exit(0)
