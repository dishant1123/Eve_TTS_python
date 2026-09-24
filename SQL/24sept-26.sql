/*
group  by  : group wise 

sytax :   select   ...... from  .... table_name....where....group by....order by...limit

*/ 

-- Q1. Count employees in each department.

use scott;
select * from  employees;

select department_id ,count(*) as employees_count
from employees 
group by  department_id ;

-- 2 .total salary  for each department  

select department_id,sum(salary)  as dept_wise_salary
from employees 
group by  department_id ;

-- 3. avg salary  for  each department  
select department_id,avg(salary)  as dept_wise_salary
from employees 
group by  department_id ;

-- highest salary  for  each department . 
select department_id,max(salary)  as dept_wise_salary
from employees 
group by  department_id ;

-- low salary 
select department_id,min(salary)  as dept_wise_salary
from employees 
group by  department_id ;

-- 4 DISPLAY DEPARTMENT_ID AND JOB_ID WISE NO. OF EMPLOYEES
select department_id,job_id,count(*) 
as job_dept_wise_emp
from employees 
group by  department_id ,job_id;

-- 5 DISPLAY HIRE YEAR WISE NO. OF EMPLOYEES

-- 6 DISPLAY QUARTER WISE TOTAL OF SALARY. 

select first_name , hire_date ,salary, 
quarter(hire_date) 
from  employees;

-- 7 DISPLAY DEPARTMENT_ID WISE, JOB_ID WISE LOWEST AND HIGHEST SALARY
select department_id,job_id,
min(salary) as min_salary,
max(salary) as max_salary 
from employees 
group by  department_id ,job_id;

-- 8 DISPLAY MANAGER_ID WISE , JOB_ID WISE AVERAGE SALARY AND TOTAL OF SALARY
select manager_id,job_id,
sum(salary) as total_salary,
avg(salary) as avg_salary 
from employees 
group by  manager_id ,job_id;



/*








9 DISPLAY DEPARTMENT_ID WISE , MANAGER_ID WISE COUNT OF EMPLOYEES

10 DISPLAY DEPARTMENT_ID WISE , JOB_ID WISE , MANAGER_ID WISE LOWEST SALARY, AVERAGE SALARY AND HIGHEST SALARY

11 DISPLAY ONLY DATE WISE (IGNORE MONTH AND YEAR) HIGHEST AND LOWEST SALARY

12 DISPLAY DAY WISE (MON,TUE...) AVERAGE SALARY

13 DISPLAY MONTH WISE (IGNORE DATE AND YEAR) TOTAL SALARY

14 DISPLAY MONTH WISE (IGNORE DATE AND YEAR) TOTAL SALARY, SORT ROWS ON MONTH NUBMER.

15 DISPLAY DAY WISE (MON,TUE...) AVERAGE SALARY, SORT ROWS ON DAY NUMBER OF WEEK.

*/ 






