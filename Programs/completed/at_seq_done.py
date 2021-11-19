#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
seq = ''
at_count = 0
for i in range(30):
	n = random.randint(1,10);
	print(n,end=' ')
	if 1<=n<=3: 
		seq+='A'
		at_count+=1
	elif 4<=n<=6:
		seq+='T'
		at_count+=1
	elif 7<=n<=8: seq+='G'
	else: seq+='C'

print('\n',len(seq), at_count/len(seq), seq)

"""
python3 at_seq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
