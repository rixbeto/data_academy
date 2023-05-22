SELECT 
COUNT(S.id) as students,
RC.id,
RC.title,
RC.grade

FROM 

relationalapp_student S
INNER JOIN 
relationalapp_coursestudent RS
ON S.id = RS.student_id
INNER JOIN 
relationalapp_course RC 
ON RS.course_id =  RC.id
GROUP BY RC.id
ORDER BY RC.grade