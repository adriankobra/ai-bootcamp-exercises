# Solution Notes

## Environment
- Python version: 3.14.3
- Key libraries used: csv, pandas
- LLM API used:
- LLM model used:

## Highest Level Completed

_Mark which level you reached per exercise:_

| Exercise | BASE | STANDARD | ADVANCED |
|----------|------|----------|----------|
| 1 - Python & Data | [X] | [X] | [ ] |
| 2 - SQL | [X] | [X] | [X] |
| 3 - LLM | [ ] | [ ] | [ ] |
| 4 - Integration | [ ] | [ ] | [ ] |

---

## Exercise 1: Data Handling

**Your approach:** _Describe what you did and why._
I loaded the CSV file using Python's csv module because it makes it easy to access values by column name. Then I used loops(for), lists([]), and dictionaries like(status_count["open"] = open_count) for the BASE level tasks.I also used append() to add needed rows to a list and lower() to compare words without case sensitivity. 
For the STANDARD level, I used pandas because the exercise required using it for data cleaning and analysis. Loading the file with pandas was very easy because it only required one line of code. Cleaning the data was also straightforward because I found the necessary functions on W3Schools, such as dropna() for removing empty values, to_datetime() for converting dates, and similar functions. I also looked at different ways of working with dates and time, such as strftime(). Also, I divided by 3600 to convert seconds into hours, rounded the results, and used other simple pandas functions where needed.

**If you completed BASE:** What was your strategy for handling the messy priority values (mixed case like "HIGH", "high", "High")? Did you use any specific Python technique?

As I mentioned earlier, I used the lower() method to make all letters lowercase before comparing them. I used this approach because we usually used the same logic in similar tasks at university.

**If you completed STANDARD:** What would you change if this dataset had 1 million rows instead of 35?

Honestly, I would not change much because pandas is already designed to work with large datasets. I might improve some parts of my code to make them more efficient, but I cannot say exactly what I would change because I have not compared different solutions yet.

**If you completed ADVANCED:** How did you decide what counts as an "anomaly"? Where do you draw the line between messy data and actually wrong data?

---

## Exercise 2: SQL

**Your approach:** _Describe what you did and why._
SQL was easier for me than Python. 
I used SELECT everywhere to get the columns that were required in the tasks. I also wrote all SQL keywords in uppercase because it is easier for me and that is how I learned SQL in my courses.Then I used FROM to get data from the table I needed. When using JOIN, SQL kind of creates a temporary table with the joined data, and FROM works with that result.I used ORDER BY to sort the results (ASC or DESC). AS was used to rename columns to whatever I wanted.
There are different types of JOIN, but I mainly used INNER JOIN, which returns only matching rows from both tables, and LEFT JOIN, which keeps all rows from the table after FROM and adds matching rows from the second table. GROUP BY was used to group rows by a value so everything is organized before using functions like COUNT, SUM, AVG, or MAX, these are basic SQL functions for calculations.In the Advanced level, I used CASE once because it made the query shorter. 
It is basically like an if-else statement.If I forgot something, I just looked it up on W3Schools. I really like that website because you can not only read about SQL functions but also practice them with interactive exercises.

**If you completed BASE:** Which query was hardest to write and what did you look up or try before getting it right?

I think Query 8 was the hardest because it already had a lot of functions, and I started to get a little confused. At first, I tried to solve it using WHERE, then I kept adding more things, but the query became too long and didn't work the way I wanted.Then I remembered about CASE and decided to use it because it made the query much shorter and easier to understand. 
I also had a problem when I divided by total_projects because I wasn't getting the correct result. After spending some more time on it, I looked it up and found that I needed to multiply by 1.0 to get a decimal number. Query 8 was definitely the most difficult one for me.

**If you completed STANDARD:** In Query 6 (active projects per department), how did you handle departments with zero projects? What happens if you use INNER JOIN instead?

I used LEFT JOIN because I wanted to keep all departments from the DEPARTMENTS table, even if they had no active projects. That way I also got departments with 0 active projects.
If I used INNER JOIN instead, departments without active projects would not appear in the result because INNER JOIN only returns rows that have matching data in both tables.

**If you completed ADVANCED:** Query 9 (highest salary per department with ties) — what approach did you take, and what's an alternative way to solve it?

For Query 9, I used a subquery with MAX(SALARY). For each department, the subquery finds the highest salary, and then the main query returns the employee whose salary matches that value. If two or more employees have the same highest salary, they will all be returned because they all match the MAX(SALARY) result. 
I think there are other ways to solve this query, but this was the approach I understood best and it worked correctly for the task.
---

## Exercise 3: LLM & Prompt Engineering

**Your approach:** _Describe what you did and why._

**If you completed BASE:** What did you notice about how the LLM responds differently when you change the wording of your prompt? Give a specific example.

**If you completed STANDARD:** Which of your two prompt strategies worked better? Paste both prompts here and explain what specifically made the difference.

**If you completed ADVANCED:** How does your retry logic decide when to give up? What's the worst-case scenario for your error handling?

---

## Exercise 4: Integration

**Your approach:** _Describe what you did and why._

**If you completed BASE:** How did you handle stop-word removal in keyword extraction? What list did you use and would you change it?

**If you completed STANDARD:** If one document fails during LLM processing, does your pipeline stop or continue? Paste the specific code that handles this.

**If you completed ADVANCED:** How does your incremental processing detect which documents were already processed? What happens if the output file gets corrupted?

---

## Process Questions

_These questions are about your experience doing the task, not the code itself._

1. **What did you get stuck on longest?** Describe the specific moment — what you were trying to do, what went wrong, and how you got past it.

2. **What did you Google/search for during this task?** List 2–3 specific things you looked up.

3. **If you used AI tools (Copilot, ChatGPT, etc.), which parts did you use them for?** Be honest — this is not penalized. We want to understand your workflow.

---

## Self-Estimation

_Rate your current skill level honestly (1 = no experience, 5 = very confident):_

| Skill | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|
| Python programming | [ ] | [ ] | [ ] | [ ] | [ ] |
| Working with data (files, CSV, JSON) | [ ] | [ ] | [ ] | [ ] | [ ] |
| pandas / data analysis | [ ] | [ ] | [ ] | [ ] | [ ] |
| SQL | [ ] | [ ] | [ ] | [ ] | [ ] |
| Git and version control | [ ] | [ ] | [ ] | [ ] | [ ] |
| REST APIs (calling/building) | [ ] | [ ] | [ ] | [ ] | [ ] |
| LLMs and prompt engineering | [ ] | [ ] | [ ] | [ ] | [ ] |
| Error handling and debugging | [ ] | [ ] | [ ] | [ ] | [ ] |
| Reading documentation to learn new tools | [ ] | [ ] | [ ] | [ ] | [ ] |
| Explaining technical concepts to others | [ ] | [ ] | [ ] | [ ] | [ ] |

**What is your strongest technical skill overall?**
_

**What is the area you most want to improve during the bootcamp?**
_

**Have you built any personal or work projects before? If yes, briefly describe one:**
_

---

## Self-Assessment

_What are you least confident about in your submission? What would you do differently next time?_
