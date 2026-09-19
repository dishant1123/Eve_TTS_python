use  scott;

select * from employees;

select salary as frist_salary , first_name 
from 
employees;

-- 1. DISPLAY THOSE WHO REPORTS TO MANAGER_ID 100 , 124 OR 149

select first_name ,manager_id 
from 
employees 
where MANAGER_ID in (100,124,149);


select first_name , salary  
from employees 
where salary  > 5000 
and salary <10000;

-- conditional  op : 
select first_name , salary  
from employees 
where salary  between 5000 and 10000; 

-- aithematic  op  

select first_name ,salary ,salary*12 as annual_salary
from 
employees;


