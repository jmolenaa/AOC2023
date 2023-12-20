from collections import defaultdict
import numpy

class	flip_flop:
	def	__init__(self, name, outputs):
		self.state = 0
		self.name = name
		self.outputs = outputs
	def __str__(self):
		return f"name is {self.name}, state is {self.state}, outputs: {self.outputs}"
	def __repr__(self):
		return f"name is {self.name}, state is {self.state}, outputs: {self.outputs}"


class	conjunction:
	def __init__(self, name, outputs, inputs_dict):
		self.name = name
		self.outputs = outputs
		self.inputs_dict = inputs_dict
	def __str__(self):
		return f"name is {self.name}, outputs: {self.outputs}, inputs: {self.inputs_dict}"
	def __repr__(self):
		return f"name is {self.name}, outputs: {self.outputs}, inputs: {self.inputs_dict}"


class	broadcaster:
	def __init__(self, name, outputs):
		self.name = name
		self.outputs = outputs
	def __str__(self):
		return f"name is {self.name}, outputs: {self.outputs}"
	def __repr__(self):
		return f"name is {self.name}, outputs: {self.outputs}"


class	button:
	def __init__(self, name, outputs):
		self.name = name
		self.outputs = outputs
	def __str__(self):
		return f"outputs: {self.outputs}"
	def __repr__(self):
		return f"outputs: {self.outputs}"



def main():
	with open("input") as file:
		lines = file.read().split("\n")


	modules = defaultdict(int)
	modules["button"] = ["button", button("button", ["broadcaster"]), 0]
	for line in lines:
		name, arrow, outputs = line.split(" ", 2)
		if name[0] == "%":
			modules[name[1:]] = ["flip", flip_flop(name[1:], outputs.split(", ")), 1]
		elif name[0] == "&":
			modules[name[1:]] = ["con", conjunction(name[1:], outputs.split(", "), dict()), 1]
		else:
			modules[name] = ["broadcaster", broadcaster(name, outputs.split(", ")), 0]


	for key, value in list(modules.items()):
		for output in value[1].outputs:
			if modules[output] != 0 and modules[output][0] == "con":
				modules[output][1].inputs_dict[key] = 0


	low = 0
	high = 0
	conjections = {"vr" : 0, "nl": 0, "lr": 0, "gt": 0}
	i = 0
	while True:

		i += 1
		if i == 1001:
			part1 = low * high
		if i > 1000 and not 0 in list(conjections.values()):
			break


		next_module_queue = list()
		module_queue = [modules["button"]]

		while module_queue or next_module_queue:

			if not module_queue:
				module_queue = next_module_queue.copy()
				next_module_queue.clear()
				
			module = module_queue.pop()

			low += len(module[1].outputs) * abs(module[2] - 1)
			high += len(module[1].outputs) * module[2]

			for output in module[1].outputs:

				output_module = modules[output]
				singal = module[2]

				if output_module == 0:
					continue

				elif output_module[0] == "flip" and singal == 0:
					output_module[1].state = (output_module[1].state + 1) % 2
					output_module[2] = output_module[1].state
					next_module_queue.append(output_module)

				elif output_module[0] == "con":
					output_module[1].inputs_dict[module[1].name] = singal
					signal = 0
					for value in output_module[1].inputs_dict.values():
						if value == 0:
							signal = 1
							break
					output_module[2] = signal
					next_module_queue.append(output_module)

				elif output_module[0] == "broadcaster":
					next_module_queue.append(output_module)
				
				if output in list(conjections.keys()) and output_module[2] == 1:
					if conjections[output] == 0:
						conjections[output] = i


	part2 = numpy.prod(list(conjections.values()))


	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	main()