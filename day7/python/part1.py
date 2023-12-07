def identify_hand(hand):
	set_hand = set(hand)
	countOfChars = list()

	for i, char in enumerate(set_hand):
		count = 0
		for character in hand:
			if character == char:
				count +=1
		countOfChars.append(count)
	
	pair = 0
	three = 0
	four = 0
	five = 0
	for number in countOfChars:
		if number == 2:
			pair += 1
		elif number == 3:
			three += 1
		elif number == 4:
			four += 1
		elif number == 5:
			five += 1

	if five:
		return 6
	elif four:
		return 5
	elif three and pair:
		return 4
	elif three:
		return 3
	elif 2 == pair:
		return 2
	elif pair:
		return 1
	return 0



	# if (len(set_hand) == 5):
	# 	return 0
	# if (len(set_hand) == 4):




	# print(len(set_hand))
	
def	find_index(hand, sorted):
	
	# print(hand)
	for i, next_hand in enumerate(sorted):
		# print(hand, next_hand[0])
		if hand == next_hand[0]:
			continue
		for j, char in enumerate(hand):
			# print(char)
			# print(char.isdigit())
			if char == next_hand[0][j]:
				continue
			if char.isdigit() and next_hand[0][j].isdigit() and char > next_hand[0][j]:
				# print("HERE6")
				return i
			elif char == "A" and next_hand[0][j] != "A":
				# print("HERE5")
				return i
			elif char == "K" and (next_hand[0][j].isdigit() or next_hand[0][j] == "T" or next_hand[0][j] == "Q" or next_hand[0][j] == "J"):
				# print("HERE4")
				return i
			elif char == "Q" and (next_hand[0][j].isdigit() or next_hand[0][j] == "T" or next_hand[0][j] == "J"):
				# print("HERE3")
				return i
			elif char == "J" and (next_hand[0][j].isdigit() or next_hand[0][j] == "T"):
				# print("HERE2")
				return i
			elif char == "T" and next_hand[0][j].isdigit():
				# print("HERE")
				return i
			break 
	# print("HUH")
	return len(sorted)


def main():
	lines = open("input").readlines()

	ranks = list()
	for i in range(7):
		ranks.append(list())


	for line in lines:
		hand_type = identify_hand(line.split()[0])
		ranks[hand_type].append(line.split())

	result = 0
	game = 1
	sorted = list()
	for rank in ranks:
		print(rank)
		for hand in rank:
			index = find_index(hand[0], sorted)
			# print(index)
			sorted.insert(index, hand)
			# print(hand)
		for hand in reversed(sorted):
			result += int(hand[1]) * game
			game += 1
			print(hand)
		# print(sorted)
		sorted = list()

	print(result)








if __name__ == "__main__":
	main()