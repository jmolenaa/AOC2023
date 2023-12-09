def differences(sequence):
	previous_number = sequence[0]
	new_sequence = list()
	for number in sequence[1:]:
		new_sequence.append(number - previous_number)
		previous_number = number
	return new_sequence

def main():
	lines = open("input").readlines()
	result = 0
	result2 = 0

	for line in lines:
		sequence = list(map(int, line.split()))
		last_number = [sequence[-1]]
		first_number = [sequence[0]]
		print(sequence)
		# while sum(sequence) != 0:
		while True:
			if all(number == 0 for number in sequence):
				break
			# print(sum(sequence))
			sequence = differences(sequence)
			last_number.append(sequence[-1])
			first_number.append(sequence[0])
			print(sequence)
		# print(last_number)
		print(first_number)
		result += sum(last_number)
		new_value_at_start = 0
		for number in reversed(first_number):
			print(number, new_value_at_start)
			new_value_at_start = number - new_value_at_start
		print(new_value_at_start)
		result2 += new_value_at_start
		# print (sum(last_number))
	print(result)
	print(result2)

if __name__ == "__main__":
	main()