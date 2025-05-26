# Write your MySQL query statement below
WITH RankedEmployees AS (
  SELECT 
    e.name AS Employee,
    e.salary AS Salary,
    e.departmentid,
    RANK() OVER (PARTITION BY e.departmentid ORDER BY e.salary DESC) AS rnk
  FROM Employee e
)
SELECT 
  d.name AS Department,
  r.Employee,
  r.Salary
FROM RankedEmployees r
JOIN Department d ON r.departmentid = d.id
WHERE r.rnk = 1;