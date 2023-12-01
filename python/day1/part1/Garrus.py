fd = open("input")
count = 0

for line in fd:
    for i in line:
        if i.isdigit():
            count += int(i) * 10
            break
    for i in reversed(line):
        if i.isdigit():
            count += int(i)
            break
print(count)
