from FileReader import read_lines


lines = read_lines('./input/test_input.txt')
numbers = []
result = 0
numbers_as_words = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
}

for line in lines:
    num_pair = []
    word_was_checked = False
    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            word_was_checked = False
            num_pair.append(char)
            break
        if char.isalpha() and not word_was_checked:
            word = [char]
            word_was_checked = True
            for c in line[i + 1:]:
                if c.isdigit():
                    break
                if c.isalpha():
                    word.append(c)
            word = "".join(w for w in word)
            number_found = (99999999, 0, 0)
            for key in numbers_as_words.keys():
                if key in word:
                    index = word.find(key)
                    if index < number_found[0]:
                        number_found = (index, key)
            if len(number_found) == 2:
                num_pair.append(numbers_as_words[number_found[1]])
                break

    word_was_checked = False
    for index, char in enumerate(reversed(line)):
        if char.isdigit():
            num_pair.append(char)
            word_was_checked = False
            break
        if char.isalpha() and not word_was_checked:
            word = [char]
            word_was_checked = True
            for c in reversed(line[:index - 1]):
                if c.isdigit():
                    break
                if c.isalpha():
                    word.append(c)
            word = "".join(w for w in reversed(word))
            number_found = (-1, 0, 0)
            for key in numbers_as_words.keys():
                if key in word:
                    index = word.find(key)
                    if index > number_found[0]:
                        number_found = (index, key)
            if len(number_found) == 2:
                num_pair.append(numbers_as_words[number_found[1]])
                break

    numbers.append(num_pair)
    print(num_pair)


for pair in numbers:
    result += (int(pair[0]) * 10) + int(pair[1])


print(result)