def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

print(two_sum([2,7,11,15],9))
print(two_sum([3,2,4],6))
print(two_sum([3,3], 6))


def two_sum_fast(nums, target):
    seen= {}
    for i in range(0,len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement],i]
        seen[nums[i]]=i
    return []
print(two_sum_fast([2,7,11,15], 9))
print(two_sum_fast([3,2,4],6))
print(two_sum_fast([3,3], 6))
