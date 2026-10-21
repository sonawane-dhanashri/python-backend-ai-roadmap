def group_anagram(word):
    group={}
    for each in word:
        # print(each)
        label = "".join(sorted(each))
        # print(label)
        if label in group:
            group[label].append(each)
        else:
            group[label]=[each]
    return list(group.values())


print(group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
