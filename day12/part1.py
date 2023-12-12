import collections 
import sys
import math
from math import comb
from array import array

def fill_questions(springs, damaged, i):
	
	if (i == len(springs)):
		return True

	print(springs, damaged)


def main():
	lines = [line.strip() for line in open("test_case").readlines()]

	array('b', lines[0])
	for line in lines:
		damaged = (line.split()[1].split(","))
		fill_questions(line.split()[0], damaged, 0)




if __name__ == "__main__":
	main()