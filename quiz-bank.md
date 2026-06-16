# Quiz Bank — From Zero to Python with AI

Six questions per checkpoint plus a final quiz. Mix of multiple-choice (MCQ),
true/false (T/F), and predict-the-output (PTO). Answers are at the bottom of
each section. Use as a live poll, randomise the order, or wire into the site.

---

## Checkpoint 1 — Python with AI

**Q1 (MCQ).** A *variable* is best described as:
- A. a colour on screen
- B. a labelled box that stores a value
- C. an error message
- D. a type of loop

**Q2 (MCQ).** What does `print()` do?
- A. saves a file
- B. deletes a value
- C. shows a value on screen
- D. asks the AI a question

**Q3 (PTO).** After these lines, what is `steps`?
```python
steps = 0
steps = steps + 1
steps = steps + 1
```
- A. 0   B. 1   C. 2   D. 3

**Q4 (MCQ).** You want to repeat an action several times. You need a:
- A. variable   B. loop   C. comment   D. print

**Q5 (T/F).** A good prompt to an AI tells it the goal, the inputs, and the output you want. **True / False**

**Q6 (MCQ).** Which is the *better* prompt for a beginner?
- A. "make code"
- B. "fix it"
- C. "Write a Python program that counts steps and prints the total, explained simply"
- D. "python"

**Answers:** 1‑B · 2‑C · 3‑C · 4‑B · 5‑True · 6‑C

---

## Checkpoint 2 — micro:bit

**Q1 (MCQ).** Which sensor on the micro:bit detects movement?
- A. temperature sensor   B. accelerometer   C. light sensor   D. compass

**Q2 (MCQ).** In `steps += 1`, what happens?
- A. steps becomes 1   B. steps increases by 1   C. steps resets   D. nothing

**Q3 (MCQ).** What does `while True:` mean?
- A. run once   B. run only if true   C. keep running / repeat forever   D. stop the program

**Q4 (PTO).** In the step counter, which line actually *counts* a step?
```python
from microbit import *
steps = 0
while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(steps)
```
- A. `steps = 0`
- B. `while True:`
- C. `if accelerometer.was_gesture('shake'):` then `steps += 1`
- D. `display.show(steps)`

**Q5 (T/F).** The micro:bit step count will always exactly match your real number of steps. **True / False**

**Q6 (MCQ).** To make button B reset the counter, you would add:
- A. `if button_b.is_pressed(): steps = 0`
- B. `steps = steps + 1`
- C. `display.clear()`
- D. `while False:`

**Answers:** 1‑B · 2‑B · 3‑C · 4‑C · 5‑False · 6‑A

---

## Checkpoint 3 — Step Data Analyser

**Q1 (MCQ).** A *list* stores:
- A. one value   B. many values in order   C. only words   D. nothing

**Q2 (PTO).** Given `steps = [5200, 8100, 6400]`, what is `steps[0]`?
- A. 0   B. 5200   C. 8100   D. 3

**Q3 (MCQ).** What does `sum(steps)` give you?
- A. the biggest value   B. the number of days   C. all the steps added together   D. the average

**Q4 (PTO).** What does `max([5200, 8100, 6400])` return?
- A. 5200   B. 6400   C. 8100   D. 19700

**Q5 (MCQ).** To check whether a day beat 10,000 steps, you use:
- A. a `for` loop only   B. an `if` statement   C. a `print`   D. a function name

**Q6 (T/F).** You can analyse step data with just lists and loops — you don't *need* any special library to start. **True / False**

**Answers:** 1‑B · 2‑B · 3‑C · 4‑C · 5‑B · 6‑True

---

## Final Quiz — Completion (8 questions)

**Q1 (MCQ).** Best description of a variable? → labelled box that stores a value *(B of: number / box / loop / error)*

**Q2 (PTO).** `steps = 5; steps = steps + 1` → `steps` is? **(6)**

**Q3 (MCQ).** Which sensor counts steps on the micro:bit? → **accelerometer**

**Q4 (MCQ).** `while True:` means? → **repeat forever**

**Q5 (MCQ).** A list holds? → **many values in order**

**Q6 (PTO).** `max([3, 9, 4])` returns? **(9)**

**Q7 (MCQ).** Which prompt is best?
- A. "code"  · B. "Write a Python program that totals my weekly steps and prints the average, explained simply"
→ **B**

**Q8 (Reflection — open answer).** Name one thing you built today, and one thing you'd build next.

**Answers:** 1‑box · 2‑6 · 3‑accelerometer · 4‑repeat forever · 5‑many values in order · 6‑9 · 7‑B · 8‑open

---

### Concept coverage map (so you can balance a randomised quiz)

| Concept | Checkpoint Qs |
|---|---|
| Variable | C1‑Q1, C1‑Q3, Final‑Q1/Q2 |
| Print / output | C1‑Q2 |
| Conditional (if) | C2‑Q4/Q6, C3‑Q5 |
| Loop | C1‑Q4, C2‑Q3, Final‑Q4 |
| Function | (Step 3 starter — add if desired) |
| List | C3‑Q1/Q2, Final‑Q5 |
| micro:bit / sensor | C2‑Q1/Q2/Q5 |
| AI prompting | C1‑Q5/Q6, Final‑Q7 |
