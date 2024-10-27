def moon_weight(earth_weight):
    """
    Compute weight on the moon from weight on earth.
    """
    return earth_weight * (1 / 6)

# Example usage
print(moon_weight(60))  # Output: 10.0

#1C - 9.1.1

def convert_signs(numbers):
    return ["pos" if num > 0 else "neg" if num < 0 else "zero" for num in numbers]

# Example usage:
numbers = [10, -5, 0, 3, -1]
print(convert_signs(numbers))  # Output: ['pos', 'neg', 'zero', 'pos', 'neg']

def has_length_five(strings):
    return any(len(s) == 5 for s in strings)

# Example usage:
strings = ["hello", "world", "python", "code"]
print(has_length_five(strings))  # Output: True

def filter_even_numbers(numbers):
    return [num for num in numbers if 10 <= num <= 20 and num % 2 == 0]

# Example usage:
numbers = [8, 10, 12, 15, 18, 22]
print(filter_even_numbers(numbers))  # Output: [10, 12, 18]


def all_z_words(wordlist : list) -> list:
    """produce list of words from the input that contain z"""
    zlist = [] # start with an empty list
    for wd in wordlist:
        if "z" in wd:
            zlist = [wd] + zlist
    return zlist
wordlist = ['pizza', 'banan', 'zebra', 'løve']
print(all_z_words(wordlist))