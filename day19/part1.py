class	Part:
	def __init__(self, x, m, a, s):
		self.x = x
		self.m = m
		self.a = a
		self.s = s
	def __str__(self):
		return f"{self.x}, {self.m}, {self.a}, {self.s}"

def	check_if_accepted(part, workspace_dict):
	current_workspace = "in"
	while True:
		conditions = workspace_dict[current_workspace]
		for condition in conditions:
			if 
			print (condition)
		break

def main():
	with open("test_case") as file:
		workspaces, parts = file.read().split("\n\n")
	workspaces = workspaces.split("\n")
	workspace_dict = dict()
	for workspace in workspaces:
		workspace = workspace.strip("}")
		key, value = workspace.split("{")
		value = value.split(",")
		workspace_dict[key] = value

	parts = parts.split("\n")
	for part in parts:
		part = part.strip("}{")
		part = part.split(",")
		part = Part(part[0][2:], part[1][2:], part[2][2:], part[3][2:])
		check_if_accepted(part, workspace_dict)
		print(part)

if __name__ == "__main__":
	main()