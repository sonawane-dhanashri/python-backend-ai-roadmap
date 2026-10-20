# Day 1 — Oct 19, 2026

## Concepts
- **Names are labels, not boxes.** `b = a` makes two labels on one object.
- **Mutate vs rebind.** `b.append(4)` changes the shared object; `b = b + [4]` creates a new one and moves `b`.
- **`append` returns `None`.** `b = b.append(4)` sets `b` to `None` — never assign the result of `append`.
- **Strings are immutable.** `s[0] = "H"` raises TypeError; build a new string: `s = "H" + s[1:]`.
- **Variable vs literal key.** `d[fruit]` uses the variable's value; `d["fruit"]` uses the text "fruit".
- **`==` vs `is`.** `==` compares values; `is` compares identity (same object).
- **Mutable:** list, dict, set. **Immutable:** int, float, str, tuple. Immutable objects can't change, but names can always be rebound.
- **Dict access.** `d[k]` for required keys (KeyError if missing); `k in d` to check; `d.get(k, default)` for optional keys.
- **Hash set / dict lookups are O(1)** on average; `x in list` is O(n).
- **Big-O** measures how work grows with input size. Nested loops multiply → O(n²).

## Problems
| Problem | Result | Help needed |
|---|---|---|
| word_count | Solved | Solution shown, then retyped |
| char_count | Solved | Independent (transfer test) |
| 217 Contains Duplicate (set) | Solved | Structured hints (skeleton) |
| SQL SELECT / WHERE / ORDER BY / AND | Solved | Hints on quotes, AND, >= |

## My mistakes to watch
1. `counts["word"]` instead of `counts[word]` — quotes make it fixed text.
2. Adding to `seen` **before** checking it.
3. `return` inside the loop vs after it.
4. SQL: comma instead of `AND`; unquoted text; "at least" = `>=`, "at most" = `<=`.

## OS (evening)
- OS = resource manager (CPU, memory, files, devices) + isolation between programs.
- **Process** = running program with its own memory. **Thread** = unit of execution inside a process, sharing its memory.
- Process crash stays isolated (Chrome tabs); thread bugs can corrupt shared data (race condition).
