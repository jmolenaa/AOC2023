

def main():
	lines = open("input").readlines()
	galaxies = list()
	for i, line in enumerate(lines):
		lines[i] = line.strip()



	inserted = 0
	for i, line in enumerate(lines):
		if inserted == 1:
			inserted = 0
			continue
		if line == len(line) * line[0]:
			lines.insert(i, line)
			inserted = 1
			# print(line)
			# print("hey")
	inserted = 0
	print (len(lines[0]))
	i = 0
	while i < len(lines[0]):
		if inserted == 1:
			inserted = 0
			i += 1
			continue
		same = 1
		# print("next", i)
		for j in range(len(lines)):
			print (lines[0][i], lines[j][i])
			if lines[0][i] != lines[j][i]:
				same = 0
				break
		if same == 1:
			# print("HIIIII")
			for j in range(len(lines)):
				lines[j] = lines[j][:i] + "." + lines[j][i:]
				inserted = 1
		i += 1


	for i, line in enumerate(lines):
		for j, char in enumerate(line):
			if char == "#":
				galaxies.append([j, i])
	
	for line in lines:
		print(line)
	print(galaxies)

	result = 0
	for i, galaxy in enumerate(galaxies):
		j = i + 1
		print("hi")
		while j < len(galaxies):
			result += abs(galaxy[0] - galaxies[j][0]) + abs(galaxy[1] - galaxies[j][1])
			j += 1
	print(result)
			



	




if __name__ == "__main__":
	main()