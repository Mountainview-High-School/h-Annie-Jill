import os
os.system('cls')
import sqlite3
connection = sqlite3.connect("newdb.db")
cursor = connection.cursor()
cursor.execute("SELECT first_name, last_name FROM student")

students = cursor.fetchall()
print("All students")
for student in students:
    print(student)                                                                                                                                                                              
connection.close()