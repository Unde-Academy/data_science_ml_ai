#import sqlite3
import sqlite3

#create connection
conn = sqlite3.connect('employee.db')

#create the cursor
cursor = conn.cursor()

#create employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          salary INTEGER)
""")

#insert employees into the table 
employees  = [
    ('John ', 45000),
    ('Elma ', 60000),
    ('Enock ', 75000),
    ('Preston ', 50000),

]

cursor.executemany("INSERT INTO employees (name, salary) VALUES(?, ?)", employees)

#commit the changes 
conn.commit()

#query for all employee names and salary who receive more than 50000
cursor.execute("SELECT name, salary FROM employees WHERE salary > 50000")
results = cursor.fetchall()

#output the results
print("Employees who receive more than 50000:")
for row in results:
   print(f"Name: {row[0]}, Salary: {row[1]}")

#close connection
conn.close()