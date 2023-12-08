class Node:
	def __init__(self, val):
		self.l = None
		self.r = None
		self.v = val

	def add_to_node(val, dir):
		new_node = Node(val)
        

class Tree:
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def add(self, val):
		if not self.root:
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.v:
			if node.l:
				self._add(val, node.l)
			else:
				node.l = Node(val)
		else:
			if node.r:
				self._add(val, node.r)
			else:
				node.r = Node(val)

	def find(self, val):
		if self.root:
			return self._find(val, self.root)

	def _find(self, val, node):
		if val == node.v:
			return node
		elif val < node.v and node.l:
			return self._find(val, node.l)
		elif val > node.v and node.r:
			return self._find(val, node.r)

	def view_tree(self):
		if self.root:
			self._view_tree(self.root)

	def _view_tree(self, node):
		if node:
			self._view_tree(node.l)
			print(node.v, end = " ")
			self._view_tree(node.r)

def make_nodes(lines):

	locations = dict()
    
	for line in lines[2:]:
		node_values = line.split()
		new_node = Node(node_values[0])
		new_node.l = node_values[2][1:4]
		new_node.r = node_values[3][:3]
		locations[node_values[0]] = new_node
		# locations.update({node_values[0], new_node})
		# locations.append([node_values[0], new_node])
	# print(locations)
	return locations

def	get_locations(locations):
	current_locations = list()

	# print (locations)
	for key, value in locations.items():
		if key[-1] == "A":
			current_locations.append(value)
	# print(current_locations)
	return current_locations

def check_if_end(current_locations):

	# print("herte now")
	# print(current_locations)
	# for location in current_locations:
	# 	print(location.v)
	# print("herte now")
	
	for location in current_locations:
		# print(location)
		str = location.v
		# print(str)
		if str[-1] == "Z":
			continue
		else:
			return False
	# print("here")
	return True

def main():
	lines = open("input").readlines()

	locations = make_nodes(lines)
	instructions = lines[0]
	current_locations = get_locations(locations)
	steps = 0
	print(current_locations)
	# print(current_location.v, current_location.l, current_location.r)
	print(instructions)
	while True:
		# print ("lol")
		for char in instructions:
			if check_if_end(current_locations) == True:
				break
			for i, location in enumerate(current_locations):
				if char == "L":
					current_locations[i] = locations[current_locations[i].l]
				elif char == "R":
					current_locations[i] = locations[current_locations[i].r]
			if char == "\n":
				break
			steps += 1
		# break 
			# if current_location.v == "ZZZ":
				# break
		# for location in current_locations:
		# 	print(location.v)
		if check_if_end(current_locations) == True:
				break
		# if steps == 6:
		# 	break
	# for location in current_locations:
	# 	print(location.v)
	# print(current_location.v)
	print(steps)

if __name__ == "__main__":
	main()