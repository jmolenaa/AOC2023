def differences(sequence):
	previous_number = sequence[0]
	new_sequence = list()
	for number in sequence[1:]:
		new_sequence.append(number - previous_number)
		previous_number = number
	return new_sequence

def main():
	lines = open("input").readlines()
	resultpart1 = 0
	resultpart2 = 0


	for line in lines:
		sequence = list(map(int, line.split()))

		# lists to keep track fo the first number and last number
		# of all the sequences from one inputline
		last_number, first_number = list(), list()
		while True:
			last_number.append(sequence[-1])
			first_number.append(sequence[0])

			# check if we reached he last sequence (all 0)
			if all(number == 0 for number in sequence):
				break

			# counts next sequence based on the differences between numbers in the current one
			sequence = differences(sequence)

		# the next number in the original sequence is the sum of all last numbers of all sequences 
		# therefore that sum is added to the result
		resultpart1 += sum(last_number)

		# calculates the value of the previous number in thte original sequence
		# we move through the first numbers and from every number we substract the previous
		# substraction, we start at 0
		new_value_at_start = 0
		for number in reversed(first_number):
			new_value_at_start = number - new_value_at_start
		resultpart2 += new_value_at_start


	print("Answer for part 1 is: ", resultpart1)
	print("Answer for part 2 is: ", resultpart2)

if __name__ == "__main__":
	main()