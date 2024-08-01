SELECT Student.Name, Student.Gender, Record.Weight, Record.Height
FROM Student
OUTER LEFT JOIN StudentHealthRecord AS Record ON Student.StudentID = Record.StudentID
ORDER BY Student.Name DESC
ORDER BY Student.Gender ASC
