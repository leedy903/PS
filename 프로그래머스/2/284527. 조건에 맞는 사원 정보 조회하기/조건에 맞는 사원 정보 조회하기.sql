select sum(grade.score) as score, emp.emp_no, emp.emp_name, emp.position, emp.email
from hr_employees as emp
join hr_grade as grade
on emp.emp_no = grade.emp_no
group by grade.emp_no
order by sum(grade.score) desc
limit 1