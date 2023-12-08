import math


class Node:
	def __init__(self, left, right):
		self.left = left
		self.right = right


# makes a dictionary of locations and nodes with the left and right location
def make_nodes(lines):
	locations = dict()
	for line in lines[2:]:
		node_values = line.split()
		locations[node_values[0]] = Node(node_values[2][1:4], node_values[3][:3])
	return locations


# finds starting locations and makes a list of them
# by looping through the keys of the dicitonary and finding the ones ending with A
def	get_locations(locations):
	start_locations = list()
	for key in locations:
		if key[-1] == "A":
			start_locations.append(key)
	return start_locations


# finds the amount of steps it takes to get from the start location to first end location
# the input has been setup in such a way that after reaching the end location it takes
# the exact same amount of steps to get back to it
# the end location is cyclical, every x aount of steps we are there
def find_steps_to_z(location, locations, instructions):
	steps = 0
	previous_steps = 0
	while True:
		for char in instructions:
			if char == "L":
				location = locations[location].left
			elif char == "R":
				location = locations[location].right
			steps += 1
			if location[-1] == "Z":
				return steps


def main():
	lines = open("input").readlines()

	locations = make_nodes(lines)
	instructions = lines[0].strip()	# stripping newline
	start_locations = get_locations(locations)

	# makes list of steps it takes for every start location to get to its
	# corresponding end location, then gets the least common multiple to find the answer ot the puzzle
	# this works cause of the cyclical nature of getting form the start to the end
	# we do a little detour at location AAA to get the answer for part 1
	steps = list()
	for location in start_locations:
		if location == "AAA":
			print("Answer to part 1 is: ", find_steps_to_z(location, locations, instructions))
		steps.append(find_steps_to_z(location, locations, instructions))
	print("Answer to part 1 is: ", math.lcm(*steps))


if __name__ == "__main__":
	main()