def is_sorted(numbers):
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


if __name__ == "__main__":
    print(is_sorted([1, 2, 2, 4]))
