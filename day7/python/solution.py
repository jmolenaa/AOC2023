def identify_hand(hand):
	

	# creating a list of numbers that represent occurences of cards in our hand
	# f.e. a hand 88285, will make a list [3, 1, 1, 0, 0], the zeros dont matter
	# since I only ever use the first two numbers fomr the list
	# I do this by first making the hand a set and then for every unique char
	# counting how often it occurs in the hand
	# I then sort the list to have the highest occurence at the start
	# I skip the "1" char for part2 reasons, since it's a wildcard and I'll add it later
	countOfChars = [0] * 5
	set_hand = set(hand)
	for i, char in enumerate(set_hand):
		if char == "1":
			continue
		countOfChars[i] = hand.count(char)
	countOfChars.sort(reverse=True)


	# I count the amount of wildcards, then add them to the highest count of cards
	# This is always the optimal play int the game, since we have no straights or flushes
	wildcard = hand.count("1")
	countOfChars[0] += wildcard


	# depending on which type of hand I have I return an index, the lower the index the weaker the type
	# 6 - five of a kind
	# 5 - 4 of a kind
	# 4 - full house
	# 3 - three of a kind
	# 2 - two pair
	# 1 - pair
	# 0 - highest card
	match countOfChars[0]:
		case 5:
			return 6
		case 4:
			return 5
		case 3:
			match countOfChars[1]:
				case 2:
					return 4
				case _:
					return 3
		case 2:
			match countOfChars[1]:
				case 2:
					return 2
				case _:
					return 1
		case _:
			return 0
	

# splits hands into hand types, putting them into our ranks list, beginning with the weakest one
def	split_hands_into_ranks(lines, ranks, joker):


		# replaces the card symbols that are letters with hexadecimal values
		# this way the strength of the card corresponds to ascii value of the card
		# J is replaced for part1 by "b" as it is worth 11 (weaker than Q and stronger than T)
		# J is replaced for part2 by "1", weakest card
	for line in lines:
		line = line.replace("T", "a").replace("J", joker).replace("Q", "c").replace("K", "d").replace("A", "e")
		hand_type = identify_hand(line.split()[0])
		ranks[hand_type].append(line.split())


# calculating results by going through our list of cards by type
# sorting the type works due to changing the cards to different ascii values
# then I go through the hands in our type and add to result
def	calculate_result(ranks, part):
	result = 0
	game = 1
	
	for rank in ranks:
		rank.sort()
		for hand in rank:
			result += int(hand[1]) * game
			game += 1
	print("The result for part", part, "is:", result)


def main():
	lines = open("input").readlines()
	rankspart1 = list()
	rankspart2 = list()


	# creating 2 lists of 7 lists, one for every possible hand type, beginning with the weakest one
	for i in range(7):
		rankspart1.append(list())
		rankspart2.append(list())


	split_hands_into_ranks(lines, rankspart1, "b")
	calculate_result(rankspart1, 1)
	
	split_hands_into_ranks(lines, rankspart2, "1")
	calculate_result(rankspart2, 2)


if __name__ == "__main__":
	main()