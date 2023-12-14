def	GetDistance(timeheld, racetime):
	speed = timeheld
	distance = (racetime - timeheld) * speed
	return distance


# exit condition of binary search is when the distance covered for the time we have beats the previous record
# and the distance covered for time -1 seconds doesn't beat the record, which means we found first time to beat
def	BinarySearch(racetime, distance_to_beat):
	low = 0
	high = racetime
	while low <= high:
		mid = low + int((high - low) / 2)
		distance_mid = GetDistance(mid, racetime)
		if distance_mid > distance_to_beat and GetDistance(mid - 1, racetime) <= distance_to_beat:
			return mid
		elif distance_mid > distance_to_beat:
			high = mid - 1
		else:
			low = mid + 1


# uses binary search to find first time to beat the record, then substracts that time twice
# from the total amount of possible times, which is the racetime + 1 (accounting for 0 seconds holding time)
def FindAmountOfWays(racetime, distance_to_beat):
	first_beat_time = BinarySearch(racetime, distance_to_beat)
	amount_of_ways = racetime + 1 - first_beat_time * 2
	return amount_of_ways


def main():
	lines = open("input").readlines()


	times_part1 = [int(time) for time in lines[0].split()[1:]]
	distances_part1 = [int(time) for time in lines[1].split()[1:]]

	# distances_part1 = list(map(int, distances_part1))
	resultpart1 = 1

	# looping over times and finding the amount of ways to beat record, then multiplying the result
	for i in range(len(times_part1)):
		resultpart1 *= FindAmountOfWays(times_part1[i], distances_part1[i])


	# joining times into one string for part 2
	time_part2 = ''.join(map(str, times_part1))
	distance_part2 = ''.join(map(str, distances_part1))

	resultpart2 = FindAmountOfWays(int(time_part2), int(distance_part2))


	print("Answer to part 1: ", resultpart1)
	print("Answer to part 2: ", resultpart2)


if __name__ == "__main__":
	main()