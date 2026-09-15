/*
data base :  information  ----->tables 
query for  creating  database : 

create databases database_name; 
create databases if not exists database_name  

query for creating  table  : 
create table table_name

query  for insert data  : 
insert into table_name values ()

query for  print  all row  and  col into the table : 

select  * (asctics)  from table_name; 

*/

create database DS_students;

/*
	id   name  		age   salary 
    1    jyot  		20    34000
    2    meghprit   21    37000
    3    priyanka   20    32000
		
*/
use ds_students;

create table dsstudents (
	id  int primary key,
    name varchar(30),
    age int,
    salary int
);

insert into dsstudents values 
(1,"jyot",20,34000),
(2,"priyanka",21,32000),
(3,"meghpreet",22,37000) ;

select * from dsstudents;






