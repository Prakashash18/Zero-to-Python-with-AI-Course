# =====================================================================
#  STEP 3 STARTER  ·  From Zero to Python with AI
#  Analyse a week of step data. Runs anywhere (Trinket, Colab, IDLE).
#  Tip: ask your AI helper to "explain this line by line, simply".
# =====================================================================

# --- Part A: the data as simple lists (no file needed) ----------------
# This is the same idea you learned in Step 1: a list is a row of boxes.
days  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [6200, 8100, 6400, 13420, 7300, 12500, 11200]

# Show each day (Step 1 concept: the FOR loop)
print("Your week:")
for i in range(len(days)):
    print(" ", days[i], "->", steps[i], "steps")
print()

# --- Part B: the big numbers ------------------------------------------
total   = sum(steps)
average = total / len(steps)
best    = max(steps)
worst   = min(steps)

print("Total steps this week:", total)
print("Daily average:", round(average))
print("Best day:", best, "steps")
print("Quietest day:", worst, "steps")
print()

# --- Part C: goal check (Step 1 concept: the IF statement) ------------
GOAL = 10000
hits = 0
for i in range(len(days)):
    if steps[i] >= GOAL:
        print(days[i], "hit the", GOAL, "goal!")
        hits += 1
print("You hit your goal on", hits, "day(s).")
print()

# --- Part D: a text bar chart (no libraries needed) -------------------
print("Activity chart (each block = 1000 steps):")
for i in range(len(days)):
    bar = "#" * (steps[i] // 1000)
    print(" ", days[i], bar, steps[i])
print()

# --- Part E: a reusable machine (Step 1 concept: the FUNCTION) --------
def summarise(step_list):
    t = sum(step_list)
    a = round(t / len(step_list))
    return "You walked " + str(t) + " steps, averaging " + str(a) + " a day."

print(summarise(steps))


# =====================================================================
#  NEXT LEVEL  ·  read the real file (download step_data.csv first)
#  Un-comment the lines below once step_data.csv is next to this file.
# =====================================================================
# import csv
#
# dates, all_steps = [], []
# with open("step_data.csv") as f:           # data/step_data.csv from the site
#     reader = csv.DictReader(f)
#     for row in reader:
#         dates.append(row["date"])
#         all_steps.append(int(row["steps"]))
#
# print("Loaded", len(all_steps), "days from the file.")
# print(summarise(all_steps))                 # the same machine works on real data!
