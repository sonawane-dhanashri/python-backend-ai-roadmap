def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return count_chars(s) == count_chars(t)


def count_chars(word):
    counts = {}
    for character in word:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts


print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "rats"))
print(is_anagram("rat", "car"))
print(is_anagram("aab", "bba"))


