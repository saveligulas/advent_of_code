def search_for_bin(numbers, target, index=0):
    if numbers[index] == target:
        return index
    return search_for_bin(numbers, target, index + 1)

print(search_for_bin([1,2,3,4,5,6,7,8,9,10], 5))