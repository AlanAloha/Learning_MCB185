#!/usr/bin/env python3

import argparse

# In prokaryotic genomes, genes are often predicted based on length
# Long ORFs are not expected to occur by chance
# Write a program that creates a histogram of ORF lengths in random DNA
# Your library should contain new functions for the following
#    1. generating random sequence
#    2. generating ORFs from sequence
# Your program should have command line options for the following:
#    + amount of sequence to generate
#    + GC fraction of sequence
# Thought questions
#    a. how does GC fraction affect the histogram?
#    b. what is a good length threshold for a gene?

