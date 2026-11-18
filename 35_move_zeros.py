def move_zeros(numbers):
    non_zeros = [number for number in numbers if number != 0]
    zeros = [number for number in numbers if number == 0]
    return non_zeros + zeros


if __name__ == "__main__":
    print(move_zeros([0, 1, 0, 3, 12]))
