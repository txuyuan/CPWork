SELECT Student.Gender, COUNT(*) AS Total, AVG(Record.Weight) AS Weight, AVG(Record.Height) AS Height
FROM Student
OUTER LEFT JOIN StudentHealthRecord Record ON Student.StudentID = Record.StudentID
GROUP BY Student.Gender
