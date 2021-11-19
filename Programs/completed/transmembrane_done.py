#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
hydro_score = {
'I': 4.5,
'V': 4.2,
'L': 3.8,
'F': 2.8,
'C': 2.5,
'M': 1.9,
'A': 1.8,
'G': -0.4,
'T': -0.7,
'S': -0.8,
'W': -0.9,
'Y': -1.3,
'P': -1.6,
'H': -3.2,
'E': -3.5,
'Q': -3.5,
'D': -3.5,
'N': -3.5,
'K': -3.9,
'R': -4.5
}


def find_name(line):
	return line[1:line.index('|')-1]
	
def signal_peptide(seq):
	pep = seq[0:30]
	signal = False
	for i in range(30-8):
		KD = 0
		for j in range(8): KD += hydro_score[pep[i+j]]
		if KD/8 > 2.5: 
			signal = True
			break
	return signal
		
	

def hydrophobic_region(seq):
	region = seq[30:]
	hydrophobic = False
	for i in range(len(region)-11):
		peptide = region[i:i+11]
		KD = 0
		if 'P' in peptide: continue
		for aa in peptide: KD += hydro_score[aa]
		if KD/11 > 2.0: 
			hydrophobic = True
			break
	return hydrophobic
	'''
	hydrophobic = False
	proline = True
	pep = seq[30:41]
	if 'P' in pep: proline = False
	KD = 0
	for aa in pep: KD += hydro_score[aa]
	if KD > 2.0/11 and proline: 
		return True
	else:
		return False
	'''
	
	
	

	
ff = open(sys.argv[1])



trans_mem = []
for line in ff.readlines():
	if ('>' in line): 
		seq = ''
		forward = ('FORWARD' in line)
		name = find_name(line)
	else:
		if '*' in line:
			seq += line
			seq = seq.replace('*','')
			seq = seq.replace('\n','')
			seq = seq.replace(' ','')
			#if forward is False: seq = seq[::-1]
			#print(name)
			#print(seq)
			if signal_peptide(seq) and hydrophobic_region(seq):
				trans_mem.append(name)
	
		else: seq += line
			
for protein in trans_mem:
	print(protein)
			
	
		
		
	
"""
python3 Programs/transmembrane.py Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
