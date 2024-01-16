def lowest_num(numbers):
    lowest_num = 0
    for i in range(1, len(numbers)):
        if lowest_num > numbers[i]:
            lowest_num = i
