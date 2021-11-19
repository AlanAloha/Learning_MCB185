#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math


nums = sys.argv[1:len(sys.argv)]
for i in range(len(nums)): nums[i] = float(nums[i])

nums.sort()

count = len(nums)
minimum = min(nums)
maximum = max(nums)
Sum = sum(nums)
mean = Sum/count
if len(nums)%2 == 1: median = nums[int(len(nums)/2)]
else: median = (nums[int(len(nums)/2)] + nums[int(len(nums)/2-1)])/2

std_dev = 0
for num in nums:
	diff = num - mean
	diff_sqr = math.pow(diff,2)	
	std_dev+=diff_sqr

std_dev = math.sqrt(std_dev/(count))

print(nums)
print(f'count: {count}\nMinimum: {minimum}\nMaximum: {maximum}\nMean: {mean:.3f}\nStd. dev: {std_dev:.3f}\nMedian: {median:.3f}')







"""
python3 stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
