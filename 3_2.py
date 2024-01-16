from FileReader import read_lines

lines = read_lines("./input/input_3_1.txt")
matrix = []
result = 0

for line in lines:
    line_to_search = []
    for char in line:
        line_to_search.append(char)
    matrix.append(line_to_search)


def number_exists(characters):
    characters = list(characters)
    for i in range(len(characters)):
        if characters[i].isdigit():
            return True


def get_number(line, start_index):
    for i in range(start_index, len(line)):
        if line[i].isdigit():
            return i


def only_one_number(checklist):
    number_found = False
    numbers_found = 0
    for symbol in checklist:
        if symbol.isdigit() and not number_found:
            number_found = True
            numbers_found += 1
        if not symbol.isdigit():
            number_found = False
    if numbers_found == 1:
        return True
    return False


def two_adjacent_numbers_exist(current_line, star_index, matrixx):
    can_look_top = current_line > 0
    can_look_bottom = current_line + 1 != len(matrixx)
    can_look_left = star_index > 0
    can_look_right = star_index + 1 != len(matrixx[current_line])
    right_adjustment = 2 if can_look_right else 1
    part_number_indexes = []

    start_index = star_index - (1 if can_look_left else 0)
    end_index = star_index + right_adjustment

    if can_look_top:
        top_checklist = matrixx[current_line - 1][start_index:end_index]
        if number_exists(top_checklist):
            part_number_indexes.append((get_number(matrixx[current_line - 1], start_index), current_line - 1))
            if not only_one_number(top_checklist):
                part_number_indexes.append((get_number(matrixx[current_line - 1], start_index + 1), current_line - 1))

    if can_look_bottom:
        bottom_checklist = matrixx[current_line + 1][start_index:end_index]
        if number_exists(bottom_checklist):
            part_number_indexes.append((get_number(matrixx[current_line + 1], start_index), current_line + 1))
            if not only_one_number(bottom_checklist):
                part_number_indexes.append((get_number(matrixx[current_line + 1], start_index + 1), current_line + 1))

    if can_look_right:
        char_to_check = matrixx[current_line][star_index + 1]
        if number_exists(char_to_check):
            part_number_indexes.append((star_index + 1, current_line))
    if can_look_left:
        char_to_check = matrixx[current_line][star_index - 1]
        if number_exists(char_to_check):
            part_number_indexes.append((star_index - 1, current_line))
    if len(part_number_indexes) == 2:
        return part_number_indexes
    return None


def get_entire_number_from_index(current_line, index, matrixx):
    line_to_search = matrixx[current_line]
    numbers_found = []
    number_found = False

    for i in range(len(line_to_search)):
        symbol = line_to_search[i]
        if symbol.isdigit() and not number_found:
            number_found = True
            num_indexes = [i]
            for k in range(i + 1, len(line_to_search)):
                if line_to_search[k].isdigit():
                    num_indexes.append(k)
                else:
                    break
            numbers_found.append(num_indexes)
        if not symbol.isdigit():
            number_found = False
    for num_set in numbers_found:
        if index in num_set:
            counter = 0
            number_found = 0
            for index in reversed(num_set):
                number_found += int(line_to_search[index]) * (10 ** counter)
                counter += 1
            return number_found


for line_index in range(len(matrix)):
    line_to_search = matrix[line_index]
    num_found = False
    for i in range(len(line_to_search)):
        symbol = line_to_search[i]
        if symbol == "*":
            indexes_to_check = two_adjacent_numbers_exist(line_index, i, matrix)
            if indexes_to_check is not None:
                num_one = get_entire_number_from_index(indexes_to_check[0][1], indexes_to_check[0][0], matrix)
                num_two = get_entire_number_from_index(indexes_to_check[1][1], indexes_to_check[1][0], matrix)
                result += num_one * num_two


print(result)