#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

agtc = 'AGTC'

#read sys inputs
chrom_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])


#Generate random genome with size chrom_size
#Actually... not necessary to generate a randome genome
'''
chrom = ''
for i in range(chrom_size):
	rint = random.randint(0,3)
	chrom+=agtc[rint]
#print(chrom)
'''

#Generate random reads with size read_len for read_num number of times
num_reads = [0] * chrom_size

for i in range(read_num):
	position = random.randint(0,chrom_size)
	for i in range(position - int(read_len/2), position + int(read_len/2)): 
		if 0<=i<=chrom_size-1: num_reads[i]+=1

trimmed = num_reads[int(read_len/2):chrom_size-int(read_len/2)]

minimum = min(trimmed)
maximum = max(trimmed)
average = sum(trimmed)/len(trimmed)

print(f'{minimum} {maximum} {average}')

"""
python3 xcoverage.py 1000 100 100
5 20 10.82375
"""
