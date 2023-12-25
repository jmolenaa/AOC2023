from sympy import var, Eq, solve
import time

def main():

	with open("input") as file:
		lines = file.read().split("\n")

	part1 = 0
	part2 = 0

	hailstones = list()
	for line in lines:
		position = line.split(" @ ")[0].split(", ")
		position = list(map(int, position))
		velocity = line.split(" @ ")[1].split(", ")
		velocity = list(map(int, velocity))

		hailstones.append((position, velocity))



	for i, hailstoneA in enumerate(hailstones):
		for hailstoneB in hailstones[i + 1:]:
			posA, vectorA = hailstoneA
			posB, vectorB = hailstoneB

			coeficientA = vectorA[1] / vectorA[0]
			coeficientB = vectorB[1] / vectorB[0]

			if coeficientA - coeficientB == 0:
				continue
			x = (posA[0] * coeficientA - posB[0] * coeficientB + posB[1] - posA[1]) / (coeficientA - coeficientB)
			y = coeficientA * (x - posA[0]) + posA[1]

			timeA = (x - posA[0]) / vectorA[0]
			timeB = (x - posB[0]) / vectorB[0]

			if x >= 200000000000000 and x <= 400000000000000 and y >= 200000000000000 and y <= 400000000000000:
				if timeA > 0 and timeB > 0:
					part1 += 1

	rock_x, rock_y, rock_z = var("x"), var("y"), var("z")
	rock_vx, rock_vy, rock_vz = var("vx"), var("vy"), var("vz")

	equations = list()
	for i, hailstone in enumerate(hailstones):
		hail_x, hail_y, hail_z = hailstone[0]
		hail_vx, hail_vy, hail_vz = hailstone[1]

		# time = str(i)
		time = "t" + str(i)
		# print(time)
		exec(f'{time} = var("{time}")')

		equations.append(Eq(eval(f"rock_x + rock_vx * {time}"), eval(f"hail_x + hail_vx * {time}")))
		equations.append(Eq(eval(f"rock_y + rock_vy * {time}"), eval(f"hail_y + hail_vy * {time}")))
		equations.append(Eq(eval(f"rock_z + rock_vz * {time}"), eval(f"hail_z + hail_vz * {time}")))
		# print(equations)
		if i > 1:
			break


	solution = solve(equations)[0]
	part2 = solution[rock_x] + solution[rock_y] + solution[rock_z]




	print(f"The answer to part 1 is: {part1}")
	print(f"The answer to part 2 is: {part2}")

if __name__ == "__main__":
	start = time.time()

	main()
	end = time.time()
	print(end - start)
