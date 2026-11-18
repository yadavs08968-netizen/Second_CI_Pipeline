from collections import Counter


def most_frequent(numbers):
    if not numbers:
        return None
    counts = Counter(numbers)
    return max(numbers, key=counts.get)


if __name__ == "__main__":
    print(most_frequent([1, 3, 2, 3, 4, 3, 2]))
