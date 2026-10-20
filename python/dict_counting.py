def word_count(sentence: str) -> dict[str, int]:
    """Count how many times each word appears in a sentence."""
    counts = {}
    for word in sentence.split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def char_count(text: str) -> dict[str, int]:
    """Count how many times each character appears in a string."""
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


if __name__ == "__main__":
    print(word_count("the cat and the hat and the bat"))
    print(char_count("banana"))
