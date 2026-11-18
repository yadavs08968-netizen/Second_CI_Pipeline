def missing_number_xor(numbers):
    n = len(numbers)
    result = n
    for index, number in enumerate(numbers):
        result ^= index ^ number
    return result


if __name__ == "__main__":
    print(missing_number_xor([3, 0, 1]))
