lines = open("input").readlines()
set1 = set()
set2 = set()
part1answer = 0
part2answer = 0
number_of_cards = [1] * len(lines)

for i, line in enumerate(lines):
	split = line.split()

	# splitting input into two sets, one for winning numbers, one for our numbers
	set = 1
	for number in split:
		if number == "|":
			set = 2
		elif set == 1:
			set1.add(number)
		else:
			set2.add(number)

	# getting a new set3 of repeating numbers in set1 and set2
	set3 = set1.intersection(set2)

	# adding the amount of current cards to the next x cards, x being the amount of numbers in set3
	for k in range(len(set3)):
		if i + k + 1 == len(lines):		# making sure we dont go out of bounds of the set
			break
		number_of_cards[i + k + 1] += number_of_cards[i]

	# making sure set isnt empty so we cna add the result to our part1answer
	if len(set3) != 0:
		part1answer += pow(2, len(set3) - 1)

	set1.clear()
	set2.clear()
	
for number in number_of_cards:
	part2answer +=number
	
print("Answer to part1: " + str(part1answer))
print("Answer to part2: " + str(part2answer))