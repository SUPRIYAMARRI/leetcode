# Write your MySQL query statement below
select firstname,lastname,city,state from person
left JOIN address
ON person.personId=address.personId;