# Link   =   (https://likegeeks.com/python-sqlite3-tutorial/)
""" DATABASE API """
import sqlite3
import datetime
from sqlite3 import Error

# to make connection to DATABASE
con = sqlite3.connect("test.db")

# Cursor to execute querys
cur = con.cursor()
cur.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
cur.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(3, 'Ash', 900, 'IT', 'Tech', '2020-02-06')''')
cur.execute('UPDATE employees SET name = "Rogers" where id = 2')
cur.execute('SELECT * FROM employees')
con.commit()     # to save changes

# to retrive data
rows = cur.fetchall()
for row in rows:
    print(row)
# OR
[print(row) for row in cur.fetchall()]


cur.execute('SELECT id, name FROM employees WHERE salary > 800.0')
[print(row) for row in cur.fetchall()]


cur.execute('create table if not exists projects(id integer, name text)')
con.commit()

# DROP table
cur.execute('DROP table if exists employees')
cur.execute('DROP table if exists employees')
con.commit()


# (Bulk insert)
cur.execute('create table if not exists projects(id integer, name text)')
data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")]
cur.executemany("INSERT INTO projects VALUES(?, ?)", data)
con.commit()

cur.execute('create table if not exists assignments(id integer, name text, date date)')
data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
cur.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
con.commit()


cur.execute('SELECT name from sqlite_master where type= "table"')
print(cur.fetchall())

con.close()
