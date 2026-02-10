# Write your MySQL query statement below
select d2.name as Employee from Employee as d1
join Employee as d2
on d1.id=d2.managerId
where d2.salary>d1.salary;