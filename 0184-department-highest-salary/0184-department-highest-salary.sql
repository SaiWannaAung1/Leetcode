# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN (
    SELECT departmentid, MAX(salary) AS max_salary
    FROM Employee
    GROUP BY departmentid
) max_salaries
  ON e.departmentid = max_salaries.departmentid
 AND e.salary = max_salaries.max_salary
JOIN Department d
  ON e.departmentid = d.id;