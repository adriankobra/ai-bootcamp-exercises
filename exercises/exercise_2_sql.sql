-- Exercise 2: SQL
-- ======================
-- This exercise has three levels. Complete as far as you can.
--
-- To test your queries, run:
--   python exercises/run_sql.py
--
-- This will execute each query against an in-memory SQLite database
-- loaded with the sample data from data/schema.sql.


-- ============================================================
-- BASE LEVEL — Simple queries
-- ============================================================

-- Query 1: List all employees sorted by name alphabetically.
-- Expected columns: name, salary, hire_date
--select
SELECT NAME,SALARY,HIRE_DATE 
--table
FROM EMPLOYEES
--asc
ORDER BY NAME ASC;


-- Query 2: List all employees with their department name.
-- (Hint: you need to JOIN two tables)
-- Expected columns: employee_name, department_name
SELECT E.NAME AS employee_name, D.NAME AS department_name
FROM EMPLOYEES E
--need all matching values
INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.ID;

-- Query 3: Count how many employees are in each department.
-- Expected columns: department_name, employee_count
--COUNT
SELECT D.NAME AS department_name, COUNT (E.ID) AS employee_count
FROM EMPLOYEES E
INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.ID
--NEED GROUP BECAUSE TO MAKE GROUP BY NAME
GROUP BY D.NAME;
-- ============================================================
-- STANDARD LEVEL — JOINs, aggregations, filtering
-- ============================================================

-- Query 4: Find the top 3 departments by average salary.
-- Expected columns: department_name, avg_salary
--also i use round because result with unlimittet simbols after avg
SELECT D.NAME AS department_name, ROUND(AVG(E.SALARY),2) AS avg_salary
FROM EMPLOYEES E
INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.ID
GROUP BY D.NAME
--desc
ORDER BY AVG_SALARY DESC
--first 3
LIMIT 3;

-- Query 5: Find departments where the total employee salary exceeds the department budget.
-- Expected columns: department_name, total_salary, budget
SELECT D.NAME AS department_name, SUM(E.SALARY) AS total_salary, D.BUDGET AS budget
FROM EMPLOYEES E
INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.ID
--also need budget group
GROUP BY D.NAME, D.BUDGET
--employee salary exceeds the department  
HAVING SUM(E.SALARY) > D.BUDGET;

-- Query 6: Count the number of active projects per department,
--          including departments with zero active projects.
-- Expected columns: department_name, active_project_count
--count projects.ID
SELECT D.NAME AS department_name, COUNT (P.ID) AS active_project_count
FROM DEPARTMENTS D
-- LEFT JOIN keeps all departments including departments with zero active
LEFT JOIN PROJECTS P ON D.ID = P.DEPARTMENT_ID AND P.STATUS = 'active'
--number of active (where)
GROUP BY D.NAME;
-- ============================================================
-- ADVANCED LEVEL — Subqueries, complex logic
-- ============================================================

-- Query 7: Find employees who were hired in the last 12 months and work in departments
--          with at least one completed project.
-- Expected columns: employee_name, department_name, hire_date
SELECT E.NAME AS employee_name, D.NAME AS department_name, E.HIRE_DATE 
FROM EMPLOYEES E
--need 2 joins fot 3 table
INNER JOIN DEPARTMENTS D ON E.DEPARTMENT_ID=D.ID 
INNER JOIN PROJECTS P ON D.ID=P.DEPARTMENT_ID 
--in the last 12 months wrom now and work in departmentswith at least one completed project.
WHERE E.HIRE_DATE >= '2025-08-01' AND P.STATUS = 'completed';

-- Query 8: Rank departments by their "project success rate"
--          (completed projects / total projects). Exclude departments with no projects.
-- Expected columns: department_name, total_projects, completed_projects, success_rate

SELECT D.NAME AS department_name, COUNT(P.ID) AS total_projects, 
--With case can easy make if else
SUM(CASE WHEN P.STATUS = 'completed' THEN 1 ELSE 0 END) AS completed_projects, 
-- need *1.0 for decimal result
ROUND((SUM(CASE WHEN P.STATUS = 'completed' THEN 1 ELSE 0 END)* 1.0 /COUNT(P.ID)),2) AS success_rate
FROM DEPARTMENTS D
INNER JOIN PROJECTS P ON D.ID=P.DEPARTMENT_ID
GROUP BY D.NAME
-- Rank 
ORDER BY SUCCESS_RATE DESC;

-- Query 9: For each department, find the employee with the highest salary.
--          If multiple employees tie, show all of them.
-- Expected columns: department_name, employee_name, salary
--
SELECT D.NAME AS department_name, E.NAME AS employee_name, E.SALARY
FROM DEPARTMENTS D 
INNER JOIN EMPLOYEES E ON D.ID = E.DEPARTMENT_ID
--highest salary in each department
WHERE E.SALARY = (SELECT MAX(SALARY) FROM EMPLOYEES 
-- current department
WHERE DEPARTMENT_ID = D.ID);
