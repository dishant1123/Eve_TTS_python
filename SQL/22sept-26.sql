/*
1. increment the salary 20% 
2. INCREMENT IS BASED ON DEPARTMENT_ID : 20 +2000 , 50 +1500 , 80 +1000 , REMAINING +500 ---->case when 
3. MANAGER_ID : 100 40% , 124 +1500 , 149 20% , REMAINING 12.5%
4. BASED SALARY RANGE : 0-6000 40% , 6001-9000 30% , 9001-13000 20% , REMAINING 10%
-- hint  between 	
5. HW :JOB_ID : IT_PROG MK_MAN +2000 , SA_REP MK_REP AD_ASST +1500 , ST_CLERK AD_VP +1000 , REMAINING +500
6. department wise min max avg salary . ----> group by
7.COUNT THOSE WHO WORKS IN DEPARTMENT 50
8. department wise avg salary and display  salary >7500 ----> group by +having
9.DISPLAY JOB WISE TOTAL SALARY, DISPLAY ONLY THOSE ROW WHICH HAS HIGHEST SALARY LOWER THAN 10000 ---> group by +having
10 .DISPLAY JOB WISE TOTAL SALARY, DISPLAY ROWS OF IT_PROG ST_CLERK AD_VP ----> group by +having +IN

*/

use  scott;
-- 7 : 7.COUNT THOSE WHO WORKS IN DEPARTMENT 50 

select count(*) as dept_50_emp
from employees 
where department_id =50;

-- ifnull () function  : 

select first_name ,last_name,ifnull(commission_pct,0) as com_pct,
salary * ifnull(commission_pct,0) as comm_amt,
salary + salary * ifnull(commission_pct,0) as total_salary
from employees;

-- 1. increment the salary 20% 

select first_name , salary , 
salary + (salary*0.2) as inc_salary 
from employees;

-- 2. INCREMENT IS BASED ON DEPARTMENT_ID : 20 +2000 , 50 +1500 , 80 +1000 , REMAINING +500 ---->case when 
/*
	 case when con then ... 
     else 
     end as col_ailas 
*/
select first_name ,salary ,department_id, 
case when department_id =20 then salary +2000 
	 when department_id =50 then salary +1500 
     when department_id =80 then salary +1000
     else salary +500 
     end as department_wise_inc_salary 
from employees ;
     
-- 3. MANAGER_ID : 100 40% , 124 +1500 , 149 20% , REMAINING 12.5%     

select manager_id , salary , 
case when manager_id =100 then salary + (salary*0.4)
	when manager_id =124 then salary + 1500
	when manager_id =149 then salary + (salary*0.2)
    else salary + (salary*0.125)
    end as manager_inc_salary

from  employees ;

-- sort -----> order by 

select first_name ,salary   
from 
employees 
order by salary desc;

select first_name ,salary   
from 
employees 
order by salary asc; 

select first_name ,salary   
from 
employees 
order by 2 desc; 

-- limit  function  :  top print 

select first_name ,salary   
from 
employees 
order by 2 desc
limit 5; 

-- bottom 5 

select first_name ,salary   
from 
employees 
order by 2 asc
limit 5;

select first_name ,salary   
from 
employees 
order by 1 ,2 desc;

 




 




