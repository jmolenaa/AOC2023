import numpy
from array import array
import time

class	grid_class:
	def __init__(self, start, cycle_steps, pos, grid, positions):
		self.start = start
		self.cycle_steps = cycle_steps
		self.pos = pos
		self.grid = grid
		self.positions = positions
		self.escapees = [0, 0, 0, 0]
	def __repr__(self):
		return f"start {self.start}"


def	step_in_grid(grid_info, length, width):
	grid = grid_info.grid
	next_positions = grid_info.positions
	positions = next_positions.copy()
	next_positions.clear()
	escapees = list()
	while positions:
		pos = positions.pop()
		grid[pos[0]][pos[1]] = "."
		if pos[0] + 1 < length and grid[pos[0] + 1][pos[1]] in ".":
			grid[pos[0] + 1][pos[1]] = 'O'
			next_positions.append((pos[0] + 1, pos[1]))
		if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] in ".":
			grid[pos[0] - 1][pos[1]] = 'O'
			next_positions.append((pos[0] - 1, pos[1]))
		if pos[1] + 1 < width and grid[pos[0]][pos[1] + 1] in ".":
			grid[pos[0]][pos[1] + 1] = 'O'
			next_positions.append((pos[0], pos[1] + 1))
		if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] in ".":
			grid[pos[0]][pos[1] - 1] = 'O'
			next_positions.append((pos[0], pos[1] - 1))

		if pos[0] + 1 == length and grid_info.escapees[0] == 0:
			grid_info.escapees[0] = 1
			escapees.append((pos[0] + 1, pos[1]))
		if pos[0] - 1 < 0 and grid_info.escapees[1] == 0:
			grid_info.escapees[1] = 1
			escapees.append((pos[0] - 1, pos[1]))
		if pos[1] + 1 == width and grid_info.escapees[2] == 0:
			grid_info.escapees[2] = 1
			escapees.append((pos[0], pos[1] + 1))
		if pos[1] - 1 < 0 and grid_info.escapees[3] == 0:
			grid_info.escapees[3] = 1
			escapees.append((pos[0], pos[1] - 1))

	return escapees

def	check_for_duplicates(grids, position):
	for grid in grids:
		if grid.start == position:
			return True
	return False

def	grid_coordinate(grid_info, escapee):
	return (0,0)


def	add_grids(grids, escapees, lines, grid_info):
	for escapee in escapees:
		next_positions = [(escapee[0] % 131, escapee[1] % 131)]
		if check_for_duplicates(grids, next_positions[0]) == True:
			continue
		grids.append(grid_class(next_positions[0], -1, grid_coordinate(grid_info.pos, escapee), numpy.copy(lines), next_positions))
		# print(escapee)

def	clear_grids(grids, lines):
	for grid in grids:
		grid.grid = numpy.copy(lines)
		grid.positions = [grid.start]
		# print(grid.positions)
		# print(grid)
		# for line in grid.grid:
		# 	print(''.join(line))

def	find_step_cycle(grid_info, lines, length, width):
	grid = numpy.copy(lines)
	next_positions = [grid_info.start]
	cycle = [0, 0]
	print("next grid", grid_info)
	for i in range(300):
		# if cycle[0] == len(next_positions):
		# 	break
		cycle[i % 2] = len(next_positions)
		positions = next_positions.copy()
		next_positions.clear()
		while positions:
			pos = positions.pop()
			grid[pos[0]][pos[1]] = "."
			if pos[0] + 1 < length and grid[pos[0] + 1][pos[1]] in ".":
				grid[pos[0] + 1][pos[1]] = 'O'
				next_positions.append((pos[0] + 1, pos[1]))
			if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] in ".":
				grid[pos[0] - 1][pos[1]] = 'O'
				next_positions.append((pos[0] - 1, pos[1]))
			if pos[1] + 1 < width and grid[pos[0]][pos[1] + 1] in ".":
				grid[pos[0]][pos[1] + 1] = 'O'
				next_positions.append((pos[0], pos[1] + 1))
			if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] in ".":
				grid[pos[0]][pos[1] - 1] = 'O'
				next_positions.append((pos[0], pos[1] - 1))
	# print(len(next_positions))
	
	print(cycle)
	return cycle


def	count_steps(grid_info, lines, steps, length, width):
	grid = numpy.copy(lines)
	next_positions = [grid_info.start]
	for i in range(steps):
		# if cycle[0] == len(next_positions):
		# 	break
		positions = next_positions.copy()
		next_positions.clear()
		while positions:
			pos = positions.pop()
			grid[pos[0]][pos[1]] = "."
			if pos[0] + 1 < length and grid[pos[0] + 1][pos[1]] in ".":
				grid[pos[0] + 1][pos[1]] = 'O'
				next_positions.append((pos[0] + 1, pos[1]))
			if pos[0] - 1 >= 0 and grid[pos[0] - 1][pos[1]] in ".":
				grid[pos[0] - 1][pos[1]] = 'O'
				next_positions.append((pos[0] - 1, pos[1]))
			if pos[1] + 1 < width and grid[pos[0]][pos[1] + 1] in ".":
				grid[pos[0]][pos[1] + 1] = 'O'
				next_positions.append((pos[0], pos[1] + 1))
			if pos[1] - 1 >= 0 and grid[pos[0]][pos[1] - 1] in ".":
				grid[pos[0]][pos[1] - 1] = 'O'
				next_positions.append((pos[0], pos[1] - 1))
	# for line in grid:
	# 	print(''.join(line))
	return len(next_positions)

def main():
	with open("input") as file:
		lines = file.read().split("\n")

	numpy.set_printoptions(linewidth=numpy.inf)
	for i, line in enumerate(lines):
		lines[i] = array('u', line)
	lines = numpy.array(lines)
	width = len(lines[0])
	length = len(lines)
	for y, line in enumerate(lines):
		for x, char in enumerate(line):
			if char == "S":
				next_positions = [(y, x)]
				lines[y, x] = "."

	clear_grid = numpy.copy(lines)

	grids = [[numpy.copy(lines), next_positions]]
	grids = [grid_class(next_positions[0], -1, (0, 0), numpy.copy(lines), next_positions)]
	for i in range(1000):
		# for line in lines:
		# 	print(''.join(line))
		# print("\n")
		# print(lines)
		# print(len(next_positions))

		for grid_info in grids:
			# if i == 0:
			# 	print(len(next_positions))
			escapees = step_in_grid(grid_info, length, width)
			if len(escapees) != 0:
				# print(i)
				add_grids(grids, escapees, lines, grid_info)
				# print(len(grids))
				# print(escapees)
			# step_in_grid(grid[0], grid[1], length, width)
		if len(grids) == 9:
			break
		# if len(grids) == 9:
		# 	for line in grids[8].grid:
		# print(len(next_positions))
				# print(''.join(line))


		# print(i)
	clear_grids(grids, lines)
	even, uneven = find_step_cycle(grids[0], lines, length, width)


	traversals = 202300
	a_blocks = traversals * 2
	b_blocks_filled = (traversals - 2) * 2
	print(a_blocks, b_blocks_filled)
	b_blocks_unfilled = 4
	c_blocks_filled = 0
	d_blocks_filled = 0
	for i in range(0, traversals, 2):
		d_blocks_filled += i
	for i in range(1, traversals - 1, 2):
		c_blocks_filled += i
	print(c_blocks_filled, d_blocks_filled)
	d_blocks_filled *= 4
	c_blocks_filled *= 4
	
	d_blocks_unfilled = traversals
	c_blocks_unfilled = (traversals - 1)
	
	total_positions = 0
	total_positions = uneven
	total_positions += a_blocks * even
	total_positions += b_blocks_filled * uneven
	total_positions += c_blocks_filled * uneven
	total_positions += d_blocks_filled * even

	step_b_block_unfilled = count_steps(grids[1], lines, 130, length, width)
	print(step_b_block_unfilled)
	total_positions += step_b_block_unfilled * b_blocks_unfilled
	
	print("D")
	step_d_block_unfilled = count_steps(grids[5], lines, 64, length, width)

	print(step_d_block_unfilled)
	total_positions += step_d_block_unfilled * d_blocks_unfilled


	step_d_block_unfilled = count_steps(grids[6], lines, 64, length, width)
	total_positions += step_d_block_unfilled * d_blocks_unfilled
	print(step_d_block_unfilled)



	step_d_block_unfilled = count_steps(grids[7], lines, 64, length, width)
	total_positions += step_d_block_unfilled * d_blocks_unfilled
	print(step_d_block_unfilled)


	step_d_block_unfilled = count_steps(grids[8], lines, 64, length, width)
	total_positions += step_d_block_unfilled * d_blocks_unfilled
	print(step_d_block_unfilled)

	print("C")
	step_c_block_unfilled = count_steps(grids[5], lines, 65 + 130, length, width)
	print(step_c_block_unfilled)
	total_positions += step_c_block_unfilled * c_blocks_unfilled
	step_c_block_unfilled = count_steps(grids[6], lines, 65 + 130, length, width)
	print(step_c_block_unfilled)
	total_positions += step_c_block_unfilled * c_blocks_unfilled
	step_c_block_unfilled = count_steps(grids[7], lines, 65 + 130, length, width)
	print(step_c_block_unfilled)
	total_positions += step_c_block_unfilled * c_blocks_unfilled
	step_c_block_unfilled = count_steps(grids[8], lines, 65 + 130, length, width)
	print(step_c_block_unfilled)
	total_positions += step_c_block_unfilled * c_blocks_unfilled
	# print(step_c_block_unfilled, c_blocks_unfilled)
	# print(step_c_block_unfilled * c_blocks_unfilled)


	# total_positions += step_c_block_unfilled * c_blocks_unfilled
	# print(d_blocks_filled, c_blocks_filled)

	print("answe rlol", total_positions)
	# print(total_positions + 7546)
	# print(total_positions + 7539)

	part1 = 0
	part2 = 0

	# print(f"The answer to part 1 is: {part1}")
	# print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	start = time.time()
	main()
	end = time.time()
	print(end - start)