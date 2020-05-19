#!/bin/python3
from Bio import SeqIO
import sys
import gzip
infile = sys.argv[1]
if infile.contains(".gz"): infile = gzip.open(sys.argv[1], "rt")
outfile = sys.argv[2]
SeqIO.convert(infile, 'embl', outfile, 'fasta')
