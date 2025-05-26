SELECT D.NAME AS Department, E.NAME AS Employee, E.Salary AS Salary 
FROM EMPLOYEE E INNER JOIN DEPARTMENT D ON E.departmentId =D.ID WHERE (d.id,E.SALARY) IN 
(select departmentId, MAX(SALARY) FROM EMPLOYEE GROUP BY departmentId )