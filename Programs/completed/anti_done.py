#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
rev_dna = ''

for i in range (len(dna)-1, -1, -1):
	if dna[i] == 'A': rev_dna+= 'T'
	elif dna[i] == 'C': rev_dna+= 'G'
	elif dna[i] == 'G': rev_dna+= 'C'
	else: rev_dna+='A'
	
print(dna, '\n'+ rev_dna)
"""
python3 anti.py
TTTTTTTTTTTCAGT
"""
