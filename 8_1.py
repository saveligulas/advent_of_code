import sys

from FileReader import read_lines

sys.setrecursionlimit(100000)

lines = read_lines("./input/input_8_1.txt")


def get_instruction_and_start():
    instruction = ""
    start = 1
    for line in lines:
        if line is None or line == '':
            break
        instruction += line
        start += 1
    return instruction, start


def get_values(start):
    value_lib = {}
    for i in range(start, len(lines)):
        data = lines[i].split()[2] + " " + lines[i].split()[3]
        split_data = data[1:-1].split(', ')
        value_lib[lines[i].split()[0]] = tuple(split_data)
    return value_lib


def convert_input(inp):
    if inp == "L":
        return 0
    if inp == "R":
        return 1
    return -1


def get_next_value(lib, instructions, index=0, val="AAA", counter=0):
    lr = convert_input(instructions[index])
    val = lib[val][lr]
    counter += 1
    if val == "ZZZ":
        return counter
    return get_next_value(lib, instructions, index + 1 if index < len(instructions) - 1 else 0, val, counter)


def get_shortest_path():
    instructions = get_instruction_and_start()[0]
    lib = get_values(get_instruction_and_start()[1])
    print(lib)
    print(instructions)
    return get_next_value(lib, instructions)


def get_shortest_path_non_recursive():
    instructions = get_instruction_and_start()[0]
    lib = get_values(get_instruction_and_start()[1])
    current_val = "AAA"
    counter = 0
    while current_val != "ZZZ":
        for inp in instructions:
            lr = convert_input(inp)
            current_val = lib[current_val][lr]
            counter += 1
            if current_val == "ZZZ":
                break
    return counter


print(get_shortest_path_non_recursive())
