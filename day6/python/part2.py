import re

lines = open("input").readlines()

times = lines[0].split()
distances = lines[1].split()

del(times[0])
del(distances[0])
print(times)
print(distances)
count = 0
result = 1


for i in range(len(times)):
	count = 0
	for j in range(int(times[i]) + 1):
		speed = j
		distance = (int(times[i]) - j) * speed
		if distance > int(distances[i]):
			result = int(times[i]) - 2 * j + 1
			print(result)
			break
			count += 1
		print(count)
	# print(count)
	result *= count
	# print(result)
	# print("NEW")
# print(result)



