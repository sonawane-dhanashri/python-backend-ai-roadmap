def contains_duplicate_brute(nums: list[int]) -> bool:
    """Return True if any value appears twice. O(n^2) time."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def contains_duplicate(nums: list[int]) -> bool:
    """Return True if any value appears twice. O(n) time, O(n) space."""
    seen = set()
    for n in nums:
        # Check before adding, otherwise every number "finds" itself.
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
    print(contains_duplicate([1, 2, 3, 4]))
    print(contains_duplicate_brute([1, 2, 3, 1]))
    print(contains_duplicate_brute([1, 2, 3, 4]))
