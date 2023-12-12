import functools
import time


# i - current iterator for our springs string
# j - current iteration in our damaged springs array
# prev - keeps track if we encountered a spring sequence in the previous iteration
# checks for current iteration if we have a sequence of either '?' or '#' chars that is equal to j
# if we do we call the function again increasing the iterator by j and j by 1
# if we didnt we check if we're at the end of the string or at a '#' char
# if we're at a '#' it means we can't find the current j in the string anymore so we stop the current branch
# we then call the function again increasing our iterator by 1 and keeping j the same
@functools.lru_cache(maxsize=None)
def	count_combinations(springs, damaged, i, j, prev):
	total = 0

	# exit condition, if we have gone through the whole damaged array
	# and the string does not contain '#' chars anymore that means we have a valid combination
	if j == len(damaged):
		if '#' in springs[i:]:
			return total
		else:
			return total + 1

	# checks if we have a sequence of chars with an extra chekc so we dont go out of bounds
	if i + damaged[j] <= len(springs) and all(char != '.' for char in springs[i : i + damaged[j]]):

		# makes sure we are not right after a previous sequence
		# this is in case we have a situation like below
		# .#?.# 1 1
		# first sequence would be the first '#', but our recursion would see '?'
		# as the next valid sequence, but then we have two broken springs next to eachother
		# we pretty much make sure we have a '.' in between sequences

		if prev == 0 and (i == 0 or springs[i - 1] != '#'):
			total += count_combinations(springs, damaged, i + damaged[j], j + 1, 1)

	# exits if we're at the string end
	# or we encountered a '#' char that is not part of broken springs sequence
	if i == len(springs) or springs[i] == '#':
		return total
	total += count_combinations(springs, damaged, i + 1, j, 0)
	return total


# splits the line and expands both splits by the expansion number either 1 or 5
# makes damaged a tuple of integers for caching purposes and comparisons
def	unpack_springs_damaged_numbers(line, expansion):
	springs, damaged = line.split()
	springs = '?'.join([springs] * expansion)
	damaged = ','.join([damaged] * expansion)
	damaged = tuple(map(int, (damaged.split(","))))
	return springs, damaged


def	main():
	lines = [line.strip() for line in open("input").readlines()]

	resultpart1 = 0
	resultpart2 = 0
	for line in lines:
		springs, damaged = unpack_springs_damaged_numbers(line, 1)
		resultpart1 += count_combinations(springs, damaged, 0, 0, 0)
		springs, damaged = unpack_springs_damaged_numbers(line, 5)
		resultpart2 += count_combinations(springs, damaged, 0, 0, 0)
	print(f"The answer to part 1 is: {resultpart1}")
	print(f"The answer to part 2 is: {resultpart2}")

if __name__ == "__main__":
	main()