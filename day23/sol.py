import numpy
import time
from array import array

def	part1_sol(route, routes):
	position, grid, steps = route
	y, x = position
	fork = 0
	grid[y][x] = "O"
	if grid[y][x + 1]in ".>":
		if fork == 0:
			routes.append(((y, x + 1), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y, x + 1), grid.copy(), steps + 1))
	if grid[y][x - 1]in ".<":
		if fork == 0:
			routes.append(((y, x - 1), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y, x - 1), grid.copy(), steps + 1))
	if grid[y + 1][x]in ".v":
		if fork == 0:
			routes.append(((y + 1, x), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y + 1, x), grid.copy(), steps + 1))
	if grid[y - 1][x]in ".^":
		if fork == 0:
			routes.append(((y - 1, x), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y - 1, x), grid.copy(), steps + 1))


def	part2_sol(route, routes):
	position, grid, steps = route
	y, x = position
	fork = 0
	grid[y][x] = "O"
	if grid[y][x + 1]in ".><v^":
		if fork == 0:
			routes.append(((y, x + 1), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y, x + 1), grid.copy(), steps + 1))
	if grid[y][x - 1]in ".<>v^":
		if fork == 0:
			routes.append(((y, x - 1), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y, x - 1), grid.copy(), steps + 1))
	if grid[y + 1][x]in ".v<>^":
		if fork == 0:
			routes.append(((y + 1, x), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y + 1, x), grid.copy(), steps + 1))
	if grid[y - 1][x]in ".^v<>":
		if fork == 0:
			routes.append(((y - 1, x), grid, steps + 1))
			fork = 1
		else:
			routes.append(((y - 1, x), grid.copy(), steps + 1))
	# print(grid)
	

def main():
	with open("input") as file:
		lines = file.read().split("\n")
	numpy.set_printoptions(linewidth=numpy.inf)
	for i, line in enumerate(lines):
		lines[i] = array('u', line)
	lines = numpy.array(lines)
	lines[0][1] = "S"
	
	grid = lines.copy()
	routes = [((1, 1), grid, 1)]
	steps = set()
	while routes:
		route = routes.pop()
		if route[0][0] == len(lines) - 1:
			steps.add(route[2])
			continue
		part1_sol(route, routes)
	
	part1 = max(steps)
	print(f"The answer to part 1 is: {part1}")
	print("Answer to part2 will take a while to print "
	   "but I cant be bothered getting it nice and fast"
	   "\nit will pop up in 30-40 minutes lol")
	time.sleep(10)
	
	
	routes = [((1, 1), lines, 1)]
	steps = set()
	while routes:
		route = routes.pop()
		if route[0][0] == len(lines) - 1:
			steps.add(route[2])
			print(max(steps))
			continue
		part2_sol(route, routes)

	part2 = max(steps)

	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()