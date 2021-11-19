#!/usr/bin/env python3
# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

person = [i for i in range(1,26)]

bday = [random.randint(1,365) for i in range(1,26)]

count = 0
for day in bday:
	for days in bday:
		if day == days: 
			count+=1
			bday.remove(days)

print(count/25)


"""
python3 birthday.py
0.571
"""

