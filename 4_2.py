from FileReader import read_lines


lines = read_lines("./input/input_4_1.txt")


def get_number_of_winning_numbers(card):
    line_words = card.split()
    justified_list = " ".join(line_words)
    cut_card_part = justified_list.split(":")[1]
    winning_numbers = list(int(num) for num in cut_card_part.split(" | ")[0].lstrip().split(" "))
    numbers_ihave = list(int(num) for num in cut_card_part.split(" | ")[1].lstrip().split(" "))
    line_result = 0
    for winning_num in winning_numbers:
        if winning_num in numbers_ihave:
            line_result += 1
    return line_result


def get_won_cards(index, winning_numbers):
    cards = []
    for i in range(index + 1, index + 1 + winning_numbers):
        cards.append(i)
    return cards


def get_next_card(text, card_dict=None, index=0):
    if card_dict is None:
        card_dict = {key: 1 for key in range(0, len(text))}
    if index == len(text) - 1:
        return card_dict
    winning_numbers = get_number_of_winning_numbers(text[index])
    cards_won = get_won_cards(index, winning_numbers)
    for card in cards_won:
        card_dict[card] += 1 * card_dict[index]
    return get_next_card(text, card_dict, index + 1)


def count_all_won_cards(card_dict):
    print(card_dict)
    result = 0
    for key in card_dict.keys():
        result += card_dict[key]
    return result


print(count_all_won_cards(get_next_card(lines)))