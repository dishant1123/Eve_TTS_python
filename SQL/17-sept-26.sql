/*
where : condition  

select colname1 ,colname2 from table_name where condition 
*/
use scott;
select * from  employees;

-- 1. print  employees name  who's work in department_id =90 

select first_name , department_id 
from employees 
where department_id =90;

-- 2. print  employees name  who's work in department_id =90 and  60 
select first_name , department_id ,salary
from employees 
where department_id =90 or department_id =60;

-- 3. count to the  total employees who working  witb=h manager_id =124. 

select  count(*) as count_of_manager_id_124 
from employees 
where manager_id =124; 

-- 4. print  only those  employees who's  name  start with "E". 

select first_name , salary  
from 
employees 
where first_name like 'E%';

-- 5. print  only those  employees who's  name second letter with 'e'. 
select first_name , salary  
from 
employees 
where first_name like '_e%';   

/*
(using like  function) ---> start word --->word%  
ending  word --->%word
for example : print those  name  which contain 'e'  ----> like %word% 
for example : print those  name  which contain 'e' in second  letter  ----> like _word% 
*/

-- update : 
/*
syntax : 

update  table_name  
set col_name 
where condition 
*/
use ds_students; 
select * from dsstudents;

-- update jyot salary 46000 

update dsstudents 
set salary=46000 
where id =1; 

-- update id =1 all  information  
update dsstudents 
set salary=460000,
	name ='parag',
    age=31
where id =1; 
 
-- delete  
/*
syntax : 

delete  from table_name 
where condition
*/

delete from dsstudents 
where id=1;