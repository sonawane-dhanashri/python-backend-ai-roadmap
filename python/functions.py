def avg(*nums):
    count = len(nums)
    if count == 0:
        return 0
    result = sum(nums) / count
    return result


print(avg(10, 20, 30))
print(avg(5))
print(avg())