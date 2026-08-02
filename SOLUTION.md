# Solution Notes

## Environment
- Python version: 3.14.3
- Key libraries used: csv, pandas, groq
- LLM API used: Groq API
- LLM model used: llama-3.3-70b-versatile

## Highest Level Completed

_Mark which level you reached per exercise:_

| Exercise | BASE | STANDARD | ADVANCED |
|----------|------|----------|----------|
| 1 - Python & Data | [X] | [X] | [ ] |
| 2 - SQL | [X] | [X] | [X] |
| 3 - LLM | [X] | [X] | [ ] |
| 4 - Integration | [X] | [X] | [ ] |

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


## Exercise 3: LLM & Prompt Engineering

**Your approach:** _Describe what you did and why._

At first, I chose Gemini because I had heard about it from friends. I created an API key and tried to connect it through PowerShell, but it did not work. Every time I ran the program, it immediately showed a quota/limit error. Because of that, I switched to Groq, since it was described as fast and free. I followed the same setup process, and it worked without any problems.
The first thing I learned was that to let the LLM work with the company descriptions, I needed to include {text} in the prompt. For questions, I used the question variable, and I called the model with call_llm().
The main challenge in the Standard level was getting clean JSON output. At first, the model often returned extra text or explanations, so I had to improve the prompts by adding clearer instructions about the expected output format. Creating different prompts was not difficult because only the prompt changed while the overall logic stayed the same.
In the end, I compared two different prompt strategies. I found that the more specific and detailed the prompt is, the more accurate and consistent the LLM's response becomes.

**If you completed BASE:** What did you notice about how the LLM responds differently when you change the wording of your prompt? Give a specific example.

I realized that even a very small change in the prompt can completely change the output. For example, when I asked the LLM to choose the main information about each company by itself, it selected different fields, changed the field names, and returned a different structure. When I gave a more specific prompt with an example and clearly asked for only valid JSON, the output matched the expected format much better.

**If you completed STANDARD:** Which of your two prompt strategies worked better? Paste both prompts here and explain what specifically made the difference.

My first prompt strategy worked better because I gave the LLM an example of the expected output. This helped it understand exactly what format I wanted.
**1**
    prompt = f"""
    Read the company descriptions and extract the following information for each company 
    like:
    
    "company_name": "TechNova Solutions",
    "industry": "Cloud infrastructure management and DevOps automation tools",
    "founded_year": 2018,
    "num_employees": 120,
    "key_products": [
      "CloudOrbit",
      "NovaDeploy"
        ]
      ,
    Use the same format for all companies.
    Company description:
    {text}

    Return ONLY valid JSON.
    Do not include explanations.
    Do not include markdown.
    """

For the second strategy, I decided to trust the LLM more and let it decide what the main information about each company was.

**2**
    prompt = f"""

    Extract the 5 main pieces of information for each company and return a list of dictionaries with valid JSON-parseable output.
    {text}
    Return ONLY valid JSON.
    Do not include explanations.
    Do not include markdown.
    Do not include any text before or after the JSON
    """
The first prompt produced the exact format I wanted because I showed an example. The second prompt was more flexible, so the LLM chose slightly different fields and field names, but the result was still very similar. From this exercise, I learned that if you need very accurate and consistent output, it is better to combine both approaches: clearly explain the task and also provide an example of the expected result.



**If you completed ADVANCED:** How does your retry logic decide when to give up? What's the worst-case scenario for your error handling?

---

## Exercise 4: Integration

**Your approach:** _Describe what you did and why._

While working on Exercise 4, the BASE level was quite difficult for me. First, I had to learn how to read files using the Path library because I had never used it before. I found a simple solution on the internet. Counting words was easier because I already knew about the split() function and using len(). The stop words part was also not too difficult, but I did not know about Counter, so I learned it from online documentation.The basic_stats function was the hardest part of the BASE level because it required combining several ideas. For example, I borrowed the idea of using 1000000 and 0 as starting values from AI, and I also needed help understanding how to keep track of the shortest and longest documents. After that, the for loop became clearer, but overall the BASE level was still challenging for me.
The STANDARD level was easier at the beginning because it was similar to Exercise 3. The functions for prompting the LLM were familiar. However, I did not know how to save JSON results, so I found the solution in the Python documentation. Finally, in generate_report, I understood most of the logic, but I used AI to better understand the last part report += f"{word}: {count}\n"
Overall, I can say that both the BASE and STANDARD levels contained several tasks that were completely new to me, so I had to learn new concepts from documentation, the internet, and AI while completing the exercise.

**If you completed BASE:** How did you handle stop-word removal in keyword extraction? What list did you use and would you change it?

I used a simple list of stop words and checked every word against that list. I would not change this approach because a list is easy to use and understand, and it worked well for this exercise.

**If you completed STANDARD:** If one document fails during LLM processing, does your pipeline stop or continue? Paste the specific code that handles this.

If one document fails, my pipeline stops. I did not implement error recovery, so there is no try block to continue processing.
def process_all_documents(documents: list[dict]) -> list[dict]:
    results = []

    for doc in documents:
        analysis = analyze_document(doc["content"])

        results.append({
            "filename": doc["filename"],
            "summary": analysis["summary"],
            "keywords": analysis["keywords"],
            "sentiment": analysis["sentiment"],
        })

    return results

**If you completed ADVANCED:** How does your incremental processing detect which documents were already processed? What happens if the output file gets corrupted?

---

## Process Questions

_These questions are about your experience doing the task, not the code itself._

1. **What did you get stuck on longest?** Describe the specific moment — what you were trying to do, what went wrong, and how you got past it.
I got stuck the longest on Exercises 1 and 4 because I do not know all Python functions yet. Sometimes I could not figure out which approach to use because I did not know that a certain function existed, or I simply forgot about it. Most of my difficulties were related to Python. I was usually able to find or remember the solution, but it took much more time. There were also a few moments when I could not make any progress, so I used AI as an assistant. It suggested possible approaches, recommended Python functions that could solve the problem, and sometimes helped me find mistakes when I thought everything was correct but there was still an error. This probably happened about 4–6 times. As I mentioned, these difficulties were only with Python; I did not have similar problems with SQL.

2. **What did you Google/search for during this task?** List 2–3 specific things you looked up.
I opened W3Schools many times because it has a simple interface and it is easy to quickly find examples and practice. I also searched for how to work with JSON because I did not remember all the details, and I looked up the Path library because I did not remember all of its functions and features.

3. **If you used AI tools (Copilot, ChatGPT, etc.), which parts did you use them for?** Be honest — this is not penalized. We want to understand your workflow.
I used ChatGPT Go mainly to help me find mistakes in my code or suggest a Python function that could solve a problem. Sometimes searching through the documentation for the right function took a lot of time, so AI helped me find the right direction faster.
I did not use AI all the time because it was in my own interest to learn something new. However, there were moments when I did not know how to continue, so I asked ChatGPT for help to understand the next step. I think AI should be used as an assistant because it can also make mistakes, and it is important to understand every line of code yourself instead of just copying it.
I also sometimes used ChatGPT as a translator because I occasionally have difficulties with English.
---

## Self-Estimation

_Rate your current skill level honestly (1 = no experience, 5 = very confident):_

| Skill | 1 | 2 | 3 | 4 | 5 |
|-------|---|---|---|---|---|
| Python programming | [ ] | [2] | [ ] | [ ] | [ ] |
| Working with data (files, CSV, JSON) | [ ] | [ ] | [3] | [ ] | [ ] |
| pandas / data analysis | [ ] | [ ] | [3] | [ ] | [ ] |
| SQL | [ ] | [ ] | [ ] | [4] | [ ] |
| Git and version control | [ ] | [ ] | [3] | [ ] | [ ] |
| REST APIs (calling/building) | [ ] | [2] | [ ] | [ ] | [ ] |
| LLMs and prompt engineering | [ ] | [ ] | [ ] | [4] | [ ] |
| Error handling and debugging | [ ] | [ ] | [3] | [ ] | [ ] |
| Reading documentation to learn new tools | [ ] | [ ] | [3] | [ ] | [ ] |
| Explaining technical concepts to others | [ ] | [2] | [ ] | [ ] | [ ] |

**What is your strongest technical skill overall?**

I think my strongest technical skill is SQL. I find its logic easy to understand, and I had three SQL courses at university, so I have had a lot of practice. Of course, I still sometimes need to look something up, but I can work with SQL confidently and usually know how to solve problems using it.

**What is the area you most want to improve during the bootcamp?**

I would like to improve my Python skills the most. I feel comfortable with the basics, but when the tasks become more advanced, I find them much more difficult. I always try to understand the solution instead of just copying it, so I hope to become much more confident with Python during the bootcamp. I would also like to improve my English because it will help me work with documentation and communicate more easily.

**Have you built any personal or work projects before? If yes, briefly describe one:**
---

One of my main personal projects was a Python application that compared prices from three different websites and displayed the best available price. It used fast page loading and web scraping to collect the data. I built it about a year ago.
Another important project was my bachelor's thesis. I worked with three different 3D face reconstruction systems on Ubuntu. I had to compile the projects on my own computer, which took a lot of time because I needed to install and configure the correct libraries and dependencies. All of the systems were run and tested through the Linux terminal.


## Self-Assessment

_What are you least confident about in your submission? What would you do differently next time?_

I am least confident about some parts of my submission, especially the STANDARD level of Exercise 4. Even though I completed it and it works, there are still a few parts that I do not fully understand. There are also some functions that are still new to me, so I am not completely confident using them yet.I would also say that some parts of the STANDARD level in Exercise 4 were quite difficult for me because they introduced concepts I had not used before.
Next time, I would spend more time learning those functions and understanding the logic behind them before moving on to the next task.
When I was not confident enough, I decided not to continue with the ADVANCED level. I only completed the ADVANCED part in SQL because I felt comfortable with it. For the other exercises, I think I do not have enough experience yet. If I did this again, I would spend more time learning the concepts first so I could solve more tasks on my own. 
