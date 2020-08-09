# John Quick
# Tutorial from https://www.youtube.com/watch?v=pd-0G0MigUA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=52&t=0s
# Create employees db,
# Add & delete employees from a SQLite database.
# Query & display db instances
# 

import sqlite3
from employee import Employee 
# --------------------------------- CREATE DB ---------------------------------- #
# Connection object representing the database
conn = sqlite3.connect('employee.db')

# Create db in memory to have new db evey time you run the program
conn = sqlite3.connect(':memory:')

# Create a cursor to allow for execution of sql commands
c = conn.cursor()

# Create Employee table that
# holds first name, last name, and pay
c.execute("""CREATE TABLE employees (
   first text,
   last text,
   pay integer
   )""")

# --------------------------------- PYTHON FUCNTIONS ---------------------------------- #
# Insert employees
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first,'last': emp.last,'pay': emp.pay})

# Search and return employees
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
    return c.fetchall()

# Update employee pay
def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
        WHERE first = :first AND last = :last""",
        {'first':emp.first,'last': emp.last, 'pay':pay})

# Remove employee
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first =:first AND last = :last",
        {'first':emp.first,'last': emp.last})


# --------------------------------- CREATE INSTANCES ---------------------------------- #
# Create employee instances from Employee class 
emp_1 = Employee('John', 'Doe', 50987)
emp_2 = Employee('Stewart', 'Dubert', 10268)
emp_3 = Employee('Munchma', 'Quchi', 50987)
emp_4 = Employee('Harry', 'Balzak', 67890)

# # Print employee attributes
# print(emp_2.pay)
# print(emp_3.first)
# print(emp_4.last)
# print(emp_1.first)

# ------------------------------- INSERT INSTANCE INTO DB ----------------------------------- #
# Insert employee instances to db
# c.execute("INSERT INTO employees VALUES ('{}','{}',{})".format(emp_1.first, emp_1.last, emp_1.pay))  # <-- Vulnerable to SQL inkection
# conn.commit()                                                                                        # values are not properly escaped  

# Safe command for inserting employee instances into db
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_3.first, emp_3.last, emp_3.pay))     # Pass tuple as 2nd arg
# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first,'last': emp_2.last,'pay': emp_2.pay})     # Dictionary 
# conn.commit()

# Add employee to database
# c.execute("INSERT INTO employee VALUES ('John', 'Quick', 100000)")
# c.execute("INSERT INTO employee VALUES ('Calvin', 'leCat', 200000)")
# c.execute("INSERT INTO employee VALUES ('Jerry', 'Junky', 20)")
# conn.commit()

# Inser into db using python function
insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)
insert_emp(emp_4)

# --------------------------------- QUERY DB INSTANCES ---------------------------------- #

# Queries db for employee with last name "Quick"
# c.execute("SELECT * FROM employees WHERE last='Quick'")

# Query db using placeholder (tuple)
# c.execute("SELECT * FROM employees WHERE last=?", ('Quchi',))

# # print(c.fetchone()) # Returns next row of results
# # # c.fetchmany(5)    # Returns specified number or rows
# print(c.fetchall())      # Returns remaining rows of results

# # Query db using placeholder (dictionary)
# c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
# print(c.fetchall())

# # commit to database
# conn.commit()

# Get employee using Python function
emps = get_emps_by_name('Quchi')
print(emps)

update_pay(emp_3, 78909)
remove_emp(emp_4)

emps = get_emps_by_name('Quchi')
print(emps)

# # close database
conn.close()