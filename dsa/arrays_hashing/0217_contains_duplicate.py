num = [4, 9, 2, 9, 6]

def contains_duplicate(num):
    seen = set()
    for i in num:
        if i in seen:
            return True
        seen.add(i)
    return False

print(contains_duplicate(num))


num = [4, 9, 2, 5, 6]

def contains_duplicate_brute(num):
    for i in range(0,len(num)):
        a = num[i]
        for j in range(i+1, len(num)):
            b = num[j]
            if a == b:
                return True
    return False

print(contains_duplicate_brute(num))
