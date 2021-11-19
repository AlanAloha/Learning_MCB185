#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change

gc_count = 0
for nt in dna:
	if nt == 'G' or nt == 'C': gc_count += 1
gc_percentage = gc_count/len(dna)

print(f'gc% is {gc_percentage:.2}')
"""
python3 gc.py
0.42
0.42
0.42
"""
