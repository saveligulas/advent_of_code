from FileReader import read_lines


lines = read_lines('./input/input_1_1.txt')
numbers = []
result = 0

for line in lines:
    num_pair = []
    for char in line:
        if char.isdigit():
            num_pair.append(char)
            break
    for char in reversed(line):
        if char.isdigit():
            num_pair.append(char)
            break
    numbers.append(num_pair)


for pair in numbers:
    result += (int(pair[0]) * 10) + int(pair[1])


print(result)
