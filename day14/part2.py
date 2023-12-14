from array import array
import numpy
import time


def move_north(lines):
	for x in range(len(lines[0])):
		last_obstacle = -1
		for y in range(len(lines)):
			if lines[y][x] == "O":
				lines[y][x] = "."
				lines[last_obstacle + 1][x] = 'O'
				last_obstacle = last_obstacle + 1
			elif lines[y][x] == "#":
				last_obstacle = y


def	move_west(lines):
	for y in range(len(lines)):
		last_obstacle = -1
		for x in range(len(lines[0])):
			if lines[y][x] == 'O':
				lines[y][x] = "."
				lines[y][last_obstacle + 1] = 'O'
				last_obstacle = last_obstacle + 1
			elif lines[y][x] == "#":
				last_obstacle = x


def move_south(lines):
	for x in range(len(lines[0])):
		last_obstacle = len(lines)
		for y in reversed(range(len(lines))):
			if lines[y][x] == "O":
				lines[y][x] = "."
				lines[last_obstacle - 1][x] = 'O'
				last_obstacle = last_obstacle - 1
			elif lines[y][x] == "#":
				last_obstacle = y


def	move_east(lines):
	for y in range(len(lines)):
		last_obstacle = len(lines[0])
		for x in reversed(range(len(lines[0]))):
			if lines[y][x] == 'O':
				lines[y][x] = "."
				lines[y][last_obstacle - 1] = 'O'
				last_obstacle = last_obstacle - 1
			elif lines[y][x] == "#":
				last_obstacle = x


def do_cycle(lines, part1):
	move_north(lines)
	if part1 == True:
		print(f"The answer to part1 is: {count_load(lines)}")
	move_west(lines)
	move_south(lines)
	move_east(lines)


def	count_load(lines):
	load = 0
	for i, row in enumerate(lines):
		load += ''.join(row).count('O') * (len(lines) - i)
	return load


def	calculate_answer(cycle_start_index, load_list):
	cycle_len = len(load_list[cycle_start_index:])
	cycle_amount_after_starting = 1000000000 - cycle_start_index - 1
	cycles_left = cycle_amount_after_starting % cycle_len
	final_load = load_list[cycle_start_index + cycles_left]
	print(f"The answer to part2 is: {final_load}")


def main():
	with open("input") as file:
		lines = file.read().splitlines()
	for i, line in enumerate(lines):
		lines[i] = array('u',line)
	lines = numpy.array(lines)
	load_list = list()
	print("Calculating part2 takes about 5 seconds, please be patient :(\n")

	part1 = True
	while True:
		do_cycle(lines, part1)
		part1 = False
		load = count_load(lines)

		# if the current load had already appeared we check for cycles
		if load in load_list:

			# gets the indexes of the current load in our load list
			indexes = [index for index, value in enumerate(load_list) if value == load]
			diffs = set()
			previous = indexes[-1]

			# loops through the indexes from the back
			for j, index in enumerate(reversed(indexes[:-1])):

				# adds how far apart our loads are form eachother
				# adds into a set so we remove duplicates
				diffs.add(previous - index)

				# if our set has moe than one value it means, the loads aren't repeating cyclically
				# (loads )
				if len(diffs) != 1:
					break
				if j == 3:
					calculate_answer(indexes[-1], load_list)
					return
				previous = index

		load_list.append(load)



if __name__ == "__main__":
	main()