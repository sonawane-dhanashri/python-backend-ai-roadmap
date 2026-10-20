# Day 2 — Oct 20, 2026

## Concepts
- **Indexes vs values.** `i` is a position; `nums[i]` is the number stored there.
- **Pairs with j > i.** Start the inner loop at `i + 1` to avoid repeats and self-pairs. Number of pairs = n(n−1)/2 → O(n²).
- **Complement.** For Two Sum, the partner of `n` is `target - n`.
- **Dict as memory of the past.** Key = what you'll look up later (the number); value = what you need back (its index).
- **Create memory once, before the loop.** `seen = {}` inside the loop wipes it every pass.
- **Loop variables survive the loop** with their last value — a `return i, j` after loops returns leftovers, not an answer.
- **A bare expression does nothing.** `nums[i] + nums[j] == target` alone computes True/False and throws it away; it needs `if`.

## Complexity recipe
1. Find the loops — how many times each runs in terms of n.
2. Cost per pass — arithmetic and dict/set ops O(1); `in list` O(n).
3. Nested → multiply; sequential → add and keep the biggest; drop constants.
4. Space — what grows with n?

## Problems
| Problem | Result | Help needed |
|---|---|---|
| 1 Two Sum (brute force) | Solved | Review hints only |
| 1 Two Sum (dict, O(n)) | Solved | Heavy guidance — re-solve from blank on Sunday |
| 217 Contains Duplicate (brute force) | Solved | Independent |
