from copy import copy
from functools import cmp_to_key

from FileReader import read_lines

lines = read_lines("./input/input_7_1.txt")


def get_hand_and_bid(line):
    hand = line.split(" ")[0]
    bid = line.split(" ")[1]
    bid = int(bid)
    val = get_hand_value(hand)
    return hand, bid, val


def get_jokers(hand):
    amount = 0
    for card in hand:
        if card == 0:
            amount += 1
    return amount


def get_card_value(elem):
    lib = {
        '1': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'J': 0, # 10
        'Q': 11,
        'K': 12,
        'A': 13
    }

    if elem in lib.keys():
        return lib[elem]
    else:
        return -1


def convert_hand_to_int(hand):
    converted_hand = list(get_card_value(value) for value in hand)
    converted_hand.sort()
    return converted_hand


def convert_hand_to_int_no_sort(hand):
    converted_hand = list(get_card_value(value) for value in hand)
    return converted_hand


def check_all_equal(hand):
    return all(element == hand[0] for element in hand)


def check_all_equal_jokers(hand):
    amount = get_jokers(hand)
    if amount == 0:
        return check_all_equal(hand)
    else:
        last = hand[-1]
        for card in reversed(hand):
            if card == last:
                amount += 1
        if amount == 5:
            return True
        return False


def check_four(hand):
    if hand[0] == hand[1]:
        hand_copy = copy(hand)
        hand_copy.pop()
        return check_all_equal(hand_copy)
    if hand[-1] == hand[-2]:
        hand_copy = copy(hand)
        hand_copy.pop(0)
        return check_all_equal(hand_copy)
    return False


def check_four_jokers(hand):
    amount = get_jokers(hand)
    if amount == 0:
        return check_four(hand)
    first_val = 0
    last_val = 0
    for card in hand:
        if card > first_val == 0:
            first_val = card
    for rcard in reversed(hand):
        if rcard > last_val == 0:
            last_val = rcard
    last_amount = 0
    first_amount = 0
    for c in hand:
        if c == first_val:
            first_amount += 1
        if c == last_val:
            last_amount += 1
    if (amount + last_amount or amount + first_amount) == 4:
        return True
    return False


def check_full_house(hand):
    split_one = hand[2:]
    remaining_one = hand[:2]
    split_two = hand[3:]
    remaining_two = hand[:3]

    if check_all_equal(split_one) and check_all_equal(remaining_one) or check_all_equal(split_two) and check_all_equal(remaining_two):
        return True

    return False


def check_three(hand):
    for element in hand:
        count = 0
        for element_b in hand:
            if element == element_b:
                count += 1
            if count == 3:
                return True
    return False


def check_two_pairs(hand):
    pairs = 0
    used_elements = []
    for element in hand:
        count = 0
        if element not in used_elements:
            for element_b in hand:
                if element == element_b:
                    count += 1
                if count == 2:
                    used_elements.append(element)
                    pairs += 1
                    break
    return pairs == 2


def check_one_pair(hand):
    for element in hand:
        count = 0
        for element_b in hand:
            if element == element_b:
                count += 1
            if count == 2:
                return True
    return False


def get_hand_value(hand):
    conv_hand = convert_hand_to_int(hand)
    if check_all_equal(conv_hand):
        return 7
    if check_four(conv_hand):
        return 6
    if check_full_house(conv_hand):
        return 5
    if check_three(conv_hand):
        return 4
    if check_two_pairs(conv_hand):
        return 3
    if check_one_pair(conv_hand):
        return 2

    return 1


def check_equal_hands(hand_a, hand_b):
    conv_hand_a = convert_hand_to_int_no_sort(hand_a[0])
    conv_hand_b = convert_hand_to_int_no_sort(hand_b[0])
    for i in range(len(conv_hand_a)):
        if conv_hand_a[i] > conv_hand_b[i]:
            return 1
        if conv_hand_a[i] < conv_hand_b[i]:
            return -1
    return 0


def calculate_table_value():
    hand_bids = []
    for line in lines:
        hand_bids.append((get_hand_and_bid(line)))
    ordered_by_rank = sorted(hand_bids, key=lambda x: x[2])
    sorted_hand_replacements = {}
    same_rank_found = False
    for i in range(len(ordered_by_rank)):
        hand = ordered_by_rank[i]
        hand_val = get_hand_value(hand[0])
        counter = i + 1
        next_hands = [hand]
        if i < len(ordered_by_rank) - 1:
            if ordered_by_rank[counter][2] == hand_val:
                next_hands.append(ordered_by_rank[counter])
            while counter + 1 < len(ordered_by_rank) and ordered_by_rank[counter + 1][2] == hand_val:
                counter += 1
                next_hands.append(ordered_by_rank[counter])
            if len(next_hands) > 1 and not same_rank_found:
                sorted_hands = sorted(next_hands, key=cmp_to_key(check_equal_hands))
                sorted_hand_replacements.update({i: (sorted_hands, counter)})
                same_rank_found = True
            if len(next_hands) == 1:
                same_rank_found = False
    final_list = []
    next_update = -1
    for k in range(len(ordered_by_rank)):
        if k in sorted_hand_replacements.keys():
            for hand in sorted_hand_replacements[k][0]:
                final_list.append(hand)
            next_update = sorted_hand_replacements[k][1]
        if k > next_update and k not in sorted_hand_replacements.keys():
            final_list.append(ordered_by_rank[k])

    result = 0
    for j in range(len(final_list)):
        result += final_list[j][1] * (j + 1)
    return result, final_list, sorted_hand_replacements


print(calculate_table_value())
