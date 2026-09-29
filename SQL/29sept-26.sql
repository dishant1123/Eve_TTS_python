/*
types of  join  : 

1. inner join   : when  two table have same  column name  then only  inner join  perform. 
2. left join
3. right join  
4. outer join  
5. self join   

1.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID — USING ,ON

2.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID, BOTH MANAGER_ID — USING ,ON

3.FIRST_NAME, DEPARTMENT_NAME, CITY — USING

4.FIRST_NAME, DEPARTMENT_NAME, CITY, COUNTRY_NAME 

5.DISPLAY DEPARTMENT_NAME , REGION_NAME (ON)

6.Departments in which no employee is hired

7.Employees whose Department_ID is not decided

8.Regions in which no country exists

9.Countries in which no location is fixed

10.Employees who HAVE got promotion ----> use  job_history table 

*/

use scott; 
select * from  employees;
select * from  departments; 

-- 1.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID — USING ,ON

select e.first_name ,e.department_id 
from employees e 
join departments d 
on e.department_id = d.department_id;

-- 2.FIRST_NAME, DEPARTMENT_NAME, DEPARTMENT_ID, BOTH MANAGER_ID — USING ,ON

select e.first_name, e.department_id , e.manager_id ,d.department_name 
from employees e
join  departments d 
on e.department_id = d.department_id
join departments ds  
on e.manager_id = ds.manager_id;

-- 3 .FIRST_NAME, DEPARTMENT_NAME, CITY — USING

select e.first_name ,d.department_name,l.city 
from employees e 
	join departments d 
	on e.department_id = d.department_id 
	join locations l 
	on l.location_id = d.location_id ;
    
select * from  employees;
select * from  departments;
select * from  locations;



