from copy import copy

from FileReader import read_lines


lines = read_lines("./input/test_input.txt")
matrix = []
result = 0

for line in lines:
    matrix_line = []
    for char in line:
        matrix_line.append(char)
    matrix.append(matrix_line)
print(matrix)


def is_special_symbol(c):
    special_symbols = ["#", "-", "+", "@", "$", "/", "*", "&", "=", "%"]
    return c in special_symbols


def adjacent_symbol_exists(current_line, indexes: list, matrixx):
    special_symbol_found = False
    start_index = indexes[0]
    end_index = indexes[-1]
    can_look_top = current_line > 0
    can_look_bottom = current_line + 1 != len(matrixx)
    can_look_left = start_index > 0
    can_look_right = end_index + 1 != len(matrixx[current_line])
    right_adjustment = 2 if can_look_right else 1

    if can_look_top:
        top_checklist = matrixx[current_line - 1][start_index - (1 if can_look_left else 0):end_index + right_adjustment]
        special_symbol_found = any(is_special_symbol(top_char) for top_char in top_checklist)
    if can_look_bottom and not special_symbol_found:
        bottom_checklist = matrixx[current_line + 1][start_index - (1 if can_look_left else 0):end_index + right_adjustment]
        special_symbol_found = any(is_special_symbol(bottom_char) for bottom_char in bottom_checklist)

    if not special_symbol_found:
        if can_look_right:
            special_symbol_found = is_special_symbol(matrixx[current_line][end_index + 1])
        if can_look_left and not special_symbol_found:
            special_symbol_found = is_special_symbol(matrixx[current_line][start_index - 1])

    return special_symbol_found

for line_index in range(len(matrix)):
    matrix_line = matrix[line_index]
    num_found = False
    for i in range(len(matrix_line)):
        symbol = matrix_line[i]
        if symbol.isdigit() and not num_found:
            num_found = True
            num_indexes = [i]
            for k in range(i + 1, len(matrix_line)):
                if matrix_line[k].isdigit():
                    num_indexes.append(k)
                else:
                    break
            if adjacent_symbol_exists(line_index, num_indexes, matrix):
                counter = 0
                number_to_add = 0
                for index in reversed(num_indexes):
                    number_to_add += int(matrix_line[index]) * (10 ** counter)
                    counter += 1
                result += number_to_add
                print(number_to_add)
        if not symbol.isdigit():
            num_found = False


print(result)
