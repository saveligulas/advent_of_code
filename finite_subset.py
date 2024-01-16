def generate_subsets(numbers, current_set, result):
    if current_set != set() and current_set not in result:
        result.append(set(current_set)) # set() weil current_set mutable
    else:
        result.append(f"Next step - remaining numbers: {numbers}, set: {set(current_set)}")
    if numbers:     # rekursion stoppt sobald numbers leer ist
        # generiert uns alle subsets mit dem ersten Element von numbers - startet bei (0)
        # nur dieser Aufruf generiert neue Sets, die abgespeichert werden
        generate_subsets(numbers[1:], current_set.union({numbers[0]}), result)
        # geht in die nächste Rekursion ohne das erste Element
        generate_subsets(numbers[1:], current_set, result)


def get_finite_subsets(n):
    result = []
    generate_subsets([x for x in range(n + 1)], set(), result)
    return result


for subset in get_finite_subsets(3):
    print(subset)


