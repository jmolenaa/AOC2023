def	calculate_next_point(info, part, prev_pt):
	# setting up dictionaries with directions as key values and vectors for the coordinate direction
	# second dictionary is for translating last number of hexadecimal to a direciton for part2

	directions = {"R" : (0, 1), "L" : (0, -1), "U" : (-1, 0), "D": (1, 0)}
	directions_dict = {0 : "R", 1 : "D", 2 : "L", 3 : "U"}

	if part == 2:
		distance = int(info[2][2:7], 16)
		direction = directions_dict[int(info[2][7])]
	else:
		distance = int(info[1])
		direction = info[0]
	
	return (prev_pt[0] + directions[direction][0] * distance, prev_pt[1] + directions[direction][1] * distance)


def	calculate_area(lines, part):


	# will calculate the target area by using shoelace formula and Picks Theorem
	previous_point = (0, 0)
	two_area = 0
	boundary_points = 0
	for line in lines:

		info = line.split()

		next_point = calculate_next_point(info, part, previous_point)

		# calculations for shoelace formula, for calculating the area we multiply the appropiate coordinates of
		# two adjacent points and substract from that the other multiplication
		# so y0 * x1 - x0 * y1
		# we add this to the accumulated area, in the end this gives us 2 * the area
		two_area += previous_point[1] * next_point[0] - previous_point[0] * next_point[1]

		# for Picks theorem we will need all the integer boundary points of our shape
		# so we need all the points between two points, so f.e.
		# between (0,0) and (0,6) we have (0,1),(0,2),(0,3),(0,4),(0,5),(0,6) - 6 points
		# we calculate by substracting x0 - x1 plus y0 - y1, this works cause every line is perpendicular
		boundary_points += abs(previous_point[0] - next_point[0] + previous_point[1] - next_point[1])
		
		previous_point = next_point

	# Picks theroem to calculate the interior integer points of our shape
	# two_area might be negative so we take absolute value
	interior_points = abs(two_area) / 2 - boundary_points / 2 + 1
	area = interior_points + boundary_points
	print(f"Answer to part {part} is: {round(area)}")


def main():
	with open("input") as file:
		lines = file.read().split("\n")
	
	calculate_area(lines, 1)
	calculate_area(lines, 2)


if __name__ == "__main__":
	main()