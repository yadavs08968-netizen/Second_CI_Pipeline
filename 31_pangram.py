def is_pangram(sentence):
    letters = {char.lower() for char in sentence if char.isalpha()}
    return len(letters) == 26


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))
