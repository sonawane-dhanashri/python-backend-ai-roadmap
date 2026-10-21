# Learning Logs

Daily interview preparation for Python backend and GenAI roles, started October 2026.
All code here is written by hand, without AI autocomplete.

## Structure

```
notes/    daily notes: concepts learned and mistakes to watch
python/   Python fundamentals practice, one file per topic
dsa/      LeetCode solutions, grouped by pattern, named by problem number
```

## DSA progress

| # | Problem | Pattern | Approaches | Date |
|---|---|---|---|---|
| 1 | [Two Sum](dsa/arrays_hashing/0001_two_sum.py) | Hash map | Brute force O(n²), hash map O(n) | Oct 20 |
| 217 | [Contains Duplicate](dsa/arrays_hashing/0217_contains_duplicate.py) | Hash set | Brute force O(n²), hash set O(n) | Oct 19 |
| 242 | [Valid Anagram](dsa/arrays_hashing/0242_valid_anagram.py) | Hash map | Count both strings, compare dicts O(n) | Oct 21 |
| 49 | [Group Anagrams](dsa/arrays_hashing/0049_group_anagrams.py) | Hash map | Sorted word as key, dict of lists O(n·k log k) | Oct 21 |

## Python topics

| Topic | File |
|---|---|
| References, mutability, strings, dicts | [references_and_dicts.py](python/references_and_dicts.py) |
| Counting with dictionaries | [dict_counting.py](python/dict_counting.py) |
| Functions, *args, default handling | [functions.py](python/functions.py) |

## Running

Python 3.9+. Each file runs its own examples:

```bash
python3 dsa/arrays_hashing/0001_two_sum.py
```
