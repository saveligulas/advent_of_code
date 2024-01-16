import re

from FileReader import read_lines

lines = read_lines("./input/input_2_1.txt")
result = 0
input = {
    "r": 12,
    "g": 13,
    "b": 14
}


for line_number in range(len(lines)):
    game_is_compatible = True
    game_id = line_number + 1
    data = lines[line_number].split(":")[1].replace(" ", "").split(";")
    data_compressed = []
    for i in range(len(data)):
        split = data[i].split(",")
        for k in range(len(split)):
            word = split[k]
            index = 0
            for c in range(len(word)):
                if word[c].isalpha():
                    index = c + 1
                    break
            split[k] = word[:index]
        data_compressed.append(split)

    for game_set in data_compressed:
        for dice_throw in game_set:
            color = dice_throw[-1]
            match = re.match(r"^(\d+)", dice_throw)
            extracted_number = int(match.group(1))
            if input[color] < extracted_number:
                game_is_compatible = False

    if game_is_compatible:
        result += game_id


print(result)
