fd = open("input")
count = 0
numbers = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
found_word = 0


def find_word():
    for k, number in enumerate(numbers):
        if line.find(number, i, i + len(number)) != -1:
            return k + 1
    return -1


def find_reverse():
    for k, number in enumerate(numbers):
        reversed_number = number[::-1]
        if line[::-1].strip("\n").find(reversed_number, i, i + len(number)) != -1:
            return k + 1
    return -1


for line in fd:
    for i, j in enumerate(line):
        if j.isdigit():
            count += int(j) * 10
            break
        found_word = find_word()
        if found_word != -1:
            count += found_word * 10
            break
    for i, j in enumerate(reversed(line)):
        if j.isdigit():
            count += int(j)
            break
        found_word = find_reverse()
        if found_word != -1:
            count += found_word
            break
print(count)
