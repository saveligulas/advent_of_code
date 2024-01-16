from FileReader import read_lines


lines = read_lines("./input/input_4_1.txt")
result = 0


for line in lines:
    line_words = line.split()
    justified_list = " ".join(line_words)
    cut_card_part = justified_list.split(":")[1]
    winning_numbers = list(int(num) for num in cut_card_part.split(" | ")[0].lstrip().split(" "))
    numbers_ihave = list(int(num) for num in cut_card_part.split(" | ")[1].lstrip().split(" "))
    line_result = 0
    for winning_num in winning_numbers:
        if winning_num in numbers_ihave:
            if line_result == 0:
                line_result += 1
            else:
                line_result *= 2
    result += line_result

print(result)
