from data import db_connection

def add_Employee():
    connectionTODB = db_connection()
    
    emp_name = input("enter emp name :-- ")
    emp_salary = float(input("enter emp salary :-- "))
    emp_dept = input("enter emp dept :-- ")
    emp_loc = input("enter emp loc :-- ")
    
    cur = connectionTODB.cursor()  # cursor object
    
    cur.execute(
        "INSERT INTO employees (emp_name, emp_salary, emp_dept, emp_loc) VALUES (%s, %s, %s, %s)",
        (emp_name, emp_salary, emp_dept, emp_loc)
    )
    
    connectionTODB.commit()
    cur.close()
    connectionTODB.close()
    
print("Employee added successfully...")


from data import db_connection

def add_Employee():
    connectionTODB = db_connection()
    
    emp_name = input("enter emp name :-- ")
    emp_salary = float(input("enter emp salary :-- "))
    emp_dept = input("enter emp dept :-- ")
    emp_loc = input("enter emp loc :-- ")
    
    cur = connectionTODB.cursor()  # cursor object
    
    cur.execute(
        "INSERT INTO employees (emp_name, emp_salary, emp_dept, emp_loc) VALUES (%s, %s, %s, %s)",
        (emp_name, emp_salary, emp_dept, emp_loc)
    )
    
    connectionTODB.commit()
    cur.close()
    connectionTODB.close()
    
print("Employee added successfully...")


def view_Employee():
    connectionTODB = db_connection()
    cur = connectionTODB.cursor()
    
    cur.execute("SELECT * FROM employees")
    records = cur.fetchall()
    
    if not records:
        print("No employee records found")
    else:
        for row in records:
            print(row)
    
    cur.close()
    connectionTODB.close()
    
    print("Employee data fetched successfully...") 


    

def update_Employee():
    connectionTODB = db_connection()
    cur = connectionTODB.cursor()

    emp_id = int(input("Enter Employee ID to update :-- "))
    new_salary = float(input("Enter new salary :-- "))
    new_dept = input("Enter new department :-- ")
    new_loc = input("Enter new location :-- ")

    cur.execute(
        "UPDATE employees SET emp_salary=%s, emp_dept=%s, emp_loc=%s WHERE emp_id=%s",
        (new_salary, new_dept, new_loc, emp_id)
    )

    if cur.rowcount > 0:
        connectionTODB.commit()
        print("Employee updated successfully")
    else:
        print("Employee ID not found")

    cur.close()
    connectionTODB.close()


def delete_Employee():
    connectionTODB = db_connection()
    cur = connectionTODB.cursor()

    emp_id = int(input("Enter Employee ID to delete :-- "))

    cur.execute(
        "DELETE FROM employees WHERE emp_id=%s",
        (emp_id,)
    )

    if cur.rowcount > 0:
        connectionTODB.commit()
        print("Employee deleted successfully")
    else:
        print("Employee ID not found")

    cur.close()
    connectionTODB.close()