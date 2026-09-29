# Problem Solving, Logic & Reasoning

Peer learning session: **Think Before You Code** (about 90 minutes).

This is not a coding class. It's about what happens **before** the code: understanding a problem, working it out by hand, breaking it into steps, and testing a plan on paper. Code is the last step, and the easy part.

| File | What it's for |
|---|---|
| [slides.md](slides.md) | The session, including two worked examples done step by step |
| [worksheets.md](worksheets.md) | The blank worksheet template and all 9 problems |
| [exercises.py](exercises.py) | Step 5: write your code here and run the tests |
| [solutions.md](solutions.md) | Model thinking for every step of every problem, plus a common wrong turn |

---

## The 6-step framework

**Steps 1 to 4 happen before you touch the keyboard.**

### 1 · Understand
Say the problem back in your own words. If you can't, you don't understand it yet.
- What goes **in**, and what comes **out**? What type is each (number, text, list)?
- What's unclear? Write down the question, or the assumption you're making.
- Is there a rule hidden in the wording ("only once", "the first one", "ignore capitals")?

### 2 · Examples, by hand
Solve 3 to 5 small cases **with a pen, not code**. Write the answer *and why*. Always include an edge case:

| Try | Example |
|---|---|
| Empty | `[]`, `""` |
| Only one item | `[4]` |
| Duplicates | `[7, 7]`, `[5, 5, 5]` |
| Negatives or zero | `[-3, 0]` |
| Odd **and** even sizes | a 3×3 board and a 4×4 board |
| First or last position | the thing you want is at the very start or end |

### 3 · Break it down
Look at what your brain did in Step 2. **Those are your steps.** What did you *remember* as you went? In what *order* did you check things?

### 4 · Plan (pseudocode), then trace it
Plain English with a little structure and no real syntax:

```text
SET total TO 0
FOR EACH price IN basket
    IF price > 1000
        ADD price TO total
RETURN total
```

Then **trace it by hand**: run each Step 2 example through your pseudocode, line by line, in a table. If you get a wrong answer, go back to Step 3. A bug found on paper takes minutes to fix. The same bug found in code can take an hour.

### 5 · Code
Translate the pseudocode line by line. If you find yourself inventing new logic here, stop: the plan is missing something.

### 6 · Test & reflect
A test fails? Don't start patching code. Ask **which step went wrong**. Once it works: is there a simpler way?

### When you're stuck
Solve a smaller version by hand. Write down what your hands did. Explain it out loud to someone else, or to a rubber duck. Re-read the problem and check your Step 1.

---

## How to do an exercise

1. Pick a problem in [worksheets.md](worksheets.md) and copy the template into your notebook.
2. Fill in **Steps 1 to 4** with your group. Laptops closed.
3. **Checkpoint:** another group follows your pseudocode. Can they get every Step 2 answer without asking you anything?
4. Only then, write the function in `exercises.py` and run it:

   ```bash
   cd problem-solving
   python exercises.py chessboard     # one problem
   python exercises.py                # all problems
   ```

5. Compare your thinking with [solutions.md](solutions.md).

**Groups of 3.** Rotate roles every 10 minutes:
- **Scribe** writes, and only what the group agrees on.
- **Navigator** leads the thinking out loud: "By hand, I'm doing…"
- **Skeptic** hunts for edge cases.

---

## For the facilitator

| # | Segment | Time |
|---|---|---|
| 1 | Warm-up puzzles (no code) | 10 min |
| 2 | The 6-step framework | 10 min |
| 3 | Worked example 1: Making change | 15 min |
| 4 | Worked example 2: Second largest (Plan A fails) | 15 min |
| 5 | Peer worksheets | 25 min |
| 6 | Share out: pseudocode and traces, not code | 10 min |
| 7 | Wrap-up and take-home | 5 min |

- In the worked examples, **ask the room before revealing each step**. In example 2, let someone suggest "just sort it", then trace it together and watch it fail.
- In the peer segment, point stuck groups to the questions on the "Stuck?" slide instead of giving hints.
- **Presenting:** `slides.md` is a [Marp](https://marp.app) deck. Install the **Marp for VS Code** extension, open the file and click the preview icon. To present full-screen or on another computer, run **Marp: Export Slide Deck** and choose PDF or PPTX. Facilitator notes are HTML comments and don't appear on the slides.
