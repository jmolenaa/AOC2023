import re


# part 1 functions ########################################################

def	get_part1_answer(workspace_dict, parts):

	part1 = 0
	parts = parts.split("\n")
	for part in parts:

		# stripping off brackets and splitting the parts into the four categories
		part = part.strip("}{").split(",")

		# making a list of the rating of every category, by grabbing the part after the =
		# x is in index 0, m in 1, a in 2, s in 3
		part = list(map(int, [part[0][2:], part[1][2:], part[2][2:], part[3][2:]]))

		# throwing the part through the workspaces to check if it gets accepted
		# if it does, the sum of the category ratings gets added to the total result
		if check_if_accepted(part, workspace_dict) == True:
			part1 += sum(part)
	
	return part1


def	check_if_accepted(part, workspace_dict):

	# we start in workspace "in"
	current_workspace = "in"

	while True:

		# gets all the conditions of the current workspace
		# by looking up the key in our dictionary
		# the value is a list of conditions with the target workspace if condition is met
		conditions = workspace_dict[current_workspace]

		# loops through each condition
		for condition in conditions:

			# if we reach the last condition it's the default case
			# this means we send the part to whatever workspace is in the condition
			if condition.find(":") == -1:
				current_workspace = condition

			# we check if our part meets the current condition
			# if it does we move the part to the target workspace
			elif condition_met(condition, part) == True:
				current_workspace = condition.split(":")[1]

			# we didnt meet the condition nor have we reached the end so we move to the next one
			else:
				continue
			break

		# if the target workspace is R or A we reject or accept the part accordingly
		if current_workspace == "R":
			return False
		elif current_workspace == "A":
			return True
		

def	condition_met(condition, part):

	# dictionary corresponding the category to the index in our part list
	category_dict = {"x" : 0, "m" : 1, "a" : 2, "s" : 3}

	# we get the comparison part of the condition, then split it into
	# the rating category we are comparing and to which number
	comparison = condition.split(":")[0]
	category, number = re.split("[<>]", comparison)

	# depending on which comparison is in the condition we compare the rating
	# from the target category and return True or False depending on if we pass the condition
	if comparison[1] == ">" and part[category_dict[category]] > int(number):
		return True
	elif comparison[1] == "<" and part[category_dict[category]] < int(number):
		return True
	return False




# part 2 functions ########################################################

def	get_part2_answer(workspace_dict):

	# list to which we will append any accepted ranges of ratings
	# every accepted range contains a list of 4 ranges, 1 for every category
	accepted_ranges = list()

	go_through_ranges(workspace_dict, accepted_ranges)

	part2 = 0
	# loops through accepted ranges and counts out all combinations
	# of the ratings in those ranges
	# it does this by multiplying all 4 lenghts of the ranges so f.e.
	# ranges (1, 200), (1, 100), (1000, 1001), (200, 300)
	# 200 * 100 * 2 * 100 = 4000000
	# range (1, 200) has 200 possibilities, 200 - 1 is 199, thats why we add 1 in our calculation
	for ranges in accepted_ranges:
		result_one_range = 1
		for range in ranges:
			result_one_range *= range[1] - range[0] + 1
		part2 += result_one_range
	return part2


def	go_through_ranges(workspace_dict, accepted_ranges):

	# starting range
	ranges = [[[1, 4000], [1, 4000], [1, 4000], [1, 4000], "in"]]

	# we looop through our ranges until we the list is empty
	# we add ranges whenever our conditions are met adn we split the range
	# or when we reach the end of a workspace
	# one range consists of the range of ratings for a specific category
	# and the workspace the range is in
	while ranges:

		current_range = ranges.pop()

		# if the workspace of our range is the accepted state we add the ranges
		# to our accepted list and continue to the next one
		# if it's rejected we just discard the range
		if current_range[4] == "A":
			accepted_ranges.append(current_range[:4])
			continue
		elif current_range[4] == "R":
			continue

		# we then loop through our conditions similarly to part1
		conditions = workspace_dict[current_range[4]]
		for condition in conditions:

			# if we reached the last condition of the workspace
			# the whole current_range gets added to our ranges list
			# but has a new workspace now
			if condition.find(":") == -1:
				ranges.append([*current_range[:4], condition])

			# else we consider the condition and split the range accordingly
			elif split_range_on_condition(condition, current_range, ranges) == True:
				break 


def	split_range_on_condition(condition, current_range, ranges):

	# dictionary corresponding the category to the index in our range list
	category_dict = {"x" : 0, "m" : 1, "a" : 2, "s" : 3}

	# we get the comparison part of the condition, then split it into
	# the rating category we are comparing and to which number
	comparison = condition.split(":")[0]
	category, number = re.split("[<>]", comparison)

	# we grab the range from our current range that corresponds to 
	# category that the condition applies to
	category_range = current_range[category_dict[category]]

	# this is just so I dont have to cast this stupid stuff everywhere
	number = int(number)

	# whatever the comparison we have three cases for where our range falls
	# case 1 -	the current range complies completely with the condition
	# 			in this case, the whole current range goes to the next workspace
	# case 2 -	the current range falls completely outside the condition
	# 			in this case, we continue within the current workspace with the current range
	# case 3 -	the current range falls sligthly within the condition and sligthly out
	# 			we add whatever falls within the condition as a new range with a new workspace
	# 			and then we adjust the current range to fit the condition and continue
	# 			with that one within the current workspace
	if comparison[1] == ">":

		# case 2
		if category_range[1] <= number:
			return False

		# case 3
		if category_range[0] <= number and category_range[1] > number:
			new_range = current_range.copy()
			new_range[category_dict[category]] = [number + 1, category_range[1]]
			new_range[4] = condition.split(":")[1]
			ranges.append(new_range)
			current_range[category_dict[category]] = [category_range[0], number]
			return False

		# case 1
		elif category_range[0] > number:
			current_range[4] = condition.split(":")[1]
			ranges.append(current_range)
			return True

	elif comparison[1] == "<":

		# case 1
		if category_range[1] < number:
			current_range[4] = condition.split(":")[1]
			ranges.append(current_range)
			return True

		# case 3
		if category_range[0] < number and category_range[1] >= number:
			new_range = current_range.copy()
			new_range[category_dict[category]] = [category_range[0], number - 1]
			new_range[4] = condition.split(":")[1]
			ranges.append(new_range)
			current_range[category_dict[category]] = [number, category_range[1]]
			return False

		# case 2
		if category_range[0] > number:
			return False





def	create_workspace_dictionary(workspaces):
	workspaces = workspaces.split("\n")
	workspace_dict = dict()
	for workspace in workspaces:
		workspace = workspace.strip("}")
		key, value = workspace.split("{")
		workspace_dict[key] = value.split(",")
	return workspace_dict


def main():
	with open("input") as file:
		workspaces, parts = file.read().split("\n\n")
	
	workspace_dict = create_workspace_dictionary(workspaces)

	part1 = get_part1_answer(workspace_dict, parts)
	part2 = get_part2_answer(workspace_dict)

	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")


if __name__ == "__main__":
	main()