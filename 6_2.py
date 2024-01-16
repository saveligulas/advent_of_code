from FileReader import read_lines


lines = read_lines("./input/input_6_2")


def get_numbers_from_line(line):
    words = line.split()
    numbers = list(int(num) for num in words[1:])
    return numbers


def get_lowest_or_highest_button_press_time(time, record, lowest=True):
    for button_press_time in (range(time + 1) if lowest else range(time, -1, -1)):
        speed = button_press_time
        remaining_time = time - button_press_time
        distance_traveled = remaining_time * speed
        if distance_traveled > record:
            return button_press_time


def get_result():
    time = get_numbers_from_line(lines[0])[0]
    distance = get_numbers_from_line(lines[1])[0]

    lowest = get_lowest_or_highest_button_press_time(time, distance)
    highest = get_lowest_or_highest_button_press_time(time, distance, False)
    return abs(lowest - highest) + 1

print(get_result())
