# Worksheets

## Submission

Save your solution in a .md or .txt file using your name eg. <emmanuel>.txt and upload it on https://forms.gle/NgDyWhDhgpWRvTUx5

or using the same file format save your file in `problem_solving/wk1/submissions` and create a pull request


## The problems

| # | Level | Problem | Function |
|---|---|---|---|
| 01 | Warm | Leap year | `is_leap_year` |
| 02 | Warm | FizzBuzz | `fizzbuzz` |
| 03 | Warm | Palindrome check | `is_palindrome` |
| 04 | Core | Chessboard | `chessboard` |
| 05 | Core | The missing number | `find_missing` |
| 06 | Core | Find the repeats | `find_duplicates` |
| 07 | Core | Anagram check | `is_anagram` |
| 08 | Stretch | Two sum | `two_sum` |
| 09 | Take-home | The longest word | `longest_word` |

Do **one Warm** problem properly, then move to Core. Doing one problem well is better than rushing through three.

---

## 01 · Leap year

**Warm** · function in `exercises.py`: `is_leap_year`

Write a function that says whether a year is a leap year.

The rule: a year is a leap year if it is divisible by 4, **except** years divisible by 100, which are **not** leap years, **unless** they are also divisible by 400, which **are**.

**Step 2, work these out by hand:** `2024`, `2023`, `1900`, `2000`, `2100`, plus at least one edge case of your own.

---

## 02 · FizzBuzz

**Warm** · function in `exercises.py`: `fizzbuzz`

For each number from 1 to `n`, say **"Fizz"** if it is divisible by 3, **"Buzz"** if it is divisible by 5, **"FizzBuzz"** if it is divisible by both, and otherwise the number itself. Return the results as a list of strings.

**Step 2, work these out by hand:** `n = 5`, `n = 15`, `n = 0`, plus at least one edge case of your own.

---

## 03 · Palindrome check

**Warm** · function in `exercises.py`: `is_palindrome`

Return `True` if a phrase reads the same forwards and backwards, ignoring capitals, spaces and punctuation.

**Step 2, work these out by hand:** `"Racecar"`, `"Never odd or even"`, `"Lagos"`, `""`, plus at least one edge case of your own.

---

## 04 · Chessboard

**Core** · function in `exercises.py`: `chessboard`

Given a number `n`, build an **n × n chessboard**. Use `#` for dark squares and `.` for light squares. The top-left square is light.

Return the board as a list of rows. Printing each row shows the board. For `n = 3`:

```text
.#.
#.#
.#.
```

**Step 2, work these out by hand:** `n = 1`, `n = 2`, `n = 3`, `n = 4`, `n = 0`, plus at least one edge case of your own.

---

## 05 · The missing number

**Core** · function in `exercises.py`: `find_missing`

A list holds the numbers 1 to n **in any order**, with **exactly one** number missing. Find the missing number.

**Step 2, work these out by hand:** `[1, 2, 4, 5, 6]`, `[3, 1, 2]`, `[2, 3, 4]`, `[]`, plus at least one edge case of your own.

---

## 06 · Find the repeats

**Core** · function in `exercises.py`: `find_duplicates`

Return every number that appears **more than once** in a list. List each repeated number only once, in the order its repeat was first spotted.

**Step 2, work these out by hand:** `[4, 2, 7, 2, 9, 4, 4]`, `[1, 2, 3]`, `[5, 5, 5]`, `[]`, plus at least one edge case of your own.

---

## 07 · Anagram check

**Core** · function in `exercises.py`: `is_anagram`

Return `True` if two words use exactly the same letters, the same number of times. For example, "listen" and "silent".

**Step 2, work these out by hand:** `"listen", "silent"`, `"aab", "abb"`, `"abc", "ab"`, `"", ""`, plus at least one edge case of your own.

---

## 08 · Two sum

**Stretch** · function in `exercises.py`: `two_sum`

Given a list of numbers and a target, return the **positions** of the two numbers that add up to the target. Return `None` if no pair adds up to it.

**Step 2, work these out by hand:** `[2, 7, 11, 15], target 9`, `[3, 3], target 6`, `[3, 5], target 6`, `[1, 2], target 10`, plus at least one edge case of your own.

---

## 09 · The longest word

**Take-home** · function in `exercises.py`: `longest_word`

Given a sentence, return its longest word. If two words tie, return the one that appears **first**. Return an empty string for an empty sentence.

**Step 2, work these out by hand:** `"Code is thinking made visible"`, `"cat dog"`, `"hi"`, `""`, plus at least one edge case of your own.
