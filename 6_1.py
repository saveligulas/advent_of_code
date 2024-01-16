from FileReader import read_lines


lines = read_lines("./input/input_6_1")


def get_numbers_from_line(line):
    words = line.split()
    numbers = list(int(num) for num in words[1:])
    return numbers


def get_all_times_with_different_button_press_time(time):
    results = []
    for button_press_time in range(time + 1):
        distance_traveled = 0
        speed = 0
        for run_time in range(1, time + 1):
            if run_time <= button_press_time != 0:
                speed += 1
            else:
                distance_traveled += speed
        results.append(distance_traveled)
    return results


def get_amount_of_record_times(results, record):
    amount = 0
    for result in results:
        if result > record:
            amount += 1
    return amount


def get_result():
    times = get_numbers_from_line(lines[0])
    records = get_numbers_from_line(lines[1])
    result = 1

    for i in range(len(times)):
        time = times[i]
        record = records[i]
        combinations = get_all_times_with_different_button_press_time(time)
        result *= get_amount_of_record_times(combinations, record)

    return result


print(get_result())