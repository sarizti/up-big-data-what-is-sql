
import _sqlite3
import pandas as pd

connection = _sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

def query_to_df(query):
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [d[0] for d in cursor.description]
    return pd.DataFrame(rows, columns=columns)

df = query_to_df("""
SELECT
    students.name || ' ' || students.last_name AS "Student Name",
    enrollments.grade AS "Calificacion",
    courses.semester AS "Semestre",
    CASE t.degree
        WHEN 'doctorade' THEN 'Dr.'
        WHEN 'masters' THEN 'Mtro.'
        ELSE 'Lic.'
    END ||' '|| t.name ||' '|| t.last_name AS "Profesor",
    classes.name || ' (' || classes.school || ')' AS "Clase"
FROM enrollments
INNER JOIN students on enrollments.student_id = students.id
INNER JOIN courses on enrollments.course_id = courses.id
INNER JOIN teachers as t on courses.teacher_id = t.id
INNER JOIN classes on courses.class_id = classes.id;
""")

df.to_csv('report.csv')

