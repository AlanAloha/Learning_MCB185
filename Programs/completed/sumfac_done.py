#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here
run_sum = 0
factorial = 1
for i in range(n,0,-1):
	run_sum += i
	factorial *= i
print(n, run_sum, factorial)
"""
python3 sumfac.py
5 15 120
"""
