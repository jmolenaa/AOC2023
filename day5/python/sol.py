class map:
	def __init__(self, s_ran, d_ran, ran):
		self.s_ran = s_ran
		self.d_ran = d_ran
		self.ran = ran


def add_to_map():
	ranges = line.split()
	current_map.append(map(ranges[1], ranges[0], ranges[2]))

def convert_items():
	# change = 0
	for i, item in enumerate(items):
		for m in current_map:
			if int(item) - int(m.s_ran) < int(m.ran) and int(item) - int(m.s_ran) > 0:
				# print(item, m.s_ran, m.d_ran, m.ran)
				# print("LOL")
				items[i] = int(m.d_ran) + int(item) - int(m.s_ran)
				# print(items[i])
				break
	
	# return items



lines = open("input").readlines()
items = lines[0]
items = items.split()
del(items[0])
# print(items)

current_map=list()

for i, line in enumerate(lines):
	if i == 0 or i == 1:
		continue
	elif line == "\n":

		convert_items()
		current_map.clear()
	elif line[0].isdigit():
		add_to_map()
		# print("DIGIT" ,line)
	# print(line)
convert_items()

print(items)
print(min(items))