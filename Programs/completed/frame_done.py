#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

'''
frame = 0
position = 0
for nt in dna:
	if position%3 == 0: frame = 0
	print(position, frame, nt)
	position+=1
	frame+=1
'''

for position in range(len(dna)):
	if position%3 != 0: continue
	for frame in range(3): print(position+frame, frame, dna[position+frame])


"""
python3 frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
