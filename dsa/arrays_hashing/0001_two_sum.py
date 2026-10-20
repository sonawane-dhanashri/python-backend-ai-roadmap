def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indexes of the two numbers that add up to target. O(n^2) time."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_fast(nums: list[int], target: int) -> list[int]:
    """Return indexes of the two numbers that add up to target. O(n) time."""
    seen = {}  # number -> index
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([3, 2, 4], 6))
    print(two_sum([3, 3], 6))
    print(two_sum_fast([2, 7, 11, 15], 9))
    print(two_sum_fast([3, 2, 4], 6))
    print(two_sum_fast([3, 3], 6))
